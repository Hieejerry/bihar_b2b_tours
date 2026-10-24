const toggle = document.querySelector('.nav-toggle');
const nav = document.querySelector('.main-nav');

if (toggle && nav) {
  toggle.addEventListener('click', () => {
    const isOpen = nav.classList.toggle('is-open');
    toggle.classList.toggle('is-open', isOpen);
    toggle.setAttribute('aria-expanded', String(isOpen));
  });

  nav.querySelectorAll('a').forEach((link) => {
    link.addEventListener('click', () => {
      nav.classList.remove('is-open');
      toggle.classList.remove('is-open');
      toggle.setAttribute('aria-expanded', 'false');
    });
  });
}

async function setupDestinationGalleries() {
  const galleryUrl = document.body.dataset.galleryUrl;
  const galleryContainers = document.querySelectorAll('.destination-gallery');
  if (!galleryUrl || !galleryContainers.length) return;

  try {
    const response = await fetch(galleryUrl, { headers: { Accept: 'application/json' } });
    if (!response.ok) throw new Error('Gallery list unavailable');
    const galleries = await response.json();

    galleryContainers.forEach((gallery) => {
      const images = galleries[gallery.dataset.destination] || [];
      if (!images.length) return; // Keep the built-in fallback photo until local images are added.

      gallery.replaceChildren();
      const slides = images.map((source, index) => {
        const image = document.createElement('img');
        image.src = source;
        image.alt = `${gallery.dataset.destination} destination image ${index + 1}`;
        image.loading = index === 0 ? 'eager' : 'lazy';
        image.classList.toggle('is-active', index === 0);
        gallery.appendChild(image);
        return image;
      });

      if (slides.length < 2) return;
      let activeSlide = 0;
      window.setInterval(() => {
        slides[activeSlide].classList.remove('is-active');
        activeSlide = (activeSlide + 1) % slides.length;
        slides[activeSlide].classList.add('is-active');
      }, 4500);
    });
  } catch (error) {
    // If the manifest cannot load, the fallback images already on the page stay visible.
  }
}

setupDestinationGalleries();
