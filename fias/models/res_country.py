# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models

class CountryState(models.Model):

    _name = 'res.country.state'
    _inherit = ['res.country.state', 'fias.fields.mixin']


class StateDistricts(models.Model):

    _name = 'res.state.district'
    _inherit = 'fias.fields.mixin'
    _description = "State district"
    _order = 'name'


    state_id = fields.Many2one('res.country.state', string='State', required=True)
    name = fields.Char(string='Name', required=True)
    #city_ids = fields.One2many('res.city', 'district_id', string='City')

    _sql_constraints = [
        ('name_code_uniq', 'unique(state_id, name)', 'The area should be unique for the region!')
    ]


class City(models.Model):

    _name = 'res.city'
    _inherit = ['res.city', 'fias.fields.mixin']
