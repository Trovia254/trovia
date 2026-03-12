document.addEventListener('DOMContentLoaded', () => {
  const observer = new IntersectionObserver(
    (entries) => entries.forEach((e) => {
      if (e.isIntersecting) {
        e.target.style.opacity = '1';
        e.target.style.transform = 'translateY(0)';
        observer.unobserve(e.target);
      }
    }),
    { threshold: 0.1, rootMargin: '0px 0px -50px 0px' }
  );
  document.querySelectorAll('[data-animate]').forEach((el) => {
    el.style.opacity = '0';
    el.style.transform = 'translateY(20px)';
    el.style.transition = 'opacity 0.6s ease, transform 0.6s ease';
    observer.observe(el);
  });
});
