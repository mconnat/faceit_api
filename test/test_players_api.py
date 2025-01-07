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
from faceit_api.api.players_api import PlayersApi  # noqa: E501
from faceit_api.rest import ApiException


class TestPlayersApi(unittest.TestCase):
    """PlayersApi unit test stubs"""

    def setUp(self):
        self.api = faceit_api.api.players_api.PlayersApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_player(self):
        """Test case for get_player

        Retrieve player details  # noqa: E501
        """
        pass

    def test_get_player_bans(self):
        """Test case for get_player_bans

        Retrieve all bans of a player  # noqa: E501
        """
        pass

    def test_get_player_from_lookup(self):
        """Test case for get_player_from_lookup

        Retrieve player details  # noqa: E501
        """
        pass

    def test_get_player_history(self):
        """Test case for get_player_history

        Retrieve all matches of a player  # noqa: E501
        """
        pass

    def test_get_player_hubs(self):
        """Test case for get_player_hubs

        Retrieve all hubs of a player  # noqa: E501
        """
        pass

    def test_get_player_stats(self):
        """Test case for get_player_stats

        Retrieve statistics of a player for a given amount of matches  # noqa: E501
        """
        pass

    def test_get_player_stats_0(self):
        """Test case for get_player_stats_0

        Retrieve statistics of a player  # noqa: E501
        """
        pass

    def test_get_player_teams(self):
        """Test case for get_player_teams

        Retrieve all teams of a player  # noqa: E501
        """
        pass

    def test_get_player_tournaments(self):
        """Test case for get_player_tournaments

        Retrieve all tournaments of a player  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
