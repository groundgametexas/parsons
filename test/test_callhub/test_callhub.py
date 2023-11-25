from parsons.callhub.callhub import CallHub
import unittest
import requests_mock
from test_callhub_data import fake_contacts_data

# TODO: This test seems to be hitting a sandbox API. We should mock the API response instead.


class TestCallHub(unittest.TestCase):
    def setUp(self):
        self.ch = CallHub(api_key="test1234")

    @requests_mock.Mocker()
    def test_get_contacts(self, m):
        # Test that contacts are returned correctly.
        m.get("https://api.callhub.io/v1/contacts/", json=fake_contacts_data)

        tbl = self.ch.get_contacts()

        self.assertEqual(tbl.num_rows, 10)
