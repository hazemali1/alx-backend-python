#!/usr/bin/env python3
"""testing"""
import unittest
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    """Test for utils"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, result):
        """Test for AccessNestedMap"""
        res = access_nested_map(nested_map, path)
        self.assertEqual(res, result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(self, nested_map, path, result):
        """Test for AccessNestedMap"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """test for utils json"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock):
        """test for get json"""
        mock.return_value = payload
        self.assertEqual(get_json(url), payload)


class TestMemoize(unittest.TestCase):
    """test for memoize"""
    def test_memoize(self):
        """test momeize"""
        class TestClass:
            """test class"""
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        with patch.object(TestClass, "a_method") as f:
            obj = TestClass()
            obj.a_property
            obj.a_property
            f.assert_called_once
