window.MathJax = {
  startup: {
    typeset: false,
    ready() {
      // MathJax 3.2.2's menu rerender must handle asynchronous speech retries.
      // Upstream workaround: https://github.com/mathjax/MathJax/issues/3124#issuecomment-1804381865
      const { mathjax } = MathJax._.mathjax;
      const { STATE } = MathJax._.core.MathItem;
      const { Menu } = MathJax._.ui.menu.Menu;
      const rerender = Menu.prototype.rerender;
      Menu.prototype.rerender = function (start = STATE.TYPESET) {
        return mathjax.handleRetriesFor(() => rerender.call(this, start));
      };
      MathJax.startup.defaultReady();
    },
  },
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex",
  },
};

document$.subscribe(() => {
  // Wait for initial typesetting and serialize subsequent document events.
  // Clearing math still present in the DOM reprocesses its assistive MathML.
  MathJax.startup.promise = MathJax.startup.promise
    .then(() => MathJax.typesetPromise())
    .catch((error) => console.error("MathJax typesetting failed:", error));
});
