{
    'name': "services extension",
    'version': '1.0',
    'depends': ['base'],
    'summary': """ Test task """,
    'author': "My company",
    'category': 'Category',
    'description': """
    Test task
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/services_view.xml',
        'views/res_partner_inh.xml',
        'views/device_view.xml',
        'reports/device_report_t.xml',
        'wizards/report_wizard_view.xml',

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
