import logging
import json

from odoo import http
from odoo.http import Response, request
from odoo.addons.rest_api.controllers.main import check_permissions, rest_cors_value, successful_response, error_response


_logger = logging.getLogger(__name__)


class Prosody(http.Controller):
    @http.route('/api/chat/channel', methods=['GET'], type='http', auth='none', csrf=False, cors=rest_cors_value)
    @check_permissions
    def api_search_channel(self, **kwargs):
        _logger.warning("Incoming data %s", kwargs)
        cr, uid = request.cr, request.session.uid
        if kwargs:
            channel_id = request.env(cr, uid)['mail.channel'].sudo().search_partner_channels(kwargs)
            _logger.warning("searched channel %s", channel_id)
            dict_data = {'channel_id': channel_id}
            return successful_response(status=200, dict_data=dict_data)
        return error_response(400, 'Bad Request', 'Some parameters are missing')

    @http.route('/api/chat', methods=['POST'], type='http', auth='none', csrf=False, cors=rest_cors_value)
    @check_permissions
    def api_chat(self, **kwargs):
        _logger.warning("Incoming data %s", kwargs)
        cr, uid = request.cr, request.session.uid
        if kwargs:
            channel_message = request.env(cr, uid)['mail.channel'].sudo().message_channel_post_chat(kwargs)
            _logger.warning("channel_message result =  %s", channel_message)
            dict_data = {'channel_message': channel_message}
            return successful_response(status=200, dict_data=dict_data)
        return error_response(400, 'Bad Request', 'Some parameters are missing')
