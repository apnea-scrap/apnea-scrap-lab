(function () {
    // Add a simple ribbon and tell crawlers to ignore previews
    var m = document.createElement('meta');
    m.setAttribute('name', 'robots');
    m.setAttribute('content', 'noindex,nofollow');
    document.head.appendChild(m);

    var ref = (window.location.pathname.match(/\/preview\/([^/]+)/) || [,'preview'])[1];
    var bar = document.createElement('div');
    bar.id = 'preview-banner';
    bar.textContent = 'Preview build: ' + ref + ' — not for indexing';
    document.body.appendChild(bar);
})();
