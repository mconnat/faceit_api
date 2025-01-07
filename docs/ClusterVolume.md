# ClusterVolume

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**created_at** | **datetime** |  | [optional] 
**id** | **str** | ID is the Swarm ID of the volume. Because cluster volumes are Swarm objects, they have an ID, unlike non-cluster volumes, which only have a Name. This ID can be used to refer to the cluster volume. | [optional] 
**info** | [**Info**](Info.md) |  | [optional] 
**publish_status** | [**list[PublishStatus]**](PublishStatus.md) | PublishStatus contains the status of the volume as it pertains to its publishing on Nodes. | [optional] 
**spec** | [**ClusterVolumeSpec**](ClusterVolumeSpec.md) |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**version** | [**Version**](Version.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


