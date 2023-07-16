# -*- coding: utf-8 -*-
{
    'name': "Andalusia Hospital Jeddah",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Aly El Nemr",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Medical',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'product'],

    # always loaded
    'data': [
        'views/oasis_patients.xml',
        'views/oasis_doctors.xml',
        'views/oasis_rooms.xml',
        'views/oasis_work_entities.xml',
        'views/patient_episodes.xml',
        'views/drug_route.xml',
        'views/patient_prescriptions.xml',
        'views/product.xml',
        'views/views.xml',
        'security/ir.model.access.csv',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "installable": True,
    "application": True,
}
