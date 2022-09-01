function generator_get()
{
    $.get("generator?theme=" + $(".generator-select option:selected").val(), function(data) { // Обработка (get-запрос на сервер)
        $(".create-idea").html(data.replace("+", " ")); // Изменения кнопки текста
    });
}