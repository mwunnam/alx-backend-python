#!/usr/bin/env python3
"""Test For utils.access_nested_map"""
from parameterized import parameterized
from unittest import TestCase
import utils


class TestAccessnestedMap(unittest.TestCase):
    """Test class using parameterize for test"""

    @parameterized.expand([
            ({"a": 1}, ("a",), 1),
            ({"a": {"b": 2}}, ("a",) {"b": 2}),
            ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        self.assertEqual(utils.access_nested_map(nested_map, path), expected)
