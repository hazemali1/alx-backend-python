#!/usr/bin/env python3
"""testing module for client"""
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
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
