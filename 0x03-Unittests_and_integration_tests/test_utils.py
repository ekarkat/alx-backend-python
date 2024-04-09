#!/usr/bin/env python3
"""TASKS 1"""

import unittest
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """the first unit test"""

    @parameterized.expand(
        [
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2)
        ]
    )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """test that the method returns"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

    @parameterized.expand(
        [
            ({}, ("a",), KeyError),
            ({"a": 1}, ("a", "b"), KeyError)
        ]
    )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """KeyError"""
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)

class TestGetJson(unittest.TestCase):
    """Test get json method"""
    @parameterized.expand(
        [
            ('http://example.com', {'payload': True}),
            ('http://holberton.io', {'payload': False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """
			Test that the mocked get method
			was called exactly once (per input)
		"""
        mock = Mock()
        mock.json.return_value = expected_output
        with patch('requests.get', return_value=mock):
            response = get_json(url)

            self.assertEqual(response, expected_output)
