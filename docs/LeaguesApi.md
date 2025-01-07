# faceit_api.LeaguesApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_league_by_id**](LeaguesApi.md#get_league_by_id) | **GET** /leagues/{league_id} | Retrieve details of a league of a matchmaking on FACEIT
[**get_league_season**](LeaguesApi.md#get_league_season) | **GET** /leagues/{league_id}/seasons/{season_id} | Retrieve details of a season of a league on FACEIT
[**get_player_for_league_season**](LeaguesApi.md#get_player_for_league_season) | **GET** /leagues/{league_id}/seasons/{season_id}/players/{player_id} | Retrieve details of a player for a given league and season on FACEIT


# **get_league_by_id**
> League get_league_by_id(league_id)

Retrieve details of a league of a matchmaking on FACEIT

Retrieve details of a league of a matchmaking on FACEIT

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
api_instance = faceit_api.LeaguesApi(faceit_api.ApiClient(configuration))
league_id = 'league_id_example' # str | The id of the league

try:
    # Retrieve details of a league of a matchmaking on FACEIT
    api_response = api_instance.get_league_by_id(league_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_league_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| The id of the league | 

### Return type

[**League**](League.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_league_season**
> SeasonDetailed get_league_season(league_id, season_id)

Retrieve details of a season of a league on FACEIT

Retrieve details of a season of a league on FACEIT

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
api_instance = faceit_api.LeaguesApi(faceit_api.ApiClient(configuration))
league_id = 'league_id_example' # str | The id of the league
season_id = 56 # int | The id of the season

try:
    # Retrieve details of a season of a league on FACEIT
    api_response = api_instance.get_league_season(league_id, season_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_league_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| The id of the league | 
 **season_id** | **int**| The id of the season | 

### Return type

[**SeasonDetailed**](SeasonDetailed.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_for_league_season**
> PlayerInLeague get_player_for_league_season(league_id, season_id, player_id)

Retrieve details of a player for a given league and season on FACEIT

Retrieve details of a player for a given league and season on FACEIT

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
api_instance = faceit_api.LeaguesApi(faceit_api.ApiClient(configuration))
league_id = 'league_id_example' # str | The id of the league
season_id = 56 # int | The id of the season
player_id = 'player_id_example' # str | The id of the player

try:
    # Retrieve details of a player for a given league and season on FACEIT
    api_response = api_instance.get_player_for_league_season(league_id, season_id, player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaguesApi->get_player_for_league_season: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **league_id** | **str**| The id of the league | 
 **season_id** | **int**| The id of the season | 
 **player_id** | **str**| The id of the player | 

### Return type

[**PlayerInLeague**](PlayerInLeague.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

