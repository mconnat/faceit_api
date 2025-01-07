# faceit_api.OrganizersApi

All URIs are relative to *https://open.faceit.com/data/v4*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organizer**](OrganizersApi.md#get_organizer) | **GET** /organizers/{organizer_id} | Retrieve organizer details
[**get_organizer_by_name**](OrganizersApi.md#get_organizer_by_name) | **GET** /organizers | Retrieve organizer details from name
[**get_organizer_championships**](OrganizersApi.md#get_organizer_championships) | **GET** /organizers/{organizer_id}/championships | Retrieve all championships of an organizer
[**get_organizer_games**](OrganizersApi.md#get_organizer_games) | **GET** /organizers/{organizer_id}/games | Retrieve all games an organizer is involved with
[**get_organizer_hubs**](OrganizersApi.md#get_organizer_hubs) | **GET** /organizers/{organizer_id}/hubs | Retrieve all hubs of an organizer
[**get_organizer_tournaments**](OrganizersApi.md#get_organizer_tournaments) | **GET** /organizers/{organizer_id}/tournaments | Retrieve all tournaments of an organizer


# **get_organizer**
> Organizer get_organizer(organizer_id)

Retrieve organizer details

Retrieve organizer details

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
organizer_id = 'organizer_id_example' # str | The id of the organizer

try:
    # Retrieve organizer details
    api_response = api_instance.get_organizer(organizer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizer_id** | **str**| The id of the organizer | 

### Return type

[**Organizer**](Organizer.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizer_by_name**
> Organizer get_organizer_by_name(name)

Retrieve organizer details from name

Retrieve organizer details from name

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
name = 'name_example' # str | The name of the organizer

try:
    # Retrieve organizer details from name
    api_response = api_instance.get_organizer_by_name(name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer_by_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| The name of the organizer | 

### Return type

[**Organizer**](Organizer.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizer_championships**
> ChampionshipsList get_organizer_championships(organizer_id, offset=offset, limit=limit)

Retrieve all championships of an organizer

Retrieve all championships of an organizer

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
organizer_id = 'organizer_id_example' # str | The id of the organizer
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all championships of an organizer
    api_response = api_instance.get_organizer_championships(organizer_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer_championships: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizer_id** | **str**| The id of the organizer | 
 **offset** | **int**| The starting item position | [optional] [default to 0]
 **limit** | **int**| The number of items to return | [optional] [default to 20]

### Return type

[**ChampionshipsList**](ChampionshipsList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizer_games**
> GamesList get_organizer_games(organizer_id)

Retrieve all games an organizer is involved with

Retrieve all games an organizer is involved with

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
organizer_id = 'organizer_id_example' # str | The id of the organizer

try:
    # Retrieve all games an organizer is involved with
    api_response = api_instance.get_organizer_games(organizer_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer_games: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizer_id** | **str**| The id of the organizer | 

### Return type

[**GamesList**](GamesList.md)

### Authorization

[key](../README.md#key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organizer_hubs**
> HubsList get_organizer_hubs(organizer_id, offset=offset, limit=limit)

Retrieve all hubs of an organizer

Retrieve all hubs of an organizer

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
organizer_id = 'organizer_id_example' # str | The id of the organizer
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 50 # int | The number of items to return (optional) (default to 50)

try:
    # Retrieve all hubs of an organizer
    api_response = api_instance.get_organizer_hubs(organizer_id, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer_hubs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizer_id** | **str**| The id of the organizer | 
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

# **get_organizer_tournaments**
> TournamentsList get_organizer_tournaments(organizer_id, type=type, offset=offset, limit=limit)

Retrieve all tournaments of an organizer

Retrieve all tournaments of an organizer

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
api_instance = faceit_api.OrganizersApi(faceit_api.ApiClient(configuration))
organizer_id = 'organizer_id_example' # str | The id of the organizer
type = 'type_example' # str | Kind of tournament. Can be upcoming(default) or past (optional)
offset = 0 # int | The starting item position (optional) (default to 0)
limit = 20 # int | The number of items to return (optional) (default to 20)

try:
    # Retrieve all tournaments of an organizer
    api_response = api_instance.get_organizer_tournaments(organizer_id, type=type, offset=offset, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrganizersApi->get_organizer_tournaments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organizer_id** | **str**| The id of the organizer | 
 **type** | **str**| Kind of tournament. Can be upcoming(default) or past | [optional] 
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

