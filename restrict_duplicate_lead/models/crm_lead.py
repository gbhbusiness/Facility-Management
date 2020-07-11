# See LICENSE file for full copyright and licensing details.

from odoo import models


class CrmLead(models.Model):

    _inherit = "crm.lead"

    def check_lead(self):
        """Check lead or partner if it is duplicating."""
        for rec in self:
            existing_lead_list = []
            existing_partner_list = []
            if rec.mobile:

                existing_partner = self.env['res.partner'].search([
                    ('mobile', '=', rec.mobile),
                ])
                existing_lead = self.env['crm.lead'].search([
                    ('mobile', '=', rec.mobile),
                    ('id', '!=', rec.id),
                ])
                for lead in existing_lead:
                    existing_lead_list.append(lead)
                for partner in existing_partner:
                    existing_partner_list.append(partner.id)
            if rec.phone:
                existing_partner = self.env['res.partner'].search([
                    ('phone', '=', rec.phone),
                ])
                existing_lead = self.env['crm.lead'].search([
                    ('phone', '=', rec.phone),
                    ('id', '!=', rec.id),
                ])
                for lead in existing_lead:
                    existing_lead_list.append(lead)
                for partner in existing_partner:
                    existing_partner_list.append(partner.id)
            if rec.email_from:
                existing_partner = self.env['res.partner'].search([
                    ('email', '=', rec.email_from),
                ])
                existing_lead = self.env['crm.lead'].search([
                    ('email_from', '=', rec.email_from),
                    ('id', '!=', rec.id),
                ])
                for lead in existing_lead:
                    existing_lead_list.append(lead)
                for partner in existing_partner:
                    existing_partner_list.append(partner.id)
            action = {
                'name': ('CRM Lead Wizard'),
                'view_type': 'form',
                'view_mode': 'form',
                'res_model': 'crm.lead.wizard',
                'type': 'ir.actions.act_window',
                'target': 'new'}
            if existing_partner_list:
                action.update({
                    'context': {
                        'default_partner_id': existing_partner_list[0]}})
                return action
            elif existing_lead_list:
                action.update(
                    {'context': {'default_lead_id': existing_lead_list[0].id}})
                return action
            else:
                action.update({
                    'context': {'default_note': "You do not have duplicate \
record with this data"}})
            return action
