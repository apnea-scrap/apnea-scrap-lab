// docs/js/local-banner.js
(function () {
    function addBanner() {
        try {
            const header = document.querySelector('.md-header');
            if (!header) return;

            var m = document.querySelector('meta[name="robots"]');
            if (!m) {
                m = document.createElement('meta');
                m.setAttribute('name', 'robots');
                document.head.appendChild(m);
            }
            m.setAttribute('content', 'noindex,nofollow');

            var ref = (window.location.pathname.match(/\/preview\/([^/]+)/) || [,'preview'])[1];
            const bar = document.createElement('div');
            bar.id = 'preview-banner';
            bar.textContent = 'Preview build: ' + ref + ' — not for indexing';
            header.prepend(bar); // inside the header
        } catch (e) {
            console.error('local-banner failed:', e);
        }
    }
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', addBanner);
    } else {
        addBanner();
    }
})();
