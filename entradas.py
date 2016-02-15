# -*- coding: utf-8 -*-
#################################################################################
#
#    OpenERP, Open Source Management Solution
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#################################################################################
from openerp import fields, models

class espectaculo(models.Model):    
	_name = 'espectaculo'
	_inherit = 'calendar.event'

	localizacion = fields.Many2one('localizacion', 'Localizacion')
       
espectaculo()

class localizacion(models.Model):
	_name = 'localizacion'
	_inherit = 'contact_address'

	aforo = fields.Integer('Aforo')
localizacion()

class entrada(Models.model):
	_inherit = 'product'

	espectaculo = fields.Many2one('espectaculo', 'Espectáculo')
entrada()

class cliente(models.Model):
	_name = 'cliente'
	_inherit = 'res.partner'

	entradas = fields.Many2many('entrada', string = 'Entradas')
cliente()

