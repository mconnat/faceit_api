# faceit_api.ChampionshipsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_championship**](ChampionshipsApi.md#get_championship) | **GET** /championships/{championship_id} | Retrieve championship details
[**get_championship_matches**](ChampionshipsApi.md#get_championship_matches) | **GET** /championships/{championship_id}/matches | Retrieve all matches of a championship
[**get_championship_results**](ChampionshipsApi.md#get_championship_results) | **GET** /championships/{championship_id}/results | Retrieve all results of a championship
[**get_championship_subscriptions**](ChampionshipsApi.md#get_championship_subscriptions) | **GET** /championships/{championship_id}/subscriptions | Retrieve all subscriptions of a championship
[**get_championships**](ChampionshipsApi.md#get_championships) | **GET** /championships | Retrieve all championships of a game


# **get_championship**
> Championship get_championship(championship_id, expanded=expanded)

Retrieve championship details

Retrieve championship details

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
expanded = ['expanded_example'] # list[str] | List of entity names to expand in request (optional)

try:
    # Retrieve championship details
    api_response = api_instance.get_championship(championship_id, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championship: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
 **expanded** | [**list[str]**](str.md)| List of entity names to expand in request | [optional] 

### Return type

[**Championship**](Championship.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_championship_matches**
> MatchList get_championship_matches(championship_id, type=type, offset=offset, limit=limit)

Retrieve all matches of a championship

Retrieve all matches of a championship

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
type = 'type_example' # str | Kind of matches to return. Can be all(default), upcoming, ongoing or past (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all matches of a championship
    api_response = api_instance.get_championship_matches(championship_id, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championship_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
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

# **get_championship_results**
> ChampionshipResultList get_championship_results(championship_id, offset=offset, limit=limit)

Retrieve all results of a championship

Retrieve all results of a championship

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all results of a championship
    api_response = api_instance.get_championship_results(championship_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championship_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**ChampionshipResultList**](ChampionshipResultList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_championship_subscriptions**
> ChampionshipSubscriptionsList get_championship_subscriptions(championship_id, offset=offset, limit=limit)

Retrieve all subscriptions of a championship

Retrieve all subscriptions of a championship

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 10 # int | The number of items to return (optional) (default to 10)

try:
    # Retrieve all subscriptions of a championship
    api_response = api_instance.get_championship_subscriptions(championship_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championship_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 10]

### Return type

[**ChampionshipSubscriptionsList**](ChampionshipSubscriptionsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_championships**
> ChampionshipsList get_championships(game, type=type, offset=offset, limit=limit)

Retrieve all championships of a game

Retrieve all championships of a game

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
game = 'game_example' # str | The id of the game
type = 'type_example' # str | Kind of matches to return. Can be all(default), upcoming, ongoing or past (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 10 # int | The number of items to return (optional) (default to 10)

try:
    # Retrieve all championships of a game
    api_response = api_instance.get_championships(game, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| The id of the game | 
 **type** | **str**| Kind of matches to return. Can be all(default), upcoming, ongoing or past | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 10]

### Return type

[**ChampionshipsList**](ChampionshipsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

