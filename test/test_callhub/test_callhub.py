from parsons.callhub.callhub import CallHub
import unittest
import requests_mock
from test_callhub_data import fake_contacts_data


class TestCallHub(unittest.TestCase):
    def setUp(self):
        self.ch = CallHub("mykey")

    @requests_mock.Mocker()
    def test_get_contacts(self, m):
        # Test that contacts are returned correctly.
        m.get(requests_mock.ANY, json=fake_contacts_data)
        tbl = self.ch.get_contacts()

        self.assertEqual(tbl.num_rows, 10)
