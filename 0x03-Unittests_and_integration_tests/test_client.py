#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from client import GithubOrgClient
from parameterized import parameterized

class TestGithubOrgClient(unittest.TestCase):
    """
    Parameterize and patch as decorators using
    GithubOrgClient from the client module
    """
    @parameterized.expand([
        ("google", {"login": "google", "id": 1}),
        ("abc", {"login": "abc", "id": 2}),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, expected_payload, mock_get_json):
        """
            Test case for org mocking to see how it performs
        """
        mock_get_json.return_value = expected_payload

        client = GithubOrgClient(org_name)
        result = client.org

        self.assertEqual(result, expected_payload)
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos(self):
        """Testing theat  _pulic_repos_url retuns
            the correct URL
        """
        payload = {"repos_url": "https://api.github.com/orgs/google/repos"}

        with patch.object(GithubOrgClient, 'org', return_value=payload):
            client = GithubOrgClient('google')
            result = client._public_repos_url

            self.assertEqual(result, payload["repos_url"])


if __name__ == "__main__":
    unittest.main()
