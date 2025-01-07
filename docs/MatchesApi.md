# faceit_api.MatchesApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_match**](MatchesApi.md#get_match) | **GET** /matches/{match_id} | Retrieve match details
[**get_match_stats**](MatchesApi.md#get_match_stats) | **GET** /matches/{match_id}/stats | Retrieve statistics of a match


# **get_match**
> Match get_match(match_id)

Retrieve match details

Retrieve match details

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
api_instance = faceit_api.MatchesApi(faceit_api.ApiClient(configuration))
match_id = 'match_id_example' # str | The id of the match

try:
    # Retrieve match details
    api_response = api_instance.get_match(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_match: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| The id of the match | 

### Return type

[**Match**](Match.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_match_stats**
> MatchStats get_match_stats(match_id)

Retrieve statistics of a match

Retrieve statistics of a match

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
api_instance = faceit_api.MatchesApi(faceit_api.ApiClient(configuration))
match_id = 'match_id_example' # str | The id of the match

try:
    # Retrieve statistics of a match
    api_response = api_instance.get_match_stats(match_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MatchesApi->get_match_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **match_id** | **str**| The id of the match | 

### Return type

[**MatchStats**](MatchStats.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

