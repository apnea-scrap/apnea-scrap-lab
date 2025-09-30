// docs/js/local-banner.js
(function () {
    function addBanner() {
        try {
            const header = document.querySelector('.md-header');
            if (!header) return;

            const bar = document.createElement('div');
            bar.id = 'local-banner';
            bar.textContent = 'Local build';
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
