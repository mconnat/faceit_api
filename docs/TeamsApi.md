# faceit_api.TeamsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_team**](TeamsApi.md#get_team) | **GET** /teams/{team_id} | Retrieve team details
[**get_team_stats**](TeamsApi.md#get_team_stats) | **GET** /teams/{team_id}/stats/{game_id} | Retrieve statistics of a team
[**get_team_tournaments**](TeamsApi.md#get_team_tournaments) | **GET** /teams/{team_id}/tournaments | Retrieve tournaments of a team


# **get_team**
> Team get_team(team_id)

Retrieve team details

Retrieve team details

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
api_instance = faceit_api.TeamsApi(faceit_api.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team

try:
    # Retrieve team details
    api_response = api_instance.get_team(team_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 

### Return type

[**Team**](Team.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_stats**
> TeamStats get_team_stats(team_id, game_id)

Retrieve statistics of a team

Retrieve statistics of a team

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
api_instance = faceit_api.TeamsApi(faceit_api.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team
game_id = 'game_id_example' # str | A game on FACEIT

try:
    # Retrieve statistics of a team
    api_response = api_instance.get_team_stats(team_id, game_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_stats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
 **game_id** | **str**| A game on FACEIT | 

### Return type

[**TeamStats**](TeamStats.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_team_tournaments**
> TournamentsList get_team_tournaments(team_id, offset=offset, limit=limit)

Retrieve tournaments of a team

Retrieve tournaments of a team

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
api_instance = faceit_api.TeamsApi(faceit_api.ApiClient(configuration))
team_id = 'team_id_example' # str | The id of the team
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve tournaments of a team
    api_response = api_instance.get_team_tournaments(team_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TeamsApi->get_team_tournaments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **team_id** | **str**| The id of the team | 
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

