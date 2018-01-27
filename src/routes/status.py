import http.client
from http.client import OK
import logging
from flask_restplus import Namespace, Resource, fields
import socket

logger = logging.getLogger(__name__)

statusNamespace = 'status'
api = Namespace(statusNamespace, description='Status')

status = api.model('Status', {
    'status': fields.String(required=True, readOnly=True, description='The status of the server'),
    'ip': fields.String(required=True, readOnly=True, description='The ip of the server'),
})


# source: https://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib
def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        # doesn't even have to be reachable
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
        logger.debug("Retrieved server ip: " + IP)
    except:
        IP = '127.0.0.1'
        logger.warn("Could not get server ip; will default to " + IP)
    finally:
        s.close()
    return IP

@api.route('/')
class Status(Resource):
    '''
    Return the server status.
    '''
    @api.doc('get_status')
    @api.marshal_with(status)
    def get(self):
        ip = get_ip()
        return {'status': http.client.responses[OK], 'ip': ip}