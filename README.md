# faceit-api
# This API provide access to FACEIT's data

This Python package is automatically generated by the [Swagger Codegen](https://github.com/swagger-api/swagger-codegen) project:

- API version: 4
- Package version: 1.0.0
- Build package: io.swagger.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import faceit_api 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import faceit_api
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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
api_instance = faceit_api.ChampionshipsApi(faceit_api.ApiClient(configuration))
championship_id = 'championship_id_example' # str | The id of the championship
expanded = ['expanded_example'] # list[str] | List of entity names to expand in request (optional)

try:
    # Retrieve championship details
    api_response = api_instance.get_championship(championship_id, expanded=expanded)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ChampionshipsApi->get_championship: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://open.faceit.com/data/v4*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChampionshipsApi* | [**get_championship**](docs/ChampionshipsApi.md#get_championship) | **GET** /championships/{championship_id} | Retrieve championship details
*ChampionshipsApi* | [**get_championship_matches**](docs/ChampionshipsApi.md#get_championship_matches) | **GET** /championships/{championship_id}/matches | Retrieve all matches of a championship
*ChampionshipsApi* | [**get_championship_results**](docs/ChampionshipsApi.md#get_championship_results) | **GET** /championships/{championship_id}/results | Retrieve all results of a championship
*ChampionshipsApi* | [**get_championship_subscriptions**](docs/ChampionshipsApi.md#get_championship_subscriptions) | **GET** /championships/{championship_id}/subscriptions | Retrieve all subscriptions of a championship
*ChampionshipsApi* | [**get_championships**](docs/ChampionshipsApi.md#get_championships) | **GET** /championships | Retrieve all championships of a game
*GamesApi* | [**get_all_games**](docs/GamesApi.md#get_all_games) | **GET** /games | Retrieve details of all games on FACEIT
*GamesApi* | [**get_game**](docs/GamesApi.md#get_game) | **GET** /games/{game_id} | Retrieve game details
*GamesApi* | [**get_game_matchmakings**](docs/GamesApi.md#get_game_matchmakings) | **GET** /games/{gameId}/matchmakings | Retrieve details of all matchmakings of a game on FACEIT
*GamesApi* | [**get_parent_game**](docs/GamesApi.md#get_parent_game) | **GET** /games/{game_id}/parent | Retrieve the details of the parent game, if the game is region-specific
*GamesApi* | [**get_queue_bans**](docs/GamesApi.md#get_queue_bans) | **GET** /games/{game_id}/queues/{queue_id}/bans | Retrieve queue bans on FACEIT
*GamesApi* | [**get_queue_by_id**](docs/GamesApi.md#get_queue_by_id) | **GET** /games/{game_id}/queues/{queue_id} | Retrieve details of a queue on FACEIT
*GamesApi* | [**get_queues_by_entity_filters**](docs/GamesApi.md#get_queues_by_entity_filters) | **GET** /games/{game_id}/queues | Retrieve queues by filters on FACEIT
*GamesApi* | [**get_queues_by_region**](docs/GamesApi.md#get_queues_by_region) | **GET** /games/{game_id}/regions/{region_id}/queues | Retrieve queues by region on FACEIT
*HubsApi* | [**get_hub**](docs/HubsApi.md#get_hub) | **GET** /hubs/{hub_id} | Retrieve hub details
*HubsApi* | [**get_hub_matches**](docs/HubsApi.md#get_hub_matches) | **GET** /hubs/{hub_id}/matches | Retrieve all matches of a hub
*HubsApi* | [**get_hub_members**](docs/HubsApi.md#get_hub_members) | **GET** /hubs/{hub_id}/members | Retrieve all members of a hub
*HubsApi* | [**get_hub_roles**](docs/HubsApi.md#get_hub_roles) | **GET** /hubs/{hub_id}/roles | Retrieve all roles members can have in a hub
*HubsApi* | [**get_hub_rules**](docs/HubsApi.md#get_hub_rules) | **GET** /hubs/{hub_id}/rules | Retrieve rules of a hub
*HubsApi* | [**get_hub_stats**](docs/HubsApi.md#get_hub_stats) | **GET** /hubs/{hub_id}/stats | Retrieve statistics of a hub
*LeaderboardsApi* | [**get_championship_group_ranking**](docs/LeaderboardsApi.md#get_championship_group_ranking) | **GET** /leaderboards/championships/{championship_id}/groups/{group} | Retrieve group ranking of a championship
*LeaderboardsApi* | [**get_championship_leaderboards**](docs/LeaderboardsApi.md#get_championship_leaderboards) | **GET** /leaderboards/championships/{championship_id} | Retrieve all leaderboards of a championship
*LeaderboardsApi* | [**get_hub_leaderboards**](docs/LeaderboardsApi.md#get_hub_leaderboards) | **GET** /leaderboards/hubs/{hub_id} | Retrieve all leaderboards of a hub
*LeaderboardsApi* | [**get_hub_ranking**](docs/LeaderboardsApi.md#get_hub_ranking) | **GET** /leaderboards/hubs/{hub_id}/general | Retrieve all time ranking of a hub
*LeaderboardsApi* | [**get_hub_season_ranking**](docs/LeaderboardsApi.md#get_hub_season_ranking) | **GET** /leaderboards/hubs/{hub_id}/seasons/{season} | Retrieve seasonal ranking of a hub
*LeaderboardsApi* | [**get_leaderboard**](docs/LeaderboardsApi.md#get_leaderboard) | **GET** /leaderboards/{leaderboard_id} | Retrieve ranking from a leaderboard id
*LeaderboardsApi* | [**get_player_ranking_in_leaderboard**](docs/LeaderboardsApi.md#get_player_ranking_in_leaderboard) | **GET** /leaderboards/{leaderboard_id}/players/{player_id} | Retrieve a players ranking in a leaderboard
*LeaguesApi* | [**get_league_by_id**](docs/LeaguesApi.md#get_league_by_id) | **GET** /leagues/{league_id} | Retrieve details of a league of a matchmaking on FACEIT
*LeaguesApi* | [**get_league_season**](docs/LeaguesApi.md#get_league_season) | **GET** /leagues/{league_id}/seasons/{season_id} | Retrieve details of a season of a league on FACEIT
*LeaguesApi* | [**get_player_for_league_season**](docs/LeaguesApi.md#get_player_for_league_season) | **GET** /leagues/{league_id}/seasons/{season_id}/players/{player_id} | Retrieve details of a player for a given league and season on FACEIT
*MatchesApi* | [**get_match**](docs/MatchesApi.md#get_match) | **GET** /matches/{match_id} | Retrieve match details
*MatchesApi* | [**get_match_stats**](docs/MatchesApi.md#get_match_stats) | **GET** /matches/{match_id}/stats | Retrieve statistics of a match
*MatchmakingsApi* | [**get_matchmaking**](docs/MatchmakingsApi.md#get_matchmaking) | **GET** /matchmakings/{matchmaking_id} | Retrieve details of a matchmaking of a game on FACEIT
*OrganizersApi* | [**get_organizer**](docs/OrganizersApi.md#get_organizer) | **GET** /organizers/{organizer_id} | Retrieve organizer details
*OrganizersApi* | [**get_organizer_by_name**](docs/OrganizersApi.md#get_organizer_by_name) | **GET** /organizers | Retrieve organizer details from name
*OrganizersApi* | [**get_organizer_championships**](docs/OrganizersApi.md#get_organizer_championships) | **GET** /organizers/{organizer_id}/championships | Retrieve all championships of an organizer
*OrganizersApi* | [**get_organizer_games**](docs/OrganizersApi.md#get_organizer_games) | **GET** /organizers/{organizer_id}/games | Retrieve all games an organizer is involved with
*OrganizersApi* | [**get_organizer_hubs**](docs/OrganizersApi.md#get_organizer_hubs) | **GET** /organizers/{organizer_id}/hubs | Retrieve all hubs of an organizer
*OrganizersApi* | [**get_organizer_tournaments**](docs/OrganizersApi.md#get_organizer_tournaments) | **GET** /organizers/{organizer_id}/tournaments | Retrieve all tournaments of an organizer
*PlayersApi* | [**get_player**](docs/PlayersApi.md#get_player) | **GET** /players/{player_id} | Retrieve player details
*PlayersApi* | [**get_player_bans**](docs/PlayersApi.md#get_player_bans) | **GET** /players/{player_id}/bans | Retrieve all bans of a player
*PlayersApi* | [**get_player_from_lookup**](docs/PlayersApi.md#get_player_from_lookup) | **GET** /players | Retrieve player details
*PlayersApi* | [**get_player_history**](docs/PlayersApi.md#get_player_history) | **GET** /players/{player_id}/history | Retrieve all matches of a player
*PlayersApi* | [**get_player_hubs**](docs/PlayersApi.md#get_player_hubs) | **GET** /players/{player_id}/hubs | Retrieve all hubs of a player
*PlayersApi* | [**get_player_stats**](docs/PlayersApi.md#get_player_stats) | **GET** /players/{player_id}/games/{game_id}/stats | Retrieve statistics of a player for a given amount of matches
*PlayersApi* | [**get_player_stats_0**](docs/PlayersApi.md#get_player_stats_0) | **GET** /players/{player_id}/stats/{game_id} | Retrieve statistics of a player
*PlayersApi* | [**get_player_teams**](docs/PlayersApi.md#get_player_teams) | **GET** /players/{player_id}/teams | Retrieve all teams of a player
*PlayersApi* | [**get_player_tournaments**](docs/PlayersApi.md#get_player_tournaments) | **GET** /players/{player_id}/tournaments | Retrieve all tournaments of a player
*RankingsApi* | [**get_global_ranking**](docs/RankingsApi.md#get_global_ranking) | **GET** /rankings/games/{game_id}/regions/{region} | Retrieve global ranking of a game
*RankingsApi* | [**get_player_ranking**](docs/RankingsApi.md#get_player_ranking) | **GET** /rankings/games/{game_id}/regions/{region}/players/{player_id} | Retrieve user position in the global ranking of a game
*SearchApi* | [**search_championships**](docs/SearchApi.md#search_championships) | **GET** /search/championships | Search for championships
*SearchApi* | [**search_clans**](docs/SearchApi.md#search_clans) | **GET** /search/clans | Search for clans
*SearchApi* | [**search_hubs**](docs/SearchApi.md#search_hubs) | **GET** /search/hubs | Search for hubs
*SearchApi* | [**search_organizers**](docs/SearchApi.md#search_organizers) | **GET** /search/organizers | Search for organizers
*SearchApi* | [**search_players**](docs/SearchApi.md#search_players) | **GET** /search/players | Search for players
*SearchApi* | [**search_teams**](docs/SearchApi.md#search_teams) | **GET** /search/teams | Search for teams
*SearchApi* | [**search_tournaments**](docs/SearchApi.md#search_tournaments) | **GET** /search/tournaments | Search for tournaments
*TeamsApi* | [**get_team**](docs/TeamsApi.md#get_team) | **GET** /teams/{team_id} | Retrieve team details
*TeamsApi* | [**get_team_stats**](docs/TeamsApi.md#get_team_stats) | **GET** /teams/{team_id}/stats/{game_id} | Retrieve statistics of a team
*TeamsApi* | [**get_team_tournaments**](docs/TeamsApi.md#get_team_tournaments) | **GET** /teams/{team_id}/tournaments | Retrieve tournaments of a team
*TournamentsApi* | [**get_tournament**](docs/TournamentsApi.md#get_tournament) | **GET** /tournaments/{tournament_id} | Retrieve tournament details
*TournamentsApi* | [**get_tournament_brackets**](docs/TournamentsApi.md#get_tournament_brackets) | **GET** /tournaments/{tournament_id}/brackets | Retrieve brackets of a tournament
*TournamentsApi* | [**get_tournament_matches**](docs/TournamentsApi.md#get_tournament_matches) | **GET** /tournaments/{tournament_id}/matches | Retrieve all matches of a tournament
*TournamentsApi* | [**get_tournament_teams**](docs/TournamentsApi.md#get_tournament_teams) | **GET** /tournaments/{tournament_id}/teams | Retrieve all teams of a tournament
*TournamentsApi* | [**get_tournaments_list**](docs/TournamentsApi.md#get_tournaments_list) | **GET** /tournaments | Retrieve tournaments v1 (no longer used)


## Documentation For Models

 - [AccessMode](docs/AccessMode.md)
 - [Address](docs/Address.md)
 - [AlgorithmParameters](docs/AlgorithmParameters.md)
 - [Assets](docs/Assets.md)
 - [AuthenticateOKBody](docs/AuthenticateOKBody.md)
 - [Availability](docs/Availability.md)
 - [Band](docs/Band.md)
 - [BirthDate](docs/BirthDate.md)
 - [Brackets](docs/Brackets.md)
 - [BracketsFaction](docs/BracketsFaction.md)
 - [BracketsMatch](docs/BracketsMatch.md)
 - [BracketsRound](docs/BracketsRound.md)
 - [CapacityRange](docs/CapacityRange.md)
 - [Championship](docs/Championship.md)
 - [ChampionshipBounds](docs/ChampionshipBounds.md)
 - [ChampionshipPlacement](docs/ChampionshipPlacement.md)
 - [ChampionshipPlacementGroup](docs/ChampionshipPlacementGroup.md)
 - [ChampionshipResultList](docs/ChampionshipResultList.md)
 - [ChampionshipSchedule](docs/ChampionshipSchedule.md)
 - [ChampionshipScreening](docs/ChampionshipScreening.md)
 - [ChampionshipStream](docs/ChampionshipStream.md)
 - [ChampionshipSubscription](docs/ChampionshipSubscription.md)
 - [ChampionshipSubscriptionsList](docs/ChampionshipSubscriptionsList.md)
 - [ChampionshipsList](docs/ChampionshipsList.md)
 - [ChangeType](docs/ChangeType.md)
 - [CheckIn](docs/CheckIn.md)
 - [ClanSearch](docs/ClanSearch.md)
 - [ClansSearchList](docs/ClansSearchList.md)
 - [ClusterVolume](docs/ClusterVolume.md)
 - [ClusterVolumeSpec](docs/ClusterVolumeSpec.md)
 - [CompetitionSearch](docs/CompetitionSearch.md)
 - [CompetitionsSearchList](docs/CompetitionsSearchList.md)
 - [ContainerTopOKBody](docs/ContainerTopOKBody.md)
 - [ContainerUpdateOKBody](docs/ContainerUpdateOKBody.md)
 - [CreateOptions](docs/CreateOptions.md)
 - [CreateResponse](docs/CreateResponse.md)
 - [DeleteResponse](docs/DeleteResponse.md)
 - [DetailedMatchResult](docs/DetailedMatchResult.md)
 - [Division](docs/Division.md)
 - [EntityRanking](docs/EntityRanking.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [Faction](docs/Faction.md)
 - [FactionResult](docs/FactionResult.md)
 - [FilesystemChange](docs/FilesystemChange.md)
 - [Game](docs/Game.md)
 - [GameAssets](docs/GameAssets.md)
 - [GameDetail](docs/GameDetail.md)
 - [GameUserSearch](docs/GameUserSearch.md)
 - [GamesList](docs/GamesList.md)
 - [GeoDescription](docs/GeoDescription.md)
 - [GeoLabel](docs/GeoLabel.md)
 - [GlobalRanking](docs/GlobalRanking.md)
 - [GlobalRankingList](docs/GlobalRankingList.md)
 - [GraphDriverData](docs/GraphDriverData.md)
 - [HistoryFaction](docs/HistoryFaction.md)
 - [HistoryResponseItem](docs/HistoryResponseItem.md)
 - [Hub](docs/Hub.md)
 - [HubMembers](docs/HubMembers.md)
 - [HubSmall](docs/HubSmall.md)
 - [HubStats](docs/HubStats.md)
 - [HubUser](docs/HubUser.md)
 - [HubsList](docs/HubsList.md)
 - [HubsSmallList](docs/HubsSmallList.md)
 - [IdResponse](docs/IdResponse.md)
 - [Info](docs/Info.md)
 - [Item](docs/Item.md)
 - [ItemList](docs/ItemList.md)
 - [ItemMedia](docs/ItemMedia.md)
 - [JoinCheck](docs/JoinCheck.md)
 - [JoinType](docs/JoinType.md)
 - [Leaderboard](docs/Leaderboard.md)
 - [LeaderboardConfig](docs/LeaderboardConfig.md)
 - [LeaderboardsList](docs/LeaderboardsList.md)
 - [League](docs/League.md)
 - [ListResponse](docs/ListResponse.md)
 - [Match](docs/Match.md)
 - [MatchHistory](docs/MatchHistory.md)
 - [MatchHistoryList](docs/MatchHistoryList.md)
 - [MatchHistoryPlayer](docs/MatchHistoryPlayer.md)
 - [MatchList](docs/MatchList.md)
 - [MatchResult](docs/MatchResult.md)
 - [MatchStats](docs/MatchStats.md)
 - [Matchmaking](docs/Matchmaking.md)
 - [MatchmakingList](docs/MatchmakingList.md)
 - [MatchmakingQueue](docs/MatchmakingQueue.md)
 - [MatchmakingSlim](docs/MatchmakingSlim.md)
 - [Meta](docs/Meta.md)
 - [Order](docs/Order.md)
 - [OrderItem](docs/OrderItem.md)
 - [OrderList](docs/OrderList.md)
 - [OrderUser](docs/OrderUser.md)
 - [Organizer](docs/Organizer.md)
 - [OrganizerSearch](docs/OrganizerSearch.md)
 - [OrganizersSearchList](docs/OrganizersSearchList.md)
 - [PaginationFields](docs/PaginationFields.md)
 - [Placement](docs/Placement.md)
 - [Player](docs/Player.md)
 - [PlayerBan](docs/PlayerBan.md)
 - [PlayerBansList](docs/PlayerBansList.md)
 - [PlayerGlobalRanking](docs/PlayerGlobalRanking.md)
 - [PlayerInLeague](docs/PlayerInLeague.md)
 - [PlayerStats](docs/PlayerStats.md)
 - [PlayerStatsForMatch](docs/PlayerStatsForMatch.md)
 - [PlayerStatsForMatchesList](docs/PlayerStatsForMatchesList.md)
 - [PlayerStatsSimple](docs/PlayerStatsSimple.md)
 - [Plugin](docs/Plugin.md)
 - [PluginConfig](docs/PluginConfig.md)
 - [PluginConfigArgs](docs/PluginConfigArgs.md)
 - [PluginConfigInterface](docs/PluginConfigInterface.md)
 - [PluginConfigLinux](docs/PluginConfigLinux.md)
 - [PluginConfigNetwork](docs/PluginConfigNetwork.md)
 - [PluginConfigRootfs](docs/PluginConfigRootfs.md)
 - [PluginConfigUser](docs/PluginConfigUser.md)
 - [PluginDevice](docs/PluginDevice.md)
 - [PluginEnv](docs/PluginEnv.md)
 - [PluginInterfaceType](docs/PluginInterfaceType.md)
 - [PluginMount](docs/PluginMount.md)
 - [PluginSettings](docs/PluginSettings.md)
 - [Port](docs/Port.md)
 - [Prize](docs/Prize.md)
 - [Promotion](docs/Promotion.md)
 - [PublishState](docs/PublishState.md)
 - [PublishStatus](docs/PublishStatus.md)
 - [Queue](docs/Queue.md)
 - [QueueAlgorithm](docs/QueueAlgorithm.md)
 - [QueueBan](docs/QueueBan.md)
 - [QueueBansList](docs/QueueBansList.md)
 - [QueueSimple](docs/QueueSimple.md)
 - [QueuesList](docs/QueuesList.md)
 - [Ranking](docs/Ranking.md)
 - [Relegation](docs/Relegation.md)
 - [Role](docs/Role.md)
 - [RolesList](docs/RolesList.md)
 - [Roster](docs/Roster.md)
 - [RoundStats](docs/RoundStats.md)
 - [Rules](docs/Rules.md)
 - [Scope](docs/Scope.md)
 - [Season](docs/Season.md)
 - [SeasonDetailed](docs/SeasonDetailed.md)
 - [Secret](docs/Secret.md)
 - [ServiceCreateResponse](docs/ServiceCreateResponse.md)
 - [ServiceUpdateResponse](docs/ServiceUpdateResponse.md)
 - [SharingMode](docs/SharingMode.md)
 - [SpacePlayer](docs/SpacePlayer.md)
 - [Stats](docs/Stats.md)
 - [StatsCompetitionPlayer](docs/StatsCompetitionPlayer.md)
 - [StatsSkillLevel](docs/StatsSkillLevel.md)
 - [StatsSkillLevelRange](docs/StatsSkillLevelRange.md)
 - [SubstitutionConfiguration](docs/SubstitutionConfiguration.md)
 - [Summary](docs/Summary.md)
 - [Team](docs/Team.md)
 - [TeamList](docs/TeamList.md)
 - [TeamSearch](docs/TeamSearch.md)
 - [TeamStats](docs/TeamStats.md)
 - [TeamStatsSimple](docs/TeamStatsSimple.md)
 - [TeamsSearchList](docs/TeamsSearchList.md)
 - [Tier](docs/Tier.md)
 - [Topology](docs/Topology.md)
 - [TopologyRequirement](docs/TopologyRequirement.md)
 - [Tournament](docs/Tournament.md)
 - [TournamentSimple](docs/TournamentSimple.md)
 - [TournamentTeam](docs/TournamentTeam.md)
 - [TournamentTeams](docs/TournamentTeams.md)
 - [TournamentsList](docs/TournamentsList.md)
 - [TypeBlock](docs/TypeBlock.md)
 - [TypeMount](docs/TypeMount.md)
 - [UsageData](docs/UsageData.md)
 - [UserSearch](docs/UserSearch.md)
 - [UserSettings](docs/UserSettings.md)
 - [UserSimple](docs/UserSimple.md)
 - [UsersSearchList](docs/UsersSearchList.md)
 - [Version](docs/Version.md)
 - [Volume](docs/Volume.md)
 - [WaitExitError](docs/WaitExitError.md)
 - [WaitResponse](docs/WaitResponse.md)


## Documentation For Authorization


## key

- **Type**: API key
- **API key parameter name**: Authorization
- **Location**: HTTP header


## Author



