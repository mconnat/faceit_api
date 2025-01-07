# coding: utf-8

"""
    Data API

    # This API provide access to FACEIT's data  # noqa: E501

    OpenAPI spec version: 4
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from faceit_api.api_client import ApiClient


class LeaguesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_league_by_id(self, league_id, **kwargs):  # noqa: E501
        """Retrieve details of a league of a matchmaking on FACEIT  # noqa: E501

        Retrieve details of a league of a matchmaking on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_league_by_id(league_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :return: League
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_league_by_id_with_http_info(league_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_league_by_id_with_http_info(league_id, **kwargs)  # noqa: E501
            return data

    def get_league_by_id_with_http_info(self, league_id, **kwargs):  # noqa: E501
        """Retrieve details of a league of a matchmaking on FACEIT  # noqa: E501

        Retrieve details of a league of a matchmaking on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_league_by_id_with_http_info(league_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :return: League
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['league_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_league_by_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'league_id' is set
        if self.api_client.client_side_validation and ('league_id' not in params or
                                                       params['league_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `league_id` when calling `get_league_by_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'league_id' in params:
            path_params['league_id'] = params['league_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/leagues/{league_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='League',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_league_season(self, league_id, season_id, **kwargs):  # noqa: E501
        """Retrieve details of a season of a league on FACEIT  # noqa: E501

        Retrieve details of a season of a league on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_league_season(league_id, season_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :param int season_id: The id of the season (required)
        :return: SeasonDetailed
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_league_season_with_http_info(league_id, season_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_league_season_with_http_info(league_id, season_id, **kwargs)  # noqa: E501
            return data

    def get_league_season_with_http_info(self, league_id, season_id, **kwargs):  # noqa: E501
        """Retrieve details of a season of a league on FACEIT  # noqa: E501

        Retrieve details of a season of a league on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_league_season_with_http_info(league_id, season_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :param int season_id: The id of the season (required)
        :return: SeasonDetailed
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['league_id', 'season_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_league_season" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'league_id' is set
        if self.api_client.client_side_validation and ('league_id' not in params or
                                                       params['league_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `league_id` when calling `get_league_season`")  # noqa: E501
        # verify the required parameter 'season_id' is set
        if self.api_client.client_side_validation and ('season_id' not in params or
                                                       params['season_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `season_id` when calling `get_league_season`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'league_id' in params:
            path_params['league_id'] = params['league_id']  # noqa: E501
        if 'season_id' in params:
            path_params['season_id'] = params['season_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/leagues/{league_id}/seasons/{season_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='SeasonDetailed',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_for_league_season(self, league_id, season_id, player_id, **kwargs):  # noqa: E501
        """Retrieve details of a player for a given league and season on FACEIT  # noqa: E501

        Retrieve details of a player for a given league and season on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_for_league_season(league_id, season_id, player_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :param int season_id: The id of the season (required)
        :param str player_id: The id of the player (required)
        :return: PlayerInLeague
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_for_league_season_with_http_info(league_id, season_id, player_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_for_league_season_with_http_info(league_id, season_id, player_id, **kwargs)  # noqa: E501
            return data

    def get_player_for_league_season_with_http_info(self, league_id, season_id, player_id, **kwargs):  # noqa: E501
        """Retrieve details of a player for a given league and season on FACEIT  # noqa: E501

        Retrieve details of a player for a given league and season on FACEIT  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_for_league_season_with_http_info(league_id, season_id, player_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str league_id: The id of the league (required)
        :param int season_id: The id of the season (required)
        :param str player_id: The id of the player (required)
        :return: PlayerInLeague
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['league_id', 'season_id', 'player_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_for_league_season" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'league_id' is set
        if self.api_client.client_side_validation and ('league_id' not in params or
                                                       params['league_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `league_id` when calling `get_player_for_league_season`")  # noqa: E501
        # verify the required parameter 'season_id' is set
        if self.api_client.client_side_validation and ('season_id' not in params or
                                                       params['season_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `season_id` when calling `get_player_for_league_season`")  # noqa: E501
        # verify the required parameter 'player_id' is set
        if self.api_client.client_side_validation and ('player_id' not in params or
                                                       params['player_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `player_id` when calling `get_player_for_league_season`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'league_id' in params:
            path_params['league_id'] = params['league_id']  # noqa: E501
        if 'season_id' in params:
            path_params['season_id'] = params['season_id']  # noqa: E501
        if 'player_id' in params:
            path_params['player_id'] = params['player_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['key']  # noqa: E501

        return self.api_client.call_api(
            '/leagues/{league_id}/seasons/{season_id}/players/{player_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerInLeague',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
