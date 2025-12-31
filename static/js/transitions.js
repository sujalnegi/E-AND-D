document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('page-container');

    if (container) {
        setTimeout(() => {
            container.classList.remove('translate-x-full', '-translate-x-full', 'opacity-0', 'translate-y-10');
            container.classList.add('translate-x-0', 'translate-y-0', 'opacity-100');
        }, 100);
    }

    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && href.startsWith('/') && container) {
                e.preventDefault();

                container.classList.remove('translate-x-0', 'translate-y-0', 'opacity-100');

                if (href === '/encryption') {
                    container.classList.add('translate-x-full', 'opacity-0');
                } else if (href === '/decryption') {
                    container.classList.add('-translate-x-full', 'opacity-0');
                } else {
                    container.classList.add('opacity-0');
                }

                setTimeout(() => {
                    window.location.href = href;
                }, 700); 
            }
        });
    });
});
