# -*- coding: utf-8 -*-
{
    'name': "ODOO12班级管理系统",

    'summary': """
        再学习ODOO12，复习重点内容和不清楚的地方""",

    'description': """
        Long description of module's purpose
    """,

    'author': "moonrong",
    'website': "http://www.haopython.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'demo/demo.xml',
        'views/odoogoedu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'sequence': 4,
}