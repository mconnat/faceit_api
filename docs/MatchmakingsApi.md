# faceit_api.MatchmakingsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_matchmaking**](MatchmakingsApi.md#get_matchmaking) | **GET** /matchmakings/{matchmaking_id} | Retrieve details of a matchmaking of a game on FACEIT


# **get_matchmaking**
> Matchmaking get_matchmaking(matchmaking_id)

Retrieve details of a matchmaking of a game on FACEIT

Retrieve details of a matchmaking of a game on FACEIT

### Example
```python
from __future__ import print_function
import time
import faceit_api
from faceit_api.rest import ApiException
from pprint import pprint

# Configure API key authorization: key
configuration = faceit_api.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = faceit_api.MatchmakingsApi(faceit_api.ApiClient(configuration))
matchmaking_id = 'matchmaking_id_example' # str | The id of the matchmaking

try:
    # Retrieve details of a matchmaking of a game on FACEIT
    api_response = api_instance.get_matchmaking(matchmaking_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchmakingsApi->get_matchmaking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **matchmaking_id** | **str**| The id of the matchmaking | 

### Return type

[**Matchmaking**](Matchmaking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

