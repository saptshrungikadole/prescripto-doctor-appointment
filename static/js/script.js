/* ================================================
   PRESCRIPTO — Global JavaScript
================================================ */

// ── NAVBAR SCROLL EFFECT ─────────────────────
const navbar = document.getElementById('navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.classList.toggle('scrolled', window.scrollY > 20);
  });
}

// ── SCROLL REVEAL ANIMATIONS ─────────────────
const observer = new IntersectionObserver((entries) => {
  entries.forEach(entry => {
    if (entry.isIntersecting) {
      entry.target.classList.add('visible');
    }
  });
}, { threshold: 0.12 });

document.querySelectorAll('.fade-up').forEach(el => observer.observe(el));

// ── TOAST NOTIFICATION SYSTEM ────────────────
function showToast(message, type = 'success') {
  const container = document.getElementById('toastContainer');
  if (!container) return;

  const toast = document.createElement('div');
  toast.className = `toast ${type}`;

  const icon = type === 'success' ? '✅' : '❌';
  toast.innerHTML = `
    <span class="toast-icon">${icon}</span>
    <span class="toast-text">${message}</span>
  `;

  container.appendChild(toast);

  setTimeout(() => {
    toast.style.animation = 'slideIn 0.3s ease reverse';
    setTimeout(() => toast.remove(), 300);
  }, 3500);
}

// ── ACTIVE NAV LINK ───────────────────────────
const currentPath = window.location.pathname;
document.querySelectorAll('.nav-links a').forEach(link => {
  if (link.getAttribute('href') === currentPath) {
    link.style.color = 'var(--navy)';
    link.style.fontWeight = '700';
  }
});

// ── FORM SUBMIT FEEDBACK ─────────────────────
// Only applies to forms that do NOT have their own JS validation handler.
// Forms with id="registerForm" or id="loginForm" handle their own submit buttons.
const SELF_VALIDATED_FORMS = ['registerForm', 'loginForm'];

document.querySelectorAll('form').forEach(form => {
  if (SELF_VALIDATED_FORMS.includes(form.id)) return; // skip — handled by page JS

  form.addEventListener('submit', function () {
    const btn = this.querySelector('[type="submit"], .btn-submit');
    if (btn) {
      btn.textContent  = '⏳ Processing...';
      btn.style.opacity = '0.8';
      btn.disabled     = true;
      setTimeout(() => {
        btn.disabled     = false;
        btn.style.opacity = '1';
      }, 4000);
    }
  });
});
