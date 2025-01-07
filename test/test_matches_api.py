# coding: utf-8

"""
    Data API

    # This API provide access to FACEIT's data  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import faceit_api
from faceit_api.api.matches_api import MatchesApi  # noqa: E501
from faceit_api.rest import ApiException


class TestMatchesApi(unittest.TestCase):
    """MatchesApi unit test stubs"""

    def setUp(self):
        self.api = faceit_api.api.matches_api.MatchesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_match(self):
        """Test case for get_match

        Retrieve match details  # noqa: E501
        """
        pass

    def test_get_match_stats(self):
        """Test case for get_match_stats

        Retrieve statistics of a match  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()