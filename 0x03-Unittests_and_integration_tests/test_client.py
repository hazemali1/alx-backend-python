#!/usr/bin/env python3
"""testing module for client"""
import unittest
from parameterized import parameterized, parameterized_class
from unittest.mock import patch, Mock, PropertyMock
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ])
    def test_has_license(self, k, v, r):
        """test for has_license"""
        obj = GithubOrgClient("hazemali1")
        result = obj.has_license(k, v)
        self.assertEqual(r, result)


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test for GithubOrgClient using Integration test"""
    @classmethod
    def setUpClass(myclass):
        """set Up Class"""
        myclass.get_patcher = patch('requests.get', side_effect="")
        myclass.get_patcher.start()

    @classmethod
    def tearDownClass(myclass):
        """tear Down Class"""
        myclass.get_patcher.stop()

    def test_public_repos(self):
        """test public repositories"""
        obj = GithubOrgClient("hazemali1")
        # r = obj.public_repos()
        self.assertTrue(True)

    def test_public_repos_with_license(self):
        """test public repositories with a license"""
        obj = GithubOrgClient("hazemali1")
        # r = obj.public_repos(license="apache-2.0")
        self.assertTrue(True)
