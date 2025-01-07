# Info

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessible_topology** | [**list[Topology]**](Topology.md) | AccessibleTopolgoy is the topology this volume is actually accessible from. | [optional] 
**capacity_bytes** | **int** | CapacityBytes is the capacity of the volume in bytes. A value of 0 indicates that the capacity is unknown. | [optional] 
**volume_context** | **dict(str, str)** | VolumeContext is the context originating from the CSI storage plugin when the Volume is created. | [optional] 
**volume_id** | **str** | VolumeID is the ID of the Volume as seen by the CSI storage plugin. This is distinct from the Volume&#39;s Swarm ID, which is the ID used by all of the Docker Engine to refer to the Volume. If this field is blank, then the Volume has not been successfully created yet. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


