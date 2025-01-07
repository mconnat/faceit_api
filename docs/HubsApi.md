# faceit_api.HubsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_hub**](HubsApi.md#get_hub) | **GET** /hubs/{hub_id} | Retrieve hub details
[**get_hub_matches**](HubsApi.md#get_hub_matches) | **GET** /hubs/{hub_id}/matches | Retrieve all matches of a hub
[**get_hub_members**](HubsApi.md#get_hub_members) | **GET** /hubs/{hub_id}/members | Retrieve all members of a hub
[**get_hub_roles**](HubsApi.md#get_hub_roles) | **GET** /hubs/{hub_id}/roles | Retrieve all roles members can have in a hub
[**get_hub_rules**](HubsApi.md#get_hub_rules) | **GET** /hubs/{hub_id}/rules | Retrieve rules of a hub
[**get_hub_stats**](HubsApi.md#get_hub_stats) | **GET** /hubs/{hub_id}/stats | Retrieve statistics of a hub


# **get_hub**
> Hub get_hub(hub_id, expanded=expanded)

Retrieve hub details

Retrieve hub details

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
expanded = ['expanded_example'] # list[str] | List of entity names to expand in request (optional)

try:
    # Retrieve hub details
    api_response = api_instance.get_hub(hub_id, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **expanded** | [**list[str]**](str.md)| List of entity names to expand in request | [optional] 

### Return type

[**Hub**](Hub.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_matches**
> MatchList get_hub_matches(hub_id, type=type, offset=offset, limit=limit)

Retrieve all matches of a hub

Retrieve all matches of a hub

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
type = 'type_example' # str | Kind of matches to return. Can be all(default), upcoming, ongoing or past (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all matches of a hub
    api_response = api_instance.get_hub_matches(hub_id, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **type** | **str**| Kind of matches to return. Can be all(default), upcoming, ongoing or past | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**MatchList**](MatchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_members**
> HubMembers get_hub_members(hub_id, offset=offset, limit=limit)

Retrieve all members of a hub

Retrieve all members of a hub

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 50 # int | The number of items to return (optional) (default to 50)

try:
    # Retrieve all members of a hub
    api_response = api_instance.get_hub_members(hub_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub_members: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 50]

### Return type

[**HubMembers**](HubMembers.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_roles**
> RolesList get_hub_roles(hub_id, offset=offset, limit=limit)

Retrieve all roles members can have in a hub

Retrieve all roles members can have in a hub

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 50 # int | The number of items to return (optional) (default to 50)

try:
    # Retrieve all roles members can have in a hub
    api_response = api_instance.get_hub_roles(hub_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub_roles: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 50]

### Return type

[**RolesList**](RolesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_rules**
> Rules get_hub_rules(hub_id)

Retrieve rules of a hub

Retrieve rules of a hub

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub

try:
    # Retrieve rules of a hub
    api_response = api_instance.get_hub_rules(hub_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub_rules: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 

### Return type

[**Rules**](Rules.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_stats**
> HubStats get_hub_stats(hub_id, offset=offset, limit=limit)

Retrieve statistics of a hub

Retrieve statistics of a hub

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
api_instance = faceit_api.HubsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve statistics of a hub
    api_response = api_instance.get_hub_stats(hub_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling HubsApi->get_hub_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**HubStats**](HubStats.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

