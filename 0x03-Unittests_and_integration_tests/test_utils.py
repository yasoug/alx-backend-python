#!/usr/bin/env python3
"""Script for testing the utils module"""

from unittest import TestCase
from parameterized import parameterized
from typing import Mapping, Sequence, Dict, Tuple, Union
from utils import access_nested_map


class TestAccessNestedMap(TestCase):
    """Test cases for the access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(
            self,
            nested_map: Mapping,
            path: Sequence,
            expected: Union[Dict, int]
            ) -> None:
        """Test the output of access_nested_map"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError),
    ])
    def test_access_nested_map_exception(
            self,
            nested_map: Mapping,
            path: Sequence,
            exception: Exception,
            ) -> None:
        """Test exceptions for access_nested_map"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)
