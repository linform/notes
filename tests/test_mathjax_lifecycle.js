"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const test = require("node:test");
const vm = require("node:vm");

const source = fs.readFileSync(
  path.join(__dirname, "..", "docs", "javascripts", "mathjax.js"),
  "utf8",
);

function deferred() {
  let resolve;
  const promise = new Promise((yes) => {
    resolve = yes;
  });
  return { promise, resolve };
}

async function eventually(predicate, message) {
  const deadline = Date.now() + 2000;
  while (!predicate() && Date.now() < deadline) {
    await new Promise((resolve) => setTimeout(resolve, 5));
  }
  assert.ok(predicate(), message);
}

function browser(t, { initialDocumentReady = true } = {}) {
  const subscribers = [];
  const timers = new Set();
  const errors = [];
  const calls = [];
  const operations = [];
  const startup = deferred();
  let page = "initial";
  let active = 0;
  let maxActive = 0;
  let typesetter = () => Promise.resolve();
  let article = { page, isConnected: true, querySelectorAll: () => [] };
  const document = {
    readyState: "complete",
    body: { contains: (node) => node.isConnected },
    documentElement: { contains: (node) => node.isConnected },
    querySelector: () => article,
    querySelectorAll: () => [],
  };
  const context = {
    document,
    document$: {
      subscribe(callback) {
        subscribers.push(callback);
        // Material replays the current document to a newly registered subscriber.
        if (initialDocumentReady) callback(document);
        return { unsubscribe() {} };
      },
    },
    console: { error: (...args) => errors.push(args), warn() {}, log() {} },
    setTimeout(callback, delay, ...args) {
      const timer = setTimeout(() => {
        timers.delete(timer);
        callback(...args);
      }, delay);
      timers.add(timer);
      return timer;
    },
    clearTimeout(timer) {
      clearTimeout(timer);
      timers.delete(timer);
    },
  };
  context.window = context;
  context.globalThis = context;
  vm.createContext(context);
  t.after(() => {
    for (const timer of timers) clearTimeout(timer);
  });

  return {
    calls,
    errors,
    operations,
    evaluate() {
      vm.runInContext(source, context, { filename: "mathjax.js" });
    },
    installRuntime({ clearCache = true } = {}) {
      const mathjax = context.MathJax;
      function Menu() {}
      Menu.prototype.rerender = () => Promise.resolve();
      mathjax._ = {
        mathjax: { mathjax: { handleRetriesFor: (callback) => callback() } },
        core: { MathItem: { STATE: { TYPESET: 150 } } },
        ui: { menu: { Menu: { Menu } } },
      };
      mathjax.startup.promise = startup.promise;
      mathjax.startup.defaultReady = () => {};
      const output = clearCache
        ? { clearCache: () => operations.push("clearCache") }
        : {};
      mathjax.startup.output = output;
      mathjax.startup.document = { outputJax: output };
      mathjax.typesetClear = () => operations.push("typesetClear");
      mathjax.texReset = () => operations.push("texReset");
      mathjax.typesetPromise = (...args) => {
        const target = args[0]?.[0];
        const call = { page: target?.page ?? page, target };
        calls.push(call);
        operations.push("typesetPromise");
        active += 1;
        maxActive = Math.max(maxActive, active);
        return Promise.resolve()
          .then(() => typesetter(call, ...args))
          .finally(() => {
            active -= 1;
          });
      };
      mathjax.startup.ready?.();
    },
    finishStartup() {
      startup.resolve();
    },
    navigate(name) {
      page = name;
      article.isConnected = false;
      article = { page, isConnected: true, querySelectorAll: () => [] };
      initialDocumentReady = true;
      for (const callback of subscribers) callback(document);
    },
    replayCurrentDocument() {
      initialDocumentReady = true;
      for (const callback of subscribers) callback(document);
    },
    setTypesetter(callback) {
      typesetter = callback;
    },
    switchRenderer(clearCache) {
      // The MathJax menu replaces the document renderer, not startup.output.
      context.MathJax.startup.document.outputJax = { clearCache };
    },
    get active() {
      return active;
    },
    get maxActive() {
      return maxActive;
    },
    get article() {
      return article;
    },
  };
}

async function readyBrowser(t, runtime = {}) {
  const app = browser(t, { initialDocumentReady: false });
  app.evaluate();
  app.installRuntime(runtime);
  app.finishStartup();
  app.replayCurrentDocument();
  await eventually(() => app.calls.length > 0 && app.active === 0, "initial typesetting did not finish");
  return app;
}

test("cold load waits for the delayed MathJax runtime and renders the first page", async (t) => {
  const app = browser(t);
  assert.doesNotThrow(() => app.evaluate());
  assert.equal(app.calls.length, 0);
  app.installRuntime();
  await new Promise((resolve) => setTimeout(resolve, 10));
  assert.equal(app.calls.length, 0, "startup must finish before typesetting");
  app.finishStartup();
  await eventually(() => app.calls.length > 0, "the first page never typeset");
  assert.equal(app.calls.at(-1).page, "initial");
});

test("navigation while MathJax is loading eventually renders the current chapter", async (t) => {
  const app = browser(t);
  app.evaluate();
  app.navigate("chapter-a");
  app.installRuntime();
  app.navigate("chapter-b");
  assert.equal(app.calls.length, 0);
  app.finishStartup();
  await eventually(
    () => app.calls.some((call) => call.page === "chapter-b"),
    "the chapter selected during startup never typeset",
  );
  assert.equal(app.maxActive, 1);
});

test("rapid chapter navigation never overlaps typesetting and reaches the latest chapter", async (t) => {
  const app = await readyBrowser(t);
  const pending = deferred();
  app.setTypesetter((call) => call.page === "chapter-a" ? pending.promise : Promise.resolve());
  app.navigate("chapter-a");
  await eventually(() => app.calls.some((call) => call.page === "chapter-a"), "chapter A never started");
  app.navigate("chapter-b");
  app.navigate("chapter-c");
  await new Promise((resolve) => setTimeout(resolve, 10));
  assert.equal(app.maxActive, 1, "MathJax cannot process two documents concurrently");
  pending.resolve();
  await eventually(
    () => app.calls.some((call) => call.page === "chapter-c") && app.active === 0,
    "the latest chapter never finished typesetting",
  );
  assert.equal(app.maxActive, 1);
});

test("a failed typeset does not prevent the next chapter from rendering", async (t) => {
  const app = await readyBrowser(t);
  app.setTypesetter((call) => {
    if (call.page === "chapter-error") throw new Error("simulated rendering failure");
  });
  app.navigate("chapter-error");
  await eventually(() => app.errors.length > 0 && app.active === 0, "the typesetting error was not handled");
  app.navigate("chapter-recovery");
  await eventually(
    () => app.calls.some((call) => call.page === "chapter-recovery") && app.active === 0,
    "a previous failure permanently blocked navigation rendering",
  );
});

test("replacing an article clears the CHTML style cache before rendering its formulas", async (t) => {
  const app = await readyBrowser(t);
  const before = app.operations.length;
  app.navigate("new-article");
  await eventually(
    () => app.calls.some((call) => call.page === "new-article") && app.active === 0,
    "the replacement article never typeset",
  );
  assert.deepEqual(app.operations.slice(before), [
    "clearCache", "typesetClear", "texReset", "typesetPromise",
  ]);
  assert.equal(app.calls.at(-1).target, app.article, "typesetting must target the replacement article");
});

test("replaying the same article does not clear or reprocess its existing MathML", async (t) => {
  const app = await readyBrowser(t);
  const before = app.operations.length;
  app.replayCurrentDocument();
  app.replayCurrentDocument();
  await new Promise((resolve) => setTimeout(resolve, 20));
  assert.deepEqual(app.operations.slice(before), [], "hash-only events must preserve the rendered article");
});

test("navigation clears the current renderer after a menu switch", async (t) => {
  const app = await readyBrowser(t);
  const before = app.operations.length;
  app.switchRenderer(() => app.operations.push("currentRendererClearCache"));
  app.navigate("switched-renderer-chapter");
  await eventually(
    () => app.calls.some((call) => call.page === "switched-renderer-chapter") && app.active === 0,
    "the chapter never rendered after changing output renderer",
  );
  assert.deepEqual(app.operations.slice(before), [
    "currentRendererClearCache", "typesetClear", "texReset", "typesetPromise",
  ], "navigation must clear the current renderer instead of the original startup renderer");
});

test("navigation also works with an output renderer that has no CHTML clearCache", async (t) => {
  const app = await readyBrowser(t, { clearCache: false });
  app.navigate("svg-chapter");
  await eventually(
    () => app.calls.some((call) => call.page === "svg-chapter") && app.active === 0,
    "SVG navigation should not require a CHTML-only API",
  );
  assert.equal(app.errors.length, 0);
});
