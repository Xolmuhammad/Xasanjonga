// Tailwind Config 
if(typeof tailwind !== 'undefined') {
  tailwind.config = {
    theme: {
      extend: {
        colors: {
          primary: {
            400: '#fb923c',
            500: '#f97316',
            600: '#ea580c',
          },
          dark: {
            900: '#0f172a',
            800: '#1e293b',
            700: '#334155',
          }
        },
        fontFamily: {
          outfit: ['Outfit', 'sans-serif'],
        }
      }
    }
  }
}

// Mobile Menu Toggle
function toggleMenu() {
  const menu = document.getElementById('mobile-menu');
  if (menu) {
    if (menu.classList.contains('hidden')) {
      menu.classList.remove('hidden');
    } else {
      menu.classList.add('hidden');
    }
  }
}

// Toast Notification System
const Toast = {
  container: null,
  
  init() {
    if (!this.container) {
      this.container = document.createElement('div');
      this.container.className = 'fixed bottom-5 right-5 z-50 flex flex-col gap-3 font-outfit';
      document.body.appendChild(this.container);
    }
  },

  show(message, type = 'success') {
    this.init();
    
    const toast = document.createElement('div');
    const bgClass = type === 'success' ? 'bg-green-500/20 border-green-500' : 
                    type === 'error' ? 'bg-red-500/20 border-red-500' : 
                    'bg-primary-500/20 border-primary-500';
                    
    const iconClass = type === 'success' ? 'fa-check-circle text-green-400' : 
                      type === 'error' ? 'fa-times-circle text-red-400' : 
                      'fa-info-circle text-primary-500';

    toast.className = `glass flex items-center gap-3 px-4 py-3 rounded-lg border-l-4 shadow-lg min-w-[250px] max-w-[350px] toast-enter ${bgClass}`;
    
    toast.innerHTML = `
      <i class="fas ${iconClass} text-xl"></i>
      <p class="text-white text-sm font-medium flex-1">${message}</p>
      <button onclick="this.parentElement.style.display='none'" class="text-gray-400 hover:text-white transition">
        <i class="fas fa-times"></i>
      </button>
    `;

    this.container.appendChild(toast);

    // Auto remove after 3s
    setTimeout(() => {
      if(toast.parentElement) {
        toast.classList.replace('toast-enter', 'toast-exit');
        setTimeout(() => toast.remove(), 300);
      }
    }, 3000);
  }
};

// Global function to add item to cart (demo)
function addToCart(event, itemName) {
  if(event) {
    event.preventDefault();
    event.stopPropagation();
  }
  Toast.show(`${itemName} savatga qo'shildi!`, 'success');
  
  // Animation effect on cart icon
  const cartIcon = document.getElementById('cart-icon-badge');
  const cartIconMobile = document.getElementById('cart-icon-badge-mobile');
  
  [cartIcon, cartIconMobile].forEach(icon => {
    if(icon) {
      icon.classList.add('scale-150', 'bg-red-500');
      let currentVal = parseInt(icon.innerText || '0');
      icon.innerText = currentVal + 1;
      setTimeout(() => {
        icon.classList.remove('scale-150', 'bg-red-500');
      }, 300);
    }
  });
}

// Function to handle layout initialization
document.addEventListener('DOMContentLoaded', () => {
    // Add current year to footer if exists
    const yearSpan = document.getElementById('current-year');
    if(yearSpan) {
        yearSpan.textContent = new Date().getFullYear();
    }
});
