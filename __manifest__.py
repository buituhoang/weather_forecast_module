# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Weather Forecast',
    'version' : '0.1',
    'summary': 'Weather Forecast',
    'sequence': -10,
    'description': """Weather Forecast""",
    'category': 'Productivity',
    'website': 'https://www.abcxyz.com/',
    'license': 'LGPL-3',
    'depends': ['website', 'base'],
    'data': [
        'views/date.xml',
        'views/templates.xml',
        'security/ir.model.access.csv',
        'data/cron.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
