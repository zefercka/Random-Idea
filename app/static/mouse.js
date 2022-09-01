window.onload = function() {
    $(".instruction-btn").hover(function () {
        $("body div:not(.instruction), header").css("filter", "blur(1rem)"); // Размытие заднего фона
        $(".instruction").css("visibility", "visible"); // Видимость окошка
    },  function() {
        $("body div:not(.instruction), header").css("filter", "blur(0)"); // Убираем размытие
        $(".instruction").css("visibility", "hidden"); // Прячем окошко
    });
}