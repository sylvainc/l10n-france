# -*- encoding: utf-8 -*-
##############################################################################
#
#    l10n FR Departments module for OpenERP
#    Copyright (C) 2013-2014 GRAP (http://www.grap.coop)
#    @author Sylvain LE GAL (https://twitter.com/legalsylvain)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import fields
from openerp.osv.orm import Model
from openerp.tools.translate import _


class res_country_department(Model):
    _description = "Department"
    _name = 'res.country.department'
    _order = 'country_id, code'

    def _get_dpt_from_state(self, cr, uid, ids, context=None):
        return self.pool['res.country.department'].search(
            cr, uid, [('state_id', 'in', ids)], context=context)

    _columns = {
        'state_id': fields.many2one(
            'res.country.state', 'State', required=True,
            help='State related to the current department'),
        'country_id': fields.related(
            'state_id', 'country_id', type='many2one',
            relation='res.country', string='Country', readonly=True,
            store={
                'res.country.state': (_get_dpt_from_state, ['country_id'], 10),
                }, help='Country of the related state'),
        'name': fields.char('Department Name', size=128, required=True),
        'code': fields.char(
            'Departement Code', size=2, required=True,
            help="""The department code in two chars."""
            """(ISO 3166-2 Codification)"""),
    }

    _sql_constraints = [
        ('code_uniq', 'unique (code)',
            _("""You cannot have two departments with the same code!""")),
    ]
