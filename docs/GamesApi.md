# faceit_api.GamesApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_games**](GamesApi.md#get_all_games) | **GET** /games | Retrieve details of all games on FACEIT
[**get_game**](GamesApi.md#get_game) | **GET** /games/{game_id} | Retrieve game details
[**get_game_matchmakings**](GamesApi.md#get_game_matchmakings) | **GET** /games/{gameId}/matchmakings | Retrieve details of all matchmakings of a game on FACEIT
[**get_parent_game**](GamesApi.md#get_parent_game) | **GET** /games/{game_id}/parent | Retrieve the details of the parent game, if the game is region-specific
[**get_queue_bans**](GamesApi.md#get_queue_bans) | **GET** /games/{game_id}/queues/{queue_id}/bans | Retrieve queue bans on FACEIT
[**get_queue_by_id**](GamesApi.md#get_queue_by_id) | **GET** /games/{game_id}/queues/{queue_id} | Retrieve details of a queue on FACEIT
[**get_queues_by_entity_filters**](GamesApi.md#get_queues_by_entity_filters) | **GET** /games/{game_id}/queues | Retrieve queues by filters on FACEIT
[**get_queues_by_region**](GamesApi.md#get_queues_by_region) | **GET** /games/{game_id}/regions/{region_id}/queues | Retrieve queues by region on FACEIT


# **get_all_games**
> GamesList get_all_games(offset=offset, limit=limit)

Retrieve details of all games on FACEIT

Retrieve details of all games on FACEIT

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve details of all games on FACEIT
    api_response = api_instance.get_all_games(offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_all_games: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**GamesList**](GamesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game**
> Game get_game(game_id)

Retrieve game details

Retrieve game details

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game

try:
    # Retrieve game details
    api_response = api_instance.get_game(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 

### Return type

[**Game**](Game.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_game_matchmakings**
> MatchmakingList get_game_matchmakings(game_id, region=region, offset=offset, limit=limit)

Retrieve details of all matchmakings of a game on FACEIT

Retrieve details of all matchmakings of a game on FACEIT

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
region = 'region_example' # str | The region of the matchmakings (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve details of all matchmakings of a game on FACEIT
    api_response = api_instance.get_game_matchmakings(game_id, region=region, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_game_matchmakings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **region** | **str**| The region of the matchmakings | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**MatchmakingList**](MatchmakingList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_parent_game**
> Game get_parent_game(game_id)

Retrieve the details of the parent game, if the game is region-specific

Retrieve the details of the parent game, if the game is region-specific

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game

try:
    # Retrieve the details of the parent game, if the game is region-specific
    api_response = api_instance.get_parent_game(game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_parent_game: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 

### Return type

[**Game**](Game.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_bans**
> QueueBansList get_queue_bans(game_id, queue_id, offset=offset, limit=limit)

Retrieve queue bans on FACEIT

Retrieve queue bans on FACEIT. Available only for game or queue owners(organizers)

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
queue_id = 'queue_id_example' # str | The id of the queue
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve queue bans on FACEIT
    api_response = api_instance.get_queue_bans(game_id, queue_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_queue_bans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **queue_id** | **str**| The id of the queue | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**QueueBansList**](QueueBansList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queue_by_id**
> Queue get_queue_by_id(game_id, queue_id)

Retrieve details of a queue on FACEIT

Retrieve details of a queue on FACEIT. Available only for game or queue owners(organizers)

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
queue_id = 'queue_id_example' # str | The id of the queue

try:
    # Retrieve details of a queue on FACEIT
    api_response = api_instance.get_queue_by_id(game_id, queue_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_queue_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **queue_id** | **str**| The id of the queue | 

### Return type

[**Queue**](Queue.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queues_by_entity_filters**
> QueuesList get_queues_by_entity_filters(game_id, entity_type, entity_id, offset=offset, limit=limit)

Retrieve queues by filters on FACEIT

Retrieve queues by filters on FACEIT. Available only for game developers and queue owners(organizers)

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
entity_type = 'entity_type_example' # str | The type of the entity
entity_id = 'entity_id_example' # str | The id of the entity
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve queues by filters on FACEIT
    api_response = api_instance.get_queues_by_entity_filters(game_id, entity_type, entity_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_queues_by_entity_filters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **entity_type** | **str**| The type of the entity | 
 **entity_id** | **str**| The id of the entity | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**QueuesList**](QueuesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_queues_by_region**
> QueuesList get_queues_by_region(game_id, region_id, offset=offset, limit=limit)

Retrieve queues by region on FACEIT

Retrieve queues by region on FACEIT. Available only for game developers

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
api_instance = faceit_api.GamesApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
region_id = 'region_id_example' # str | The id of the region
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve queues by region on FACEIT
    api_response = api_instance.get_queues_by_region(game_id, region_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling GamesApi->get_queues_by_region: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **region_id** | **str**| The id of the region | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**QueuesList**](QueuesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

