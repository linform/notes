window.MathJax = {
  startup: {
    typeset: false,
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
