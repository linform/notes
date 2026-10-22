(() => {
  let queue;
  let renderedArticle;

  function typesetArticle() {
    const article = document.querySelector('.md-content__inner');
    queue = queue.then(async () => {
      if (!article?.isConnected || article === renderedArticle) return;

      // Instant navigation replaces the article and its generated head styles.
      // Rebuild CHTML's stylesheet and forget the previous article's MathItems.
      MathJax.startup.document.outputJax.clearCache?.();
      MathJax.typesetClear();
      MathJax.texReset();
      await MathJax.typesetPromise([article]);
      renderedArticle = article;
    }).catch((error) => console.error('MathJax typesetting failed:', error));
  }

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
        // Subscribe after the runtime exists, and keep its startup promise intact.
        queue = MathJax.startup.promise;
        document$.subscribe(typesetArticle);
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
})();
