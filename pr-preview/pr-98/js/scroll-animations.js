(function () {
  const animatedElements = document.querySelectorAll('[data-animate="fade-up"]');

  if (!animatedElements.length) {
    return;
  }

  const reveal = (element) => {
    element.classList.add('visible');
  };

  if (!('IntersectionObserver' in window)) {
    animatedElements.forEach(reveal);
    return;
  }

  const observer = new IntersectionObserver(
    (entries, obs) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          reveal(entry.target);
          obs.unobserve(entry.target);
        }
      });
    },
    {
      rootMargin: '0px 0px -10% 0px',
      threshold: 0.2,
    }
  );

  animatedElements.forEach((element) => observer.observe(element));
})();
