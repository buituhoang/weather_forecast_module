odoo.define('hospital.FrameworkSample', function (required) {
    "use strict";
    function initCss(e) {
        var style_css = document.createElement("link");

        style_css.setAttribute("rel", "stylesheet"),
        style_css.setAttribute("type", "text/css"),
        style_css.onload = e,
        style_css.setAttribute("href", "/om_hospital/static/src/css/my.css"),
        document.head.appendChild(style_css);
    }
    function initJs(e) {
        var js_src = document.createElement("script");

        js_src.setAttribute("type", "text/javascript"),
        js_src.onload = e,
        js_src.setAttribute("src", "/om_hospital/static/src/js/another_js.js"),
        document.head.appendChild(js_src);
    }
});

