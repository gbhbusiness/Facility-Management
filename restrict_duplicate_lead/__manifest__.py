# See LICENSE file for full copyright and licensing details.

{
    'name': 'Restrict Duplicate Lead',
    'version': '13.0.1.0.0',
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'description': 'Restricts Duplicate Leads',
    'category': 'CRM',
    'license': "AGPL-3",
    'summary': 'A Module To Restrict Duplicate CRM Lead',
    'depends': ['crm'],
    'data': [
        'wizard/crm_wiz_view.xml',
        'views/crm_lead_view.xml',
    ],
    'installable': True,
}
