# faceit_api.TournamentsApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tournament**](TournamentsApi.md#get_tournament) | **GET** /tournaments/{tournament_id} | Retrieve tournament details
[**get_tournament_brackets**](TournamentsApi.md#get_tournament_brackets) | **GET** /tournaments/{tournament_id}/brackets | Retrieve brackets of a tournament
[**get_tournament_matches**](TournamentsApi.md#get_tournament_matches) | **GET** /tournaments/{tournament_id}/matches | Retrieve all matches of a tournament
[**get_tournament_teams**](TournamentsApi.md#get_tournament_teams) | **GET** /tournaments/{tournament_id}/teams | Retrieve all teams of a tournament
[**get_tournaments_list**](TournamentsApi.md#get_tournaments_list) | **GET** /tournaments | Retrieve tournaments v1 (no longer used)


# **get_tournament**
> Tournament get_tournament(tournament_id, expanded=expanded)

Retrieve tournament details

Retrieve tournament details

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
api_instance = faceit_api.TournamentsApi(faceit_api.ApiClient(configuration))
tournament_id = 'tournament_id_example' # str | The id of the tournament
expanded = ['expanded_example'] # list[str] | List of entity names to expand in request (optional)

try:
    # Retrieve tournament details
    api_response = api_instance.get_tournament(tournament_id, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournament: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **str**| The id of the tournament | 
 **expanded** | [**list[str]**](str.md)| List of entity names to expand in request | [optional] 

### Return type

[**Tournament**](Tournament.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tournament_brackets**
> Brackets get_tournament_brackets(tournament_id)

Retrieve brackets of a tournament

Retrieve brackets of a tournament

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
api_instance = faceit_api.TournamentsApi(faceit_api.ApiClient(configuration))
tournament_id = 'tournament_id_example' # str | The id of the tournament

try:
    # Retrieve brackets of a tournament
    api_response = api_instance.get_tournament_brackets(tournament_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournament_brackets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **str**| The id of the tournament | 

### Return type

[**Brackets**](Brackets.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tournament_matches**
> MatchList get_tournament_matches(tournament_id, offset=offset, limit=limit)

Retrieve all matches of a tournament

Retrieve all matches of a tournament

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
api_instance = faceit_api.TournamentsApi(faceit_api.ApiClient(configuration))
tournament_id = 'tournament_id_example' # str | The id of the tournament
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all matches of a tournament
    api_response = api_instance.get_tournament_matches(tournament_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournament_matches: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **str**| The id of the tournament | 
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

# **get_tournament_teams**
> TournamentTeams get_tournament_teams(tournament_id, offset=offset, limit=limit)

Retrieve all teams of a tournament

Retrieve all teams of a tournament

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
api_instance = faceit_api.TournamentsApi(faceit_api.ApiClient(configuration))
tournament_id = 'tournament_id_example' # str | The id of the tournament
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all teams of a tournament
    api_response = api_instance.get_tournament_teams(tournament_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournament_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tournament_id** | **str**| The id of the tournament | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**TournamentTeams**](TournamentTeams.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tournaments_list**
> TournamentsList get_tournaments_list(game=game, region=region, offset=offset, limit=limit)

Retrieve tournaments v1 (no longer used)

Retrieve tournaments v1 (no longer used). Please refer to the Championships controller to retrieve tournaments v2

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
api_instance = faceit_api.TournamentsApi(faceit_api.ApiClient(configuration))
game = 'game_example' # str | A game on FACEIT (optional)
region = 'region_example' # str | A region of the game (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve tournaments v1 (no longer used)
    api_response = api_instance.get_tournaments_list(game=game, region=region, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TournamentsApi->get_tournaments_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **game** | **str**| A game on FACEIT | [optional] 
 **region** | **str**| A region of the game | [optional] 
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

