from django.test import TestCase, override_settings
from app.ciscoeox.base_api import CiscoEoxApi
from app.config.utils import test_cisco_eox_api_access, test_cisco_hello_api_access


@override_settings(APP_CONFIG_FILE="conf/product_database.cisco_api_test.config")
class TestConfigUtility(TestCase):
    """
    test the Cisco EoX API classes
    """
    fixtures = ['default_vendors.yaml']

    def test_cisco_hellp_api_access(self):
        eox_call = CiscoEoxApi()
        eox_call.load_client_credentials()

        self.assertTrue(test_cisco_hello_api_access(eox_call.client_id, eox_call.client_secret, drop_credentials=False))

    def test_cisco_eox_api_access(self):
        eox_call = CiscoEoxApi()
        eox_call.load_client_credentials()

        self.assertTrue(test_cisco_eox_api_access(eox_call.client_id, eox_call.client_secret, drop_credentials=False))
