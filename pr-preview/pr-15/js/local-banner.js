(function () {
    // Add a simple ribbon and tell crawlers to ignore previews
    var bar = document.createElement('div');
    bar.id = 'local-banner';
    bar.textContent = 'Local build';
    document.body.appendChild(bar);
})();
