{
    'name' : 'School',
    'summary': """Manage Students""",

    'description': """
        Open Academy module for managing students
    """,

    'author': "Tanvir",
    'website': "http://www.BayIT.co",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        #'views/openacademy_course.xml',
        #'views/openacademy_session.xml',
        'views/school_student.xml',
        'views/inherited_course_views.xml',
        'views/inherited_session_views.xml',
    ],
}