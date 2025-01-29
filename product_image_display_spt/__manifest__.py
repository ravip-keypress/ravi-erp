{'name': 'Odoo All In One Product Image Display',
'version': '17.0.0.4',
'summary': 'Display product quantities in an alternative unit of measure across products, sale orders, deliveries, purchase orders, and invoices.',
'sequence': 1,
'images': ['static/description/youtubebanner.png'],
'price': 100,
'currency': 'USD',
'author': 'Keypress IT Services',
'description': 'Transform your inventory management with Odoo All-in-One Unit of Measure. Display product quantities in both primary and secondary units across products, sales, deliveries, purchases, and invoices for improved accuracy and clarity.',
'website': 'https://staging.keypress.co.in',
'depends': ['base', 'sale', 'stock', 'delivery', 'purchase'],
'data': ['security/ir.model.access.csv', 'views/sale_order_view.xml', 'views/purchase_order_view.xml', 'views/stock_picking_view.xml', 'reports/sale_order_extend_report.xml', 'reports/purchase_quotation_extend_report.xml', 'reports/purchase_order_extend_report.xml', 'reports/product_report_action.xml', 'reports/product_template_report_template_spt.xml', 'reports/product_product_report_template_spt.xml', 'reports/stock_picking_extend.xml', 'reports/delivery_slip_report_extend.xml'],
'application': True,
'auto_install': False,
'live_test_url': 'https://www.youtube.com/watch?v=toaYVTNaSF4',
'maintainer': 'Keypress IT Services',
'installable': True,
'license': 'OPL-1',
'category': 'Extra Tools',}