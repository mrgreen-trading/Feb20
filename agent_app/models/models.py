# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class my_module(models.Model):
#     _name = 'my_module.my_module'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class AgentModel(models.Model):
    _name = 'agent_app.agentmodel'
    _description = "Agents database model"

    name = fields.Char(required=True)
    phone = fields.Char()
    location = fields.Char()
    city_id = fields.Integer()
    town_id = fields.Integer()
    mpesa = fields.Boolean()
    completed = fields.Boolean()
    direction = fields.Char()
    latitude = fields.Char()
    longitude = fields.Char()
    archive = fields.Boolean()
    active = fields.Boolean()
    deleted_at = fields.Datetime()
    email = fields.Boolean()
    organized = fields.Boolean()
    kind = fields.Char()
    balance = fields.Monetary(compute='_compute_balance')

    
    def _compute_balance(self, amount,status):
        for record in self:
            if status == 'delivered':
                record.balance +=  amount
            else:
                record.balance -= amount
    