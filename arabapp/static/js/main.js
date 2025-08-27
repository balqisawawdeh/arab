// تحميل الترجمة وتبديل اللغة
let translations = {};

fetch("/static/lang/translations.json")
  .then(response => response.json())
  .then(data => {
    translations = data;
    switchLanguage("ar"); // اللغة الافتراضية
  });

function switchLanguage(lang) {
  document.documentElement.lang = lang;
  document.documentElement.dir = lang === "ar" ? "rtl" : "ltr";

  const keys = [
    "title", "description", "title2", "description2",
    "section-title", "section-text",
    "about-title", "about-text",
    "companies-title", "arabbro-title", "arabbro-text",
    "fip-title", "fip-text", "sma-title", "sma-text",
    "services-title", "service1", "service2", "service3", "service4",
    "partners-title", "partners-text",
    "projects-title", "projects-text",
    "values-title", "value1", "value2", "value3",
    "contact-title", "contact-text",
    "label-name", "label-email", "label-message", "submit-button"
  ];

  keys.forEach(id => {
    const el = document.getElementById(id);
    if (el && translations[lang][id]) {
      el.textContent = translations[lang][id];
    }
  });
}

// التعامل مع النموذج
document.addEventListener("DOMContentLoaded", () => {
  const form = document.getElementById("contact-form");
  if (form) {
    form.addEventListener("submit", function (e) {
      e.preventDefault();
      alert("✅ Form submitted");
      form.reset();
    });
  }

  // Swiper تم تفعيله مسبقًا من index.html
});
(function ($) {
  "use strict";
  $(document).ready(function () {
    ///============= Nav Menu Sidebar Popup  =============\\\
    $(".nav_menu_popup-99 .nav_menu_bar i").on("click", function () {
      $(".nav_menu_popup-99 .nav_menu_bar-popup").addClass("show");
    });
    $(".nav_menu_popup-99 .nav_menu_bar-popup-close").on("click", function () {
      $(".nav_menu_popup-99 .nav_menu_bar-popup").removeClass("show");
    });
    ///============= * Responsive Menu Toggle  =============\\\
    var mobileItems = jQuery('.vertical_menu-99');
    mobileItems.find('ul li.menu-item-has-children, ul li.mega-menu-enabled').append('<span class="mobile-arrows far fa-plus"></span>');

    jQuery(".vertical_menu-99 .mobile-arrows").click(function () {
      jQuery(this).parent().find('ul.sub-menu:first, .mega-menu-wrap').slideToggle(300);
      jQuery(this).parent().find('> .mobile-arrows').toggleClass('is-open');
    });
    // ///============= * MegaMenu Width  =============\\\
    function setMegaMenuStyles() {
      var windowWidth = $(window).width();
      if (windowWidth >= 1000) {
        $('.header_mega-menu .mega-menu-wrap').each(function () {
          var leftPosition = Math.floor($(this).position().left - $(this).offset().left);
          $(this).css({
            'width': windowWidth + 'px',
            'left': leftPosition + 'px'
          });
        });
      } else {
        $('.header_mega-menu .mega-menu-wrap').each(function () {
          $(this).css({
            'width': '',
            'left': ''
          });
        });
      }
    }
    $(document).ready(function () {
      setMegaMenuStyles();
      $(window).resize(function () {
        setMegaMenuStyles();
      });
    });
  });
})(jQuery);
