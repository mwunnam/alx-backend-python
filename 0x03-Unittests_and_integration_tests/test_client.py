import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """
    Parameterize and patch as decorators using GithubOrgClient from the client module
    """
    @parameterized.expand([
        ("google", ),
        ("abc", ) ,
    ])

    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """
            Test case for org mocking to see how it performs         
        """
        expected_payload = {"key": "value"}
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org()
        self.assertEqual(result, expected_payload)

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")