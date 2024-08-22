from gnocchiclient import auth
from gnocchiclient.v1 import client
from oslo_log import log

LOG = log.getLogger(__name__)

# pprint.pp(list(metric_ids))
# Метрики ресурса
#pprint.pp(gnocchi.resource.get(resource_id='ffefe222-85c5-5785-b35f-1fe0bded73b0', resource_type='generic'))

class GnocchiClient:
    def __init__(self, conf):
        self.endpoint = conf.CONF.gnocchi_client.endpoint
        self.metrics = conf.CONF.ai.metrics
        auth_plugin = auth.GnocchiBasicPlugin(user="admin", endpoint=self.endpoint)
        
        self.client = client.Client(session_options={'auth': auth_plugin})
        self.conf = conf

