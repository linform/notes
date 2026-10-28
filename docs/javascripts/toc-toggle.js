/* Keep the theme's generated TOC expanded by default; reader toggle is per-page only. */
(() => {
  function initialize() {
    const sidebar = document.querySelector('.md-sidebar--secondary:not([hidden])');
    const nav = sidebar?.querySelector('.md-nav--secondary');
    if (!nav?.querySelector('a[href]') || sidebar.querySelector('.notes-toc-toggle')) return;

    let collapsed = false;
    nav.id = 'notes-page-toc';
    const button = document.createElement('button');
    button.type = 'button';
    button.className = 'notes-toc-toggle';
    button.setAttribute('aria-controls', nav.id);
    sidebar.prepend(button);
    sidebar.classList.add('notes-toc');

    function render() {
      sidebar.classList.toggle('notes-toc--collapsed', collapsed);
      button.textContent = collapsed ? '展开目录' : '收起目录';
      button.setAttribute('aria-expanded', String(!collapsed));
    }

    button.addEventListener('click', () => {
      collapsed = !collapsed;
      render();
    });
    render();
  }

  // Material emits on initial load and when instant navigation is enabled.
  if (typeof document$ !== 'undefined') {
    document$.subscribe(initialize);
  } else if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', initialize, { once: true });
  } else {
    initialize();
  }
})();
