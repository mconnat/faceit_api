# faceit_api.RankingsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_global_ranking**](RankingsApi.md#get_global_ranking) | **GET** /rankings/games/{game_id}/regions/{region} | Retrieve global ranking of a game
[**get_player_ranking**](RankingsApi.md#get_player_ranking) | **GET** /rankings/games/{game_id}/regions/{region}/players/{player_id} | Retrieve user position in the global ranking of a game


# **get_global_ranking**
> GlobalRankingList get_global_ranking(game_id, region, country=country, offset=offset, limit=limit)

Retrieve global ranking of a game

Retrieve global ranking of a game

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
api_instance = faceit_api.RankingsApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
region = 'region_example' # str | A region of a game
country = 'country_example' # str | A country code (ISO 3166-1) (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve global ranking of a game
    api_response = api_instance.get_global_ranking(game_id, region, country=country, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_global_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **region** | **str**| A region of a game | 
 **country** | **str**| A country code (ISO 3166-1) | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**GlobalRankingList**](GlobalRankingList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_ranking**
> PlayerGlobalRanking get_player_ranking(game_id, region, player_id, country=country, limit=limit)

Retrieve user position in the global ranking of a game

Retrieve user position in the global ranking of a game

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
api_instance = faceit_api.RankingsApi(faceit_api.ApiClient(configuration))
game_id = 'game_id_example' # str | The id of the game
region = 'region_example' # str | A region of a game
player_id = 'player_id_example' # str | The id of a player
country = 'country_example' # str | A country code (ISO 3166-1) (optional)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve user position in the global ranking of a game
    api_response = api_instance.get_player_ranking(game_id, region, player_id, country=country, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RankingsApi->get_player_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game_id** | **str**| The id of the game | 
 **region** | **str**| A region of a game | 
 **player_id** | **str**| The id of a player | 
 **country** | **str**| A country code (ISO 3166-1) | [optional] 
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**PlayerGlobalRanking**](PlayerGlobalRanking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

