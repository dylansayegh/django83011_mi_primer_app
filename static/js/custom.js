// CAMISETAS RETRO DS - JavaScript Personalizado

// Funciones globales para el e-commerce
class CamisetasRetro {
    constructor() {
        this.init();
    }

    init() {
        this.initScrollAnimations();
        this.initNotifications();
        this.initLazyLoading();
    }

    // Animaciones al hacer scroll
    initScrollAnimations() {
        const observerOptions = {
            threshold: 0.1,
            rootMargin: '0px 0px -50px 0px'
        };

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('fade-in');
                }
            });
        }, observerOptions);

        document.querySelectorAll('.camiseta-item').forEach(item => {
            observer.observe(item);
        });
    }

    // Sistema de notificaciones
    initNotifications() {
        this.showNotification = (message, type = 'success') => {
            const notification = document.createElement('div');
            notification.className = `alert alert-${type} position-fixed`;
            notification.style.cssText = 'top: 20px; right: 20px; z-index: 9999; min-width: 300px;';
            notification.innerHTML = `
                ${message}
                <button type="button" class="btn-close" data-bs-dismiss="alert"></button>
            `;
            
            document.body.appendChild(notification);
            
            setTimeout(() => {
                notification.remove();
            }, 3000);
        };
    }

    // Carga lazy de imágenes
    initLazyLoading() {
        if ('IntersectionObserver' in window) {
            const imageObserver = new IntersectionObserver((entries) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        const img = entry.target;
                        img.src = img.dataset.src;
                        img.classList.remove('lazy');
                        imageObserver.unobserve(img);
                    }
                });
            });

            document.querySelectorAll('img[data-src]').forEach(img => {
                imageObserver.observe(img);
            });
        }
    }
}

// Funciones específicas del carrito
const CartManager = {
    // Actualizar contador con animación
    updateCounter(count) {
        const counter = document.querySelector('.cart-counter');
        if (counter) {
            counter.textContent = count;
            counter.classList.add('pulse');
            setTimeout(() => counter.classList.remove('pulse'), 300);
        }
    },

    // Agregar producto con feedback
    addProduct(productId, quantity = 1) {
        const button = event.target;
        const originalText = button.innerHTML;
        
        button.innerHTML = '<div class="custom-loader"></div>';
        button.disabled = true;

        // Simular petición AJAX
        fetch(`/agregar-al-carrito/${productId}/`, {
            method: 'POST',
            headers: {
                'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ cantidad: quantity })
        })
        .then(response => response.json())
        .then(data => {
            if (data.success) {
                window.camisetasRetro.showNotification('¡Producto agregado al carrito!', 'success');
                this.updateCounter(data.cart_count);
            } else {
                window.camisetasRetro.showNotification('Error al agregar producto', 'danger');
            }
        })
        .finally(() => {
            button.innerHTML = originalText;
            button.disabled = false;
        });
    }
};

// Inicializar cuando el DOM esté listo
document.addEventListener('DOMContentLoaded', () => {
    window.camisetasRetro = new CamisetasRetro();
    
    // Agregar smooth scrolling
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({ behavior: 'smooth' });
            }
        });
    });
});

// Exportar funciones globales
window.CartManager = CartManager;
