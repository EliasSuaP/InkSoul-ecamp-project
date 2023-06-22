// Función que se ejecuta al hacer clic en el botón "Back to Top"
function topFunction() {
    document.body.scrollTop = 0; // Para navegadores que no sean Chrome
    document.documentElement.scrollTop = 0; // Para Chrome, Firefox, IE y Opera
}

// Muestra u oculta el botón "Back to Top" en función de la posición de desplazamiento
window.onscroll = function() {
    scrollFunction();
};

function scrollFunction() {
    if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        document.getElementById("backToTopBtn").style.display = "block";
    } else {
        document.getElementById("backToTopBtn").style.display = "none";
    }
}
