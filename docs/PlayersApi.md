# faceit_api.PlayersApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_player**](PlayersApi.md#get_player) | **GET** /players/{player_id} | Retrieve player details
[**get_player_bans**](PlayersApi.md#get_player_bans) | **GET** /players/{player_id}/bans | Retrieve all bans of a player
[**get_player_from_lookup**](PlayersApi.md#get_player_from_lookup) | **GET** /players | Retrieve player details
[**get_player_history**](PlayersApi.md#get_player_history) | **GET** /players/{player_id}/history | Retrieve all matches of a player
[**get_player_hubs**](PlayersApi.md#get_player_hubs) | **GET** /players/{player_id}/hubs | Retrieve all hubs of a player
[**get_player_stats**](PlayersApi.md#get_player_stats) | **GET** /players/{player_id}/games/{game_id}/stats | Retrieve statistics of a player for a given amount of matches
[**get_player_stats_0**](PlayersApi.md#get_player_stats_0) | **GET** /players/{player_id}/stats/{game_id} | Retrieve statistics of a player
[**get_player_teams**](PlayersApi.md#get_player_teams) | **GET** /players/{player_id}/teams | Retrieve all teams of a player
[**get_player_tournaments**](PlayersApi.md#get_player_tournaments) | **GET** /players/{player_id}/tournaments | Retrieve all tournaments of a player


# **get_player**
> Player get_player(player_id)

Retrieve player details

Retrieve player details

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player

try:
    # Retrieve player details
    api_response = api_instance.get_player(player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 

### Return type

[**Player**](Player.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_bans**
> PlayerBansList get_player_bans(player_id, offset=offset, limit=limit)

Retrieve all bans of a player

Retrieve all bans of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all bans of a player
    api_response = api_instance.get_player_bans(player_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_bans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**PlayerBansList**](PlayerBansList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_from_lookup**
> Player get_player_from_lookup(nickname=nickname, game=game, game_player_id=game_player_id)

Retrieve player details

Retrieve player details

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
nickname = 'nickname_example' # str | The nickname of the player on FACEIT (optional)
game = 'game_example' # str | A game on FACEIT (optional)
game_player_id = 'game_player_id_example' # str | The ID of a player on game's platform (optional)

try:
    # Retrieve player details
    api_response = api_instance.get_player_from_lookup(nickname=nickname, game=game, game_player_id=game_player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_from_lookup: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nickname** | **str**| The nickname of the player on FACEIT | [optional] 
 **game** | **str**| A game on FACEIT | [optional] 
 **game_player_id** | **str**| The ID of a player on game&#39;s platform | [optional] 

### Return type

[**Player**](Player.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_history**
> MatchHistoryList get_player_history(player_id, game, _from=_from, to=to, offset=offset, limit=limit)

Retrieve all matches of a player

Retrieve all matches of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
game = 'game_example' # str | A game on FACEIT
_from = 56 # int | The timestamp (Unix time) as lower bound of the query. 1 month ago if not specified (optional)
to = 56 # int | The timestamp (Unix time) as higher bound of the query. Current timestamp if not specified (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all matches of a player
    api_response = api_instance.get_player_history(player_id, game, _from=_from, to=to, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_history: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **game** | **str**| A game on FACEIT | 
 **_from** | **int**| The timestamp (Unix time) as lower bound of the query. 1 month ago if not specified | [optional] 
 **to** | **int**| The timestamp (Unix time) as higher bound of the query. Current timestamp if not specified | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**MatchHistoryList**](MatchHistoryList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_hubs**
> HubsList get_player_hubs(player_id, offset=offset, limit=limit)

Retrieve all hubs of a player

Retrieve all hubs of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 50 # int | The number of items to return (optional) (default to 50)

try:
    # Retrieve all hubs of a player
    api_response = api_instance.get_player_hubs(player_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_hubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 50]

### Return type

[**HubsList**](HubsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_stats**
> PlayerStatsForMatchesList get_player_stats(player_id, game_id, offset=offset, limit=limit, _from=_from, to=to)

Retrieve statistics of a player for a given amount of matches

Retrieve statistics of a player for a given amount of matches

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
game_id = 'game_id_example' # str | A game on FACEIT
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)
_from = 56 # int | Used to filter the dataset by date (minimum). Expected value is date (\"items.stats.Match Finished At\") in epoch milliseconds.  (optional)
to = 56 # int | Used to filter the dataset by date (maximum). Expected value is date (\"items.stats.Match Finished At\") in epoch milliseconds.  (optional)

try:
    # Retrieve statistics of a player for a given amount of matches
    api_response = api_instance.get_player_stats(player_id, game_id, offset=offset, limit=limit, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **game_id** | **str**| A game on FACEIT | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]
 **_from** | **int**| Used to filter the dataset by date (minimum). Expected value is date (\&quot;items.stats.Match Finished At\&quot;) in epoch milliseconds.  | [optional] 
 **to** | **int**| Used to filter the dataset by date (maximum). Expected value is date (\&quot;items.stats.Match Finished At\&quot;) in epoch milliseconds.  | [optional] 

### Return type

[**PlayerStatsForMatchesList**](PlayerStatsForMatchesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_stats_0**
> PlayerStats get_player_stats_0(player_id, game_id)

Retrieve statistics of a player

Retrieve statistics of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
game_id = 'game_id_example' # str | A game on FACEIT

try:
    # Retrieve statistics of a player
    api_response = api_instance.get_player_stats_0(player_id, game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_stats_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **game_id** | **str**| A game on FACEIT | 

### Return type

[**PlayerStats**](PlayerStats.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_teams**
> TeamList get_player_teams(player_id, offset=offset, limit=limit)

Retrieve all teams of a player

Retrieve all teams of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all teams of a player
    api_response = api_instance.get_player_teams(player_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**TeamList**](TeamList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_tournaments**
> TournamentsList get_player_tournaments(player_id, offset=offset, limit=limit)

Retrieve all tournaments of a player

Retrieve all tournaments of a player

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
api_instance = faceit_api.PlayersApi(faceit_api.ApiClient(configuration))
player_id = 'player_id_example' # str | The id of the player
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all tournaments of a player
    api_response = api_instance.get_player_tournaments(player_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlayersApi->get_player_tournaments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **player_id** | **str**| The id of the player | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**TournamentsList**](TournamentsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

