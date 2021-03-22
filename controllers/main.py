from odoo import http
from odoo.http import request
from . import data_scrapping
import json
import datetime

class Hospital(http.Controller):
    @http.route('/weather_forecast_<num>', type="http", auth="public", website=True)
    def weather_forecast(self, num, **kw):
        dates_list = http.request.env['weather.forecast.date']
        today = datetime.date.today()
        three_day = today + datetime.timedelta(days=2)
        week = today + datetime.timedelta(days=6)
        if num == '1':
            return http.request.render('weather_forecast.dates_weather', {'dates': dates_list.search([('date', '=', today)]), 'count':1})
        elif num == '3':
            return http.request.render('weather_forecast.dates_weather', {'dates': dates_list.search([('date', '>=', today), ('date', '<=', three_day)]), 'count':3})
        else:
            return http.request.render('weather_forecast.dates_weather', {'dates': dates_list.search([('date', '>=', today), ('date', '<=', week)]), 'count':7})

    @http.route('/update_weather', type="http", auth="public", website=True)
    def update_weather(self):
        obj = data_scrapping.data_scrapping()
        obj.get_weather()
        data = obj.data
        date = datetime.date.today()
        if data:
            for i in range(9):
                data[i]['date'] = date
                date_info = request.env['weather.forecast.date'].sudo().search([('date', '=', date)], limit=1)
                if date_info:
                    date_info.sudo().write(data[i])
                    print(date_info)
                else:
                    new_date_info = request.env['weather.forecast.date'].sudo().create({'date': date})
                    new_date_info.sudo().write(data[i])
                    print(new_date_info)
                date += datetime.timedelta(days=1)
        dates_list = http.request.env['weather.forecast.date']
        today = datetime.date.today()
        return request.render('weather_forecast.dates_weather',
                                   {'dates': dates_list.search([('date', '=', today)]), 'count': 1})



