# -*- coding: utf-8 -*-

{
    'name': 'Custom Module',
    'category': 'Hidden',
    'summary': 'Module customisation',
    'version': '1.0',
    'description': """Customisation in Existing Module.....""",
    'author': 'Logicious',
    'website': 'http://logicious.net',
    'depends': ['base','product','stock','mrp'],
    'data': [
        'wizard/mrp_product_produce_view.xml',
        'product_view.xml',
        'mrp_view.xml',
#        'stock_view.xml',
        'product_data.xml',


    ],
    'installable': True,
}
