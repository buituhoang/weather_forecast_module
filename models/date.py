from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError
import requests
from bs4 import BeautifulSoup
from odoo.http import request
import datetime


class WeatherForecastDate(models.Model):
    _name = "weather.forecast.date"
    _description = "Weather Forecast Date"
    _rec_name = "date"

    # This function is currently cannot work due to timeout
    def update_weather_data(self):
        try:
            file = requests.get('https://weather.com/en-GB/weather/tenday/l/21.00,105.84')
            soup = BeautifulSoup(file.text, 'html.parser')
            list = []
            content = soup.find_all("div", {"data-testid": "DetailsSummary"})
            for items in content:
                dict = {}
                day = items.find_all("span")
                try:
                    dict["high_temp"] = int(day[0].text.split('°')[0])
                    dict["low_temp"] = int(day[2].text.split('°')[0])
                    dict["weather"] = day[3].text.split('/')[0].replace('AM ', '')
                    dict["humidity"] = int(day[4].text.split('%')[0])
                    dict["wind_speed"] = round(int(day[5].text.split(' ')[1]) * 1.609344, 1)
                except:
                    dict["high_temp"] = ""
                    dict["low_temp"] = ""
                    dict["weather"] = "None"
                    dict["humidity"] = ""
                    dict["wind_speed"] = ""
                list.append(dict)
            date = datetime.date.today()
            for i in range(9):
                list[i]['date'] = date
                date_info = request.env['weather.forecast.date'].sudo().search([('date', '=', date)], limit=1)
                if date_info:
                    date_info.sudo().write(list[i])
                    print(date_info)
                else:
                    new_date_info = request.env['weather.forecast.date'].sudo().create({'date': date})
                    new_date_info.sudo().write(list[i])
                    print(new_date_info)
                date += datetime.timedelta(days=1)
            print("Data updated")
        except:
            print("Error")

    @api.constrains('date')
    def _check_date(self):
        date = self.env['weather.forecast.date'].search([('date', '=', self.date), ('id', '!=', self.id)])
        if date:
            raise ValidationError(_('Record of this day already existed.'))

    @api.depends('weather')
    def _choose_icon(self):
        for rec in self:
            if 'Cloud' in rec.weather:
                rec.weather_icon = 'cloud'
            elif 'Storm'in rec.weather or 'storm' in rec.weather:
                rec.weather_icon = 'storm'
            elif 'Rain' in rec.weather or 'Shower' in rec.weather:
                rec.weather_icon = 'rain'
            else:
                rec.weather_icon = 'sun'

    @api.depends('date')
    def _get_day(self):
        for rec in self:
            if rec.date.weekday() == 0:
                rec.day = 'mon'
            elif rec.date.weekday() == 1:
                rec.day = 'tue'
            elif rec.date.weekday() == 2:
                rec.day = 'wed'
            elif rec.date.weekday() == 3:
                rec.day = 'thu'
            elif rec.date.weekday() == 4:
                rec.day = 'fri'
            elif rec.date.weekday() == 5:
                rec.day = 'sat'
            else:
                rec.day = 'sun'

    date = fields.Date(string='Date', required=True, copy=False)
    day = fields.Selection([
        ('mon', 'Monday'),
        ('tue', 'Tuesday'),
        ('wed', 'Wednesday'),
        ('thu', 'Thursday'),
        ('fri', 'Friday'),
        ('sat', 'Saturday'),
        ('sun', 'Sunday'),
    ], default='mon', compute='_get_day', readonly=True)
    weather_icon = fields.Selection([
        ('rain', 'Rainy'),
        ('sun', 'Sunny'),
        ('cloud', 'Cloudy'),
        ('storm', 'Storm'),
    ], default='sun', string="Weather Icon", compute='_choose_icon')
    weather = fields.Char(string='Weather')
    humidity = fields.Integer(string='Humidity (%)')
    high_temp = fields.Integer(string='Highest Temperature(°C)')
    low_temp = fields.Integer(string='Lowest Temperature(°C)')
    wind_speed = fields.Float(string='Wind Speed (kmh)')
