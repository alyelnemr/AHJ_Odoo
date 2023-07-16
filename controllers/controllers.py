# -*- coding: utf-8 -*-
# from odoo import http


# class AlyAhjOdoo(http.Controller):
#     @http.route('/aly_ahj_odoo/aly_ahj_odoo', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/aly_ahj_odoo/aly_ahj_odoo/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('aly_ahj_odoo.listing', {
#             'root': '/aly_ahj_odoo/aly_ahj_odoo',
#             'objects': http.request.env['aly_ahj_odoo.aly_ahj_odoo'].search([]),
#         })

#     @http.route('/aly_ahj_odoo/aly_ahj_odoo/objects/<model("aly_ahj_odoo.aly_ahj_odoo"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('aly_ahj_odoo.object', {
#             'object': obj
#         })

