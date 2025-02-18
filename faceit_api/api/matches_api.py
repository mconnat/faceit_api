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


class MatchesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_match(self, match_id, **kwargs):  # noqa: E501
        """Retrieve match details  # noqa: E501

        Retrieve match details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_match(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_id: The id of the match (required)
        :return: Match
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_match_with_http_info(match_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_match_with_http_info(match_id, **kwargs)  # noqa: E501
            return data

    def get_match_with_http_info(self, match_id, **kwargs):  # noqa: E501
        """Retrieve match details  # noqa: E501

        Retrieve match details  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_match_with_http_info(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_id: The id of the match (required)
        :return: Match
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_match" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if self.api_client.client_side_validation and ('match_id' not in params or
                                                       params['match_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `match_id` when calling `get_match`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['match_id'] = params['match_id']  # noqa: E501

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
            '/matches/{match_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Match',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_match_stats(self, match_id, **kwargs):  # noqa: E501
        """Retrieve statistics of a match  # noqa: E501

        Retrieve statistics of a match  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_match_stats(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_id: The id of the match (required)
        :return: MatchStats
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_match_stats_with_http_info(match_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_match_stats_with_http_info(match_id, **kwargs)  # noqa: E501
            return data

    def get_match_stats_with_http_info(self, match_id, **kwargs):  # noqa: E501
        """Retrieve statistics of a match  # noqa: E501

        Retrieve statistics of a match  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_match_stats_with_http_info(match_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str match_id: The id of the match (required)
        :return: MatchStats
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['match_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_match_stats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'match_id' is set
        if self.api_client.client_side_validation and ('match_id' not in params or
                                                       params['match_id'] is None):  # noqa: E501
            raise ValueError("Missing the required parameter `match_id` when calling `get_match_stats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'match_id' in params:
            path_params['match_id'] = params['match_id']  # noqa: E501

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
            '/matches/{match_id}/stats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MatchStats',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
