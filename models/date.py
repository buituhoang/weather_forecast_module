from odoo import api, models, fields, _
from odoo.exceptions import UserError, ValidationError

class WeatherForecastDate(models.Model):
    _name = "weather.forecast.date"
    _description = "Weather Forecast Date"
    _rec_name = "date"

    @api.constrains('date')
    def _check_date(self):
        date = self.env['weather.forecast.date'].search([('date', '=', self.date), ('id', '!=', self.id)])
        if date:
            raise ValidationError(_('Record of this day already existed.'))

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
    ], default='sun', string="Weather Icon")
    weather = fields.Char(string='Weather')
    humidity = fields.Integer(string='Humidity')
    high_temp = fields.Integer(string='Highest Temperature')
    low_temp = fields.Integer(string='Lowest Temperature')
    wind_speed = fields.Float(string='Wind Speed')
