# -*- coding: utf-8 -*-
{
    'name': 'Real Estate',
    'category' : 'Sales',
    'application' : True,
    #'depends' : ['base','estate','account'],
    'data' : [
    	'security/access_security.xml',
    	'security/ir.model.access.csv',
    	'views/estate_menus.xml',
        'wizard/create_sold_invoice_views.xml',
        'wizard/confirm_accept_view.xml',
    	'views/estate_property_views.xml',
        'report/property_report.xml',
        'report/property_detail.xml',
    ],
}
	

