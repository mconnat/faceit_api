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
from faceit_api.api.tournaments_api import TournamentsApi  # noqa: E501
from faceit_api.rest import ApiException


class TestTournamentsApi(unittest.TestCase):
    """TournamentsApi unit test stubs"""

    def setUp(self):
        self.api = faceit_api.api.tournaments_api.TournamentsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_tournament(self):
        """Test case for get_tournament

        Retrieve tournament details  # noqa: E501
        """
        pass

    def test_get_tournament_brackets(self):
        """Test case for get_tournament_brackets

        Retrieve brackets of a tournament  # noqa: E501
        """
        pass

    def test_get_tournament_matches(self):
        """Test case for get_tournament_matches

        Retrieve all matches of a tournament  # noqa: E501
        """
        pass

    def test_get_tournament_teams(self):
        """Test case for get_tournament_teams

        Retrieve all teams of a tournament  # noqa: E501
        """
        pass

    def test_get_tournaments_list(self):
        """Test case for get_tournaments_list

        Retrieve tournaments v1 (no longer used)  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()