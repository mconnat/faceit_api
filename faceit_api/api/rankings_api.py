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


class RankingsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_global_ranking(self, game_id, region, **kwargs):  # noqa: E501
        """Retrieve global ranking of a game  # noqa: E501

        Retrieve global ranking of a game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_ranking(game_id, region, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: The id of the game (required)
        :param str region: A region of a game (required)
        :param str country: A country code (ISO 3166-1)
        :param int offset: The starting item position
        :param int limit: The number of items to return
        :return: GlobalRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_global_ranking_with_http_info(game_id, region, **kwargs)  # noqa: E501
        else:
            (data) = self.get_global_ranking_with_http_info(game_id, region, **kwargs)  # noqa: E501
            return data

    def get_global_ranking_with_http_info(self, game_id, region, **kwargs):  # noqa: E501
        """Retrieve global ranking of a game  # noqa: E501

        Retrieve global ranking of a game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_global_ranking_with_http_info(game_id, region, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: The id of the game (required)
        :param str region: A region of a game (required)
        :param str country: A country code (ISO 3166-1)
        :param int offset: The starting item position
        :param int limit: The number of items to return
        :return: GlobalRankingList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id', 'region', 'country', 'offset', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_global_ranking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_id' is set
        if self.api_client.client_side_validation and ('game_id' not in params or
                                                       params['game_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `game_id` when calling `get_global_ranking`")  # noqa: E501
        # verify the required parameter 'region' is set
        if self.api_client.client_side_validation and ('region' not in params or
                                                       params['region'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `region` when calling `get_global_ranking`")  # noqa: E501

        if self.api_client.client_side_validation and ('offset' in params and params['offset'] < 0):  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `get_global_ranking`, must be a value greater than or equal to `0`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_global_ranking`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_global_ranking`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'game_id' in params:
            path_params['game_id'] = params['game_id']  # noqa: E501
        if 'region' in params:
            path_params['region'] = params['region']  # noqa: E501

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/rankings/games/{game_id}/regions/{region}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GlobalRankingList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_player_ranking(self, game_id, region, player_id, **kwargs):  # noqa: E501
        """Retrieve user position in the global ranking of a game  # noqa: E501

        Retrieve user position in the global ranking of a game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_ranking(game_id, region, player_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: The id of the game (required)
        :param str region: A region of a game (required)
        :param str player_id: The id of a player (required)
        :param str country: A country code (ISO 3166-1)
        :param int limit: The number of items to return
        :return: PlayerGlobalRanking
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_player_ranking_with_http_info(game_id, region, player_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_player_ranking_with_http_info(game_id, region, player_id, **kwargs)  # noqa: E501
            return data

    def get_player_ranking_with_http_info(self, game_id, region, player_id, **kwargs):  # noqa: E501
        """Retrieve user position in the global ranking of a game  # noqa: E501

        Retrieve user position in the global ranking of a game  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_player_ranking_with_http_info(game_id, region, player_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str game_id: The id of the game (required)
        :param str region: A region of a game (required)
        :param str player_id: The id of a player (required)
        :param str country: A country code (ISO 3166-1)
        :param int limit: The number of items to return
        :return: PlayerGlobalRanking
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['game_id', 'region', 'player_id', 'country', 'limit']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_player_ranking" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'game_id' is set
        if self.api_client.client_side_validation and ('game_id' not in params or
                                                       params['game_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `game_id` when calling `get_player_ranking`")  # noqa: E501
        # verify the required parameter 'region' is set
        if self.api_client.client_side_validation and ('region' not in params or
                                                       params['region'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `region` when calling `get_player_ranking`")  # noqa: E501
        # verify the required parameter 'player_id' is set
        if self.api_client.client_side_validation and ('player_id' not in params or
                                                       params['player_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `player_id` when calling `get_player_ranking`")  # noqa: E501

        if self.api_client.client_side_validation and ('limit' in params and params['limit'] > 100):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_player_ranking`, must be a value less than or equal to `100`")  # noqa: E501
        if self.api_client.client_side_validation and ('limit' in params and params['limit'] < 1):  # noqa: E501
            raise ValueError("Invalid value for parameter `limit` when calling `get_player_ranking`, must be a value greater than or equal to `1`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'game_id' in params:
            path_params['game_id'] = params['game_id']  # noqa: E501
        if 'region' in params:
            path_params['region'] = params['region']  # noqa: E501
        if 'player_id' in params:
            path_params['player_id'] = params['player_id']  # noqa: E501

        query_params = []
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501

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
            '/rankings/games/{game_id}/regions/{region}/players/{player_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PlayerGlobalRanking',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
