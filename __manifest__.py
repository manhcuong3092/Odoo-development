{
    'name': "Hospital Manager",
    'summary': """Hospital Manager""",
    'description': """test odoo""",
    'sequence': "-10",
    'author': "Dung",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': [
        'sale',
        'mail',
        'website_slides',
        'hr',
    ],
    'data': [
        "security/ir.model.access.csv",
        "views/patient.xml",
        "views/sale.xml"
    ],
    # 'qweb': ['static/src/xml/*.xml'],
    'installable': True,
    'application': True,
}
