odoo.define('weather_forecast.Weather_forecast', function (required) {
    "use strict";
    // function initCss(e) {
        // var style_css = document.createElement("link");
        //
        // style_css.setAttribute("rel", "stylesheet"),
        // style_css.setAttribute("type", "text/css"),
        // style_css.onload = e,
        // style_css.setAttribute("href", "/om_hospital/static/src/css/my.css"),
        // document.head.appendChild(style_css);
    // }
    function initJs(e) {
        var js_src = document.createElement("script");

        js_src.setAttribute("type", "text/javascript"),
        js_src.onload = e,
        js_src.setAttribute("src", "/weather_forecast/static/src/js/create_table.js"),
        document.head.appendChild(js_src);
    }
    initJs()
});

