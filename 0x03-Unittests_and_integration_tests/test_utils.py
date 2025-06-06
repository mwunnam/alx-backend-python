 #!/usr/bin/env python3

import unittest
from utils import access_nested_map
from parameterized import parameterized

class TestUtils(unittest.TestCase):
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