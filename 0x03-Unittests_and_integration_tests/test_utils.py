#!/usr/bin/env python3
"""Unit tests for the utils module functions: access_nested_map,
get_json, and memoize."""

import unittest
from unittest.mock import patch
from utils import access_nested_map
from utils import get_json
from utils import memoize
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
    def test_access_nested_map_exception(
        self,
        nested_map,
        path,
        expected_message
    ):
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
    @parameterized.expand([
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


class TestMemoize(unittest.TestCase):
    """
    Unit tests for the `memoize` decorator function.
    """
    def test_memoize(self):
        """
        Test that a method decorated with @memoize is only called once,
        and the result is cached and returned on subsequent calls.
        """
        class TestClass:
            """
           Class with a method and a memoized property.
           for the testing to be able to take place
            """
            def a_method(self):
                """
                Method that returns a constant for the testing
                to be able take place
                """
                return 42

            @memoize
            def a_property(self):
                """
                Memoized property that calls a_method and keeps it return value
                if it's the same
                """
                return self.a_method()

        with patch.object(
            TestClass,
            'a_method',
            return_value=42
        ) as mock_method:

            obj = TestClass()
            result1 = obj.a_property
            result2 = obj.a_property

            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)
            mock_method.assert_called_once()
