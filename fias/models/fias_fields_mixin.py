# Copyright 2020 Eugene Molotov <https://it-projects.info/team/em230418>
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl.html).

from odoo import api, fields, models


class FiasFieldsMixin(models.AbstractModel):

    _name = 'fias.fields.mixin'
    _description = 'Поля для записей из ФИАС'

    fias_aoguid = fields.Char('Глобальный уникальный идентификатор адресного объекта', readonly=True)
    fias_okato = fields.Char('ОКАТО', readonly=True)
    fias_oktmo = fields.Char('ОКТМО', readonly=True)
