#!/usr/bin/env python3

import unittest
from unittest.mock import patch
from utils import access_nested_map 
from utils import get_json 
from parameterized import parameterized

class TestAccessNestedMap(unittest.TestCase):
    """
    Unitest Class for testing utils functions
    """
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])

    def test_access_nested_map(self, nested_map, path, expected):
        """
        test for test_access_nested_map
        """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
            ({}, ("a",), "'a'"),
            ({"a": 1}, ("a", "b"), "'b'"),  
        ])
    
    def test_access_nested_map_exception(self, nested_map, path, expected_message):
        """
        Testing KeyError error Handling 
        """
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)

        self.assertEqual(str(context.exception), expected_message)


class TestGetJson(unittest.TestCase):
    """
    Test class ofr get_json function
    """
    parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])

    @patch("utils.requests.get")
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Mock test for get_json function
        """
        mock_get.return_value.json.return_value = test_payload
        result = get_json(test_url)
        self.assertEqual(result, test_payload)
        mock_get.assert_called_once_with(test_url)