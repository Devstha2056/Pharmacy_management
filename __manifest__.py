{
    'name': 'Pharmacy Management',
    'version': "18.0.1.0.0",
    'category': 'Hospital',
    'sequence': -100,
    'author': 'Devendra Kumar Shrestha',
    'summary': 'Used for Pharmacy',
    'description': """
        This module provides Fully feature pharmacy management system for clients and pharmacist to order,
        deliverd and track the order record.
    """,
    'depends': ['base','contacts','mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data_view.xml',
        'views/pharmacy_view.xml',

        'views/menu_view.xml',

    ],
    'assets': {

    },
    'demo': [],
    'application': True,
    'installable': True,
    'auto_install': False,
    'license': 'LGPL-3',
}
