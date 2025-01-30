{'name': 'Odoo Sale Secondary UOM',
'version': '17.0.0.1',
'sequence': 1,
'category': 'Extra Tools',
'author': 'Keypress IT Services',
'website': 'https://staging.keypress.co.in',
'summary': 'Easily display sales order quantities in an alternative unit of measurement.',
'depends': ['sale_management', 'kits_product_secondary_units'],
'data': ['views/sale_order_view.xml', 'reports/kits_sale_report_inherit.xml'],
'application': True,
'installable': True,
'auto-install': False,
'live_test_url': 'https://staging.keypress.co.in/odoo-apps/17.0/reports-custom-font',
'images': ['static/description/banner.png'],
'price': 20,
'currency': 'INR',
'description': 'Enhance your sales order management with Odoo Sale Secondary UOM. Display product quantities in an alternative unit of measurement alongside the primary unit for improved visibility and accuracy.',
'maintainer': 'Keypress IT Services',
'auto_install': False,
'license': 'OPL-1',}