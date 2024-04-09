#!/usr/bin/env python3
"""Test client unitest"""
import unittest
from typing import Dict
from unittest.mock import (
    MagicMock,
    Mock,
    patch,
)
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test GithubOrgClient"""

    @parameterized.expand([
        ("google", {'test': "google"}),
        ("abc", {'test': "abc"}),
    ])
    @patch(
        "client.get_json",
    )
    def test_org(self, org: str, expected_response: Dict,
                 mock_fn: MagicMock) -> None:
        """test client.get_json"""

        mock_fn.return_value = expected_response
        client = GithubOrgClient(org)
        org_response = client.org()
        self.assertEqual(org_response, expected_response)
        mock_fn.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(org)
        )

    def test_public_repos_url(self) -> None:
        """Mock the org method to return a known payload"""

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock,
        ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )
