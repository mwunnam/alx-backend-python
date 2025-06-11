#!/usr/bin/env python3
""" Test for the clinet models"""

import unittest
from unittest.mock import patch, MagicMock, PropertyMock
from client import GithubOrgClient
from fixtures import org_payload, repos_payload, expected_repos, apache2_repos
from parameterized import parameterized
import requests


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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """ Test case to mock get_json and _public_repos_url
            method using patch context manager
        """
        test_payload = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]
        mock_get_json.return_value = test_payload

        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_url:
            mock_url.return_value = "https://api.github.com/google/repo"

            client = GithubOrgClient("google")
            result = client.public_repos()

            self.assertEqual(result, ["repo1", "repo2", "repo3"])
            mock_url.assert_called_once()
            mock_get_json.assert_called_once_with(
                "https://api.github.com/google/repo"
            )

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """
        Test case for has_license returns True or false
        """
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos,
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up patcher for requests.get"""
        cls.get_patcher = patch("requests.get")

        # Start the patcher and save the mock
        cls.mock_get = cls.get_patcher.start()

        # Side effect list matches order of requests: org -> repos
        cls.mock_get.side_effect = [
            unittest.mock.Mock(**{"json.return_value": cls.org_payload}),
            unittest.mock.Mock(**{"json.return_value": cls.repos_payload}),
        ]

    @classmethod
    def tearDownClass(cls):
        """Stop the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test the public_repos method without a license filter"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos with filtering by license"""
        client = GithubOrgClient("google")
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )


if __name__ == "__main__":
    unittest.main()
