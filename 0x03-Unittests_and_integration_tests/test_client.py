#!/usr/bin/env python3
"""testing module for client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test for client"""
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch("client.get_json")
    def test_org(self, name, mock):
        """test for org"""
        m = Mock()
        org = {"login": name}
        m.return_value = org
        mock.return_value = m
        obj = GithubOrgClient(name)
        self.assertEqual(obj.org(), org)
        mock.assert_called_once_with(
            "https://api.github.com/orgs/{}".format(name)
        )

    def test_public_repos_url(self):
        """test for public repositories"""
        with patch("client.GithubOrgClient.org",
                   new_callable=PropertyMock) as m:
            url = "https://api.github.com/users/hazemali1/repos"
            m.return_value['repos_url'] = url
            obj = GithubOrgClient("hazemali1")
            self.assertEqual(obj._public_repos_url,
                             m.return_value['repos_url'])

    @patch("client.get_json")
    def test_public_repos(self, mock):
        """test for public repo"""
        with patch("client.GithubOrgClient._public_repos_url",
                   new_callable=PropertyMock) as m:
            url = "https://api.github.com/users/hazemali1/repos"
            m.return_value['repos_url'] = url
            obj = GithubOrgClient("hazemali1")
            self.assertEqual(obj.public_repos(),
                             [])
            m.assert_called_once()
        mock.assert_called_once()
