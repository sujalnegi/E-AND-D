document.addEventListener('DOMContentLoaded', () => {
    const container = document.getElementById('page-container');

    if (container.classList.contains('translate-x-full')) {
        setTimeout(() => {
            container.classList.remove('translate-x-full', 'opacity-0');
            container.classList.add('translate-x-0', 'opacity-100');
        }, 50);
    }

    const links = document.querySelectorAll('a');
    links.forEach(link => {
        link.addEventListener('click', (e) => {
            const href = link.getAttribute('href');
            if (href && href.startsWith('/')) {
                e.preventDefault();
                container.classList.remove('translate-x-0');

                if (href === '/encryption') {
                    container.classList.add('translate-x-full', 'opacity-0');
                } else if (href === '/decryption') {
                    container.classList.add('-translate-x-full', 'opacity-0');
                } else {
                    container.classList.add('translate-x-full', 'opacity-0');
                }
                setTimeout(() => {
                    window.location.href = href;
                }, 500); 
            }
        });
    });
});
