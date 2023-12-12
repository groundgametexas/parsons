import unittest
import requests_mock
from parsons.legiscan.legiscan import Legiscan


class TestLegiscan(unittest.TestCase):
    def setUp(self):
        self.api_key = "YOUR_API_KEY"
        self.legiscan = Legiscan(api_key=self.api_key)

    @requests_mock.Mocker()
    def test_get_session_list(self, m):
        expected_response = {
            "sessions": [{"session_id": 1, "session_name": "Session 1"}]
        }
        m.get(
            f"http://api.legiscan.com/?key={self.api_key}&op=getSessionList",
            json=expected_response,
        )
        response = self.legiscan.get_session_list()
        self.assertEqual(response, expected_response)

    def test_get_session_list_tbl(self):
        expected_response = {
            "sessions": [{"session_id": 1, "session_name": "Session 1"}]
        }
        with requests_mock.Mocker() as m:
            m.get(
                f"http://api.legiscan.com/?key={self.api_key}&op=getSessionList",
                json=expected_response,
            )
            table = self.legiscan.get_session_list_tbl()
            self.assertEqual(len(table), 1)
            self.assertEqual(table[0]["session_id"], 1)
            self.assertEqual(table[0]["session_name"], "Session 1")

    # Add more test methods for other methods in the Legiscan class


if __name__ == "__main__":
    unittest.main()
