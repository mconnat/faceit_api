# faceit_api.LeaderboardsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_championship_group_ranking**](LeaderboardsApi.md#get_championship_group_ranking) | **GET** /leaderboards/championships/{championship_id}/groups/{group} | Retrieve group ranking of a championship
[**get_championship_leaderboards**](LeaderboardsApi.md#get_championship_leaderboards) | **GET** /leaderboards/championships/{championship_id} | Retrieve all leaderboards of a championship
[**get_hub_leaderboards**](LeaderboardsApi.md#get_hub_leaderboards) | **GET** /leaderboards/hubs/{hub_id} | Retrieve all leaderboards of a hub
[**get_hub_ranking**](LeaderboardsApi.md#get_hub_ranking) | **GET** /leaderboards/hubs/{hub_id}/general | Retrieve all time ranking of a hub
[**get_hub_season_ranking**](LeaderboardsApi.md#get_hub_season_ranking) | **GET** /leaderboards/hubs/{hub_id}/seasons/{season} | Retrieve seasonal ranking of a hub
[**get_leaderboard**](LeaderboardsApi.md#get_leaderboard) | **GET** /leaderboards/{leaderboard_id} | Retrieve ranking from a leaderboard id
[**get_player_ranking_in_leaderboard**](LeaderboardsApi.md#get_player_ranking_in_leaderboard) | **GET** /leaderboards/{leaderboard_id}/players/{player_id} | Retrieve a players ranking in a leaderboard


# **get_championship_group_ranking**
> EntityRanking get_championship_group_ranking(championship_id, group, offset=offset, limit=limit)

Retrieve group ranking of a championship

Retrieve group ranking of a championship

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
group = 56 # int | A group of the championship
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve group ranking of a championship
    api_response = api_instance.get_championship_group_ranking(championship_id, group, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_championship_group_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
 **group** | **int**| A group of the championship | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**EntityRanking**](EntityRanking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_championship_leaderboards**
> LeaderboardsList get_championship_leaderboards(championship_id, offset=offset, limit=limit)

Retrieve all leaderboards of a championship

Retrieve all leaderboards of a championship

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all leaderboards of a championship
    api_response = api_instance.get_championship_leaderboards(championship_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_championship_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **championship_id** | **str**| The id of the championship | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**LeaderboardsList**](LeaderboardsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_leaderboards**
> LeaderboardsList get_hub_leaderboards(hub_id, offset=offset, limit=limit)

Retrieve all leaderboards of a hub

Retrieve all leaderboards of a hub

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all leaderboards of a hub
    api_response = api_instance.get_hub_leaderboards(hub_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_hub_leaderboards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**LeaderboardsList**](LeaderboardsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_ranking**
> EntityRanking get_hub_ranking(hub_id, offset=offset, limit=limit)

Retrieve all time ranking of a hub

Retrieve all time ranking of a hub

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all time ranking of a hub
    api_response = api_instance.get_hub_ranking(hub_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_hub_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**EntityRanking**](EntityRanking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_hub_season_ranking**
> EntityRanking get_hub_season_ranking(hub_id, season, offset=offset, limit=limit)

Retrieve seasonal ranking of a hub

Retrieve seasonal ranking of a hub

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
hub_id = 'hub_id_example' # str | The id of the hub
season = 56 # int | A season of the hub
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve seasonal ranking of a hub
    api_response = api_instance.get_hub_season_ranking(hub_id, season, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_hub_season_ranking: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_id** | **str**| The id of the hub | 
 **season** | **int**| A season of the hub | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**EntityRanking**](EntityRanking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_leaderboard**
> EntityRanking get_leaderboard(leaderboard_id, offset=offset, limit=limit)

Retrieve ranking from a leaderboard id

Retrieve ranking from a leaderboard id

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
leaderboard_id = 'leaderboard_id_example' # str | The id of the leaderboard
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve ranking from a leaderboard id
    api_response = api_instance.get_leaderboard(leaderboard_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **str**| The id of the leaderboard | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**EntityRanking**](EntityRanking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_player_ranking_in_leaderboard**
> Ranking get_player_ranking_in_leaderboard(leaderboard_id, player_id)

Retrieve a players ranking in a leaderboard

Retrieve a players ranking in a leaderboard

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
api_instance = faceit_api.LeaderboardsApi(faceit_api.ApiClient(configuration))
leaderboard_id = 'leaderboard_id_example' # str | The id of the leaderboard
player_id = 'player_id_example' # str | The id of the player

try:
    # Retrieve a players ranking in a leaderboard
    api_response = api_instance.get_player_ranking_in_leaderboard(leaderboard_id, player_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LeaderboardsApi->get_player_ranking_in_leaderboard: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **leaderboard_id** | **str**| The id of the leaderboard | 
 **player_id** | **str**| The id of the player | 

### Return type

[**Ranking**](Ranking.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

