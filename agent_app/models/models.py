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
    ussd_id = fields.Char()
    phone = fields.Char()
    location = fields.Char()
    city_id = fields.Char()
    area = fields.Char()
    town_id = fields.Char()
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
    balance = fields.Float()
    partner_id = fields.Many2one('res.partner', string="Partner")

    @api.model
    def _compute_balance(self, amount,status):
        for record in self:
            if status == 'delivered':
                record.balance +=  amount
            else:
                record.balance -= amount
    
class AgentType(models.Model):
    _name = 'agentapp.agenttype'
    _description = 'Agent type database'
    
    name = fields.Char(required=True)
    kind = fields.Char()
    active = fields.Boolean()
    
class Location(models.Model):
    _name = 'agentapp.location'
    _description = 'Location model for MGA Payment Hub Module'
    
    name = fields.Char(required=True)
    tradingpoint = fields.One2many('agentapp_tradingpoint','city')
    active = fields.Boolean()

class TradingPoint(models.Model):
    _name = 'agentapp.tradingpoint'
    _description = 'Trading point model for MGA Payment Hub'
    
    city = fields.Many2one('agentapp_location',
        ondelete='cascade', string="City", required=True)
    name = fields.Char(required=True)
    active = fields.Boolean()
    
    
    
