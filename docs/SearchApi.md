# faceit_api.SearchApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**search_championships**](SearchApi.md#search_championships) | **GET** /search/championships | Search for championships
[**search_clans**](SearchApi.md#search_clans) | **GET** /search/clans | Search for clans
[**search_hubs**](SearchApi.md#search_hubs) | **GET** /search/hubs | Search for hubs
[**search_organizers**](SearchApi.md#search_organizers) | **GET** /search/organizers | Search for organizers
[**search_players**](SearchApi.md#search_players) | **GET** /search/players | Search for players
[**search_teams**](SearchApi.md#search_teams) | **GET** /search/teams | Search for teams
[**search_tournaments**](SearchApi.md#search_tournaments) | **GET** /search/tournaments | Search for tournaments


# **search_championships**
> CompetitionsSearchList search_championships(name, game=game, region=region, type=type, offset=offset, limit=limit)

Search for championships

Search for championships

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of a championship on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
region = 'region_example' # str | A region of the game (optional)
type = 'type_example' # str | Kind of competitions to return (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for championships
    api_response = api_instance.search_championships(name, game=game, region=region, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_championships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a championship on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **region** | **str**| A region of the game | [optional] 
 **type** | **str**| Kind of competitions to return | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**CompetitionsSearchList**](CompetitionsSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_clans**
> ClansSearchList search_clans(name, game=game, region=region, offset=offset, limit=limit)

Search for clans

Search for clans

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of a clan on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
region = 'region_example' # str | A region of the game (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for clans
    api_response = api_instance.search_clans(name, game=game, region=region, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_clans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a clan on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **region** | **str**| A region of the game | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**ClansSearchList**](ClansSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_hubs**
> CompetitionsSearchList search_hubs(name, game=game, region=region, offset=offset, limit=limit)

Search for hubs

Search for hubs

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of a hub on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
region = 'region_example' # str | A region of the game (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for hubs
    api_response = api_instance.search_hubs(name, game=game, region=region, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_hubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a hub on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **region** | **str**| A region of the game | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**CompetitionsSearchList**](CompetitionsSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_organizers**
> OrganizersSearchList search_organizers(name, offset=offset, limit=limit)

Search for organizers

Search for organizers

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of a organizer on FACEIT
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for organizers
    api_response = api_instance.search_organizers(name, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_organizers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a organizer on FACEIT | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**OrganizersSearchList**](OrganizersSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_players**
> UsersSearchList search_players(nickname, game=game, country=country, offset=offset, limit=limit)

Search for players

Search for players

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
nickname = 'nickname_example' # str | The nickname of a player on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
country = 'country_example' # str | A country code (ISO 3166-1) (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for players
    api_response = api_instance.search_players(nickname, game=game, country=country, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_players: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nickname** | **str**| The nickname of a player on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **country** | **str**| A country code (ISO 3166-1) | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**UsersSearchList**](UsersSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_teams**
> TeamsSearchList search_teams(nickname, game=game, offset=offset, limit=limit)

Search for teams

Search for teams

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
nickname = 'nickname_example' # str | The nickname of a team on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for teams
    api_response = api_instance.search_teams(nickname, game=game, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_teams: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **nickname** | **str**| The nickname of a team on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**TeamsSearchList**](TeamsSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_tournaments**
> CompetitionsSearchList search_tournaments(name, game=game, region=region, type=type, offset=offset, limit=limit)

Search for tournaments

Search for tournaments

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
api_instance = faceit_api.SearchApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of a tournament on FACEIT
game = 'game_example' # str | A game on FACEIT (optional)
region = 'region_example' # str | A region of the game (optional)
type = 'type_example' # str | Kind of competitions to return (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Search for tournaments
    api_response = api_instance.search_tournaments(name, game=game, region=region, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->search_tournaments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of a tournament on FACEIT | 
 **game** | **str**| A game on FACEIT | [optional] 
 **region** | **str**| A region of the game | [optional] 
 **type** | **str**| Kind of competitions to return | [optional] 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**CompetitionsSearchList**](CompetitionsSearchList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

