# Division

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assets** | [**Assets**](Assets.md) |  | [optional] 
**config_type** | **str** | The type of the division. Can be nested or classic. Nested means that the division has tiers, classic is without tiers. | [optional] 
**leaderboard_config** | [**LeaderboardConfig**](LeaderboardConfig.md) |  | [optional] 
**leaderboards** | **list[str]** | The leaderboards of the division | [optional] 
**max_elo** | **int** | Max ELO for a user to be placed in this division after placement matches | [optional] 
**min_elo** | **int** | Min ELO for a user to be placed in this division after placement matches | [optional] 
**name** | **str** | The name of the division. | [optional] 
**tiers** | [**list[Tier]**](Tier.md) | The tiers of the division | [optional] 
**type** | **str** | The type of the division. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


