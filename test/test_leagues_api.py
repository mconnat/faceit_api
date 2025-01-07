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
from faceit_api.api.leagues_api import LeaguesApi  # noqa: E501
from faceit_api.rest import ApiException


class TestLeaguesApi(unittest.TestCase):
    """LeaguesApi unit test stubs"""

    def setUp(self):
        self.api = faceit_api.api.leagues_api.LeaguesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_league_by_id(self):
        """Test case for get_league_by_id

        Retrieve details of a league of a matchmaking on FACEIT  # noqa: E501
        """
        pass

    def test_get_league_season(self):
        """Test case for get_league_season

        Retrieve details of a season of a league on FACEIT  # noqa: E501
        """
        pass

    def test_get_player_for_league_season(self):
        """Test case for get_player_for_league_season

        Retrieve details of a player for a given league and season on FACEIT  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
