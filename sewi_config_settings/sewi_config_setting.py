from openerp import models, fields, api, _


class sewisoft_config_settings(models.TransientModel):

    _name = "sewisoft.config.settings"

    _description = 'Sewisoft Addons Configuration'
    _inherit = 'res.config.settings'

