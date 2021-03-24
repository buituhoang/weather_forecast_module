odoo.define('weather_forecast.Create_table', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');
    var button_1_day = document.getElementById("get_weather_one_day")
    var button_3_day = document.getElementById("get_weather_three_days")
    var button_7_day = document.getElementById("get_weather_week")

    function get_json(count) {
        var ajax = require('web.ajax');
        ajax.jsonRpc("http://localhost:8069/get_weather/" + count, "call").then(function (data) {
            var output = data["content"]
            var temp_table = document.getElementById("temp_table")
            if (count == "1") {
                button_1_day.className = "btn btn-primary"
                button_3_day.className = "btn btn-secondary"
                button_7_day.className = "btn btn-secondary"
            } else if (count == "3") {
                button_1_day.className = "btn btn-secondary"
                button_3_day.className = "btn btn-primary"
                button_7_day.className = "btn btn-secondary"
            } else {
                button_1_day.className = "btn btn-secondary"
                button_3_day.className = "btn btn-secondary"
                button_7_day.className = "btn btn-primary"
            }
            var img = ""
            // var day = ""
            var table = "";
            for (var i = 0; i < output.length; i++) {
                if (output[i]["weather_icon"] == "sun")
                    img = '<img src="/weather_forecast/static/src/img/sunny.png" className="img" style="max-width: 40mm; max-height: 20mm;"/>'
                else if (output[i]["weather_icon"] == "rain")
                    img = '<img src="/weather_forecast/static/src/img/rainy.png" className="img" style="max-width: 40mm; max-height: 20mm;"/>'
                else if (output[i]["weather_icon"] == "storm")
                    img = '<img src="/weather_forecast/static/src/img/storm.png" className="img" style="max-width: 40mm; max-height: 20mm;"/>'
                else
                    img = '<img src="/weather_forecast/static/src/img/cloudy.png" className="img" style="max-width: 40mm; max-height: 20mm;"/>'

                table += '<table class="tg table-bordered table-striped table-sm" \n' +
                    'style="width: 30%; margin-top: 2vh; margin-bottom: 2vh" ' +
                    'align="center"><tr><td rowSpan="2" align="center">' +
                    img +
                    '</td><td><strong>' +
                    output[i]["day"] +
                    '</strong></td></tr><tr><td><span>' +
                    output[i]["date"] +
                    '</span></td></tr>' +
                    '<tr><td colSpan="2" align="center"><span>' +
                    output[i]["weather"] +
                    '</span></td></tr><tr><td>Wind speed: <span>' +
                    output[i]["wind_speed"] +
                    '<span/>km/h</td><td>Highest temperature: <span>' +
                    output[i]["high_temp"] +
                    '<span/>°C</td></tr><tr><td>Chance of Rain: <span>' +
                    output[i]["rain_chance"] +
                    '<span/>%</td><td>Lowest temperature: <span>' +
                    output[i]["low_temp"] +
                    '<span/>°C</td></tr>'
                '</table>'
            }
            if (temp_table) temp_table.remove()
            document.getElementById("test_ajax_table").innerHTML = table
        })
    }

    publicWidget.registry.GetWeatherToday = publicWidget.Widget.extend({
        selector: '#get_weather_one_day',
        events: {
            click: '_onClick'
        },
        async _onClick(e) {
            e.preventDefault();
            await get_json("1")
        }
    });

    publicWidget.registry.GetWeatherThreeDays = publicWidget.Widget.extend({
        selector: '#get_weather_three_days',
        events: {
            click: '_onClick'
        },
        async _onClick(e) {
            e.preventDefault();
            await get_json("3")
        }
    });

    publicWidget.registry.GetWeatherWeek = publicWidget.Widget.extend({
        selector: '#get_weather_week',
        events: {
            click: '_onClick'
        },
        async _onClick(e) {
            e.preventDefault();
            await get_json("7")
        }
    });
});





