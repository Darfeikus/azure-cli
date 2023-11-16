# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps  # pylint: disable=unused-import
# pylint: disable=line-too-long, too-many-lines

helps['redis'] = """
type: group
short-summary: Manage dedicated Redis caches for your Azure applications.
"""

helps['redis create'] = """
type: command
short-summary: Create new Redis Cache instance.
parameters:
  - name: --redis-configuration
    short-summary: A json file used to set redis-configuration settings. You may encounter parse errors if the json file is invalid.
    long-summary: |
        Usage: --redis-configuration @"{config_file.json}"

        An example json file for configuring max-memory policies
        [
          {
            "maxmemory-policy": "allkeys-lru"
          }
        ]

        An example json file for enabling the RDB back up data persistence is
        [
          {
            "rdb-storage-connection-string": "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=myAccountKey;EndpointSuffix=core.windows.net",
            "rdb-backup-enabled": "true",
            "rdb-backup-frequency": "15",
            "rdb-backup-max-snapshot-count": "1"
          }
        ]

        An example json file for enabling the AOF back up data persistence is
        [
          {
            "aof-backup-enabled": "true",
            "aof-storage-connection-string-0": "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=myAccountKey;EndpointSuffix=core.windows.net",
            "aof-storage-connection-string-1": "DefaultEndpointsProtocol=https;AccountName=mystorageaccount;AccountKey=myAccountKey;EndpointSuffix=core.windows.net"
          }
        ]

        The content for a json file for configuring Microsoft Entra Authentication is
        {
        "aad-enabled": "true",
        }
                
examples:
  - name: Create new Redis Cache instance. (autogenerated)
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Basic --vm-size c0
    crafted: true
  - name: Configure the multiple zones for new Premium Azure Cache for Redis
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --zones 1 2
    crafted: true
  - name: Configure the memory policies for the cache.
    text: az redis create --resource-group resourceGroupName --name cacheName --location westus2 --sku Standard --vm-size c0 --redis-configuration @"config_max-memory.json"
    crafted: true
  - name: Configure and enable the RDB back up data persistence for new Premium Azure Cache for Redis.
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --redis-configuration @"config_rdb.json"
    crafted: true
  - name: Configure and enable the AOF back up data persistence for new Premium Azure Cache for Redis
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --redis-configuration @"config_aof.json"
    crafted: true
  - name: Create a Premium Azure Cache for Redis with clustering enabled
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --shard-count 2
    crafted: true
  - name: Deploying a Premium Azure Cache for Redis inside an existing Azure Virtual Network
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --subnet-id "/subscriptions/{subid}/resourceGroups/{resourceGroupName}/providers/Microsoft.{Network|ClassicNetwork}/virtualNetworks/vnet1/subnets/subnet1"
    crafted: true
  - name: Deploying a Premium Azure Cache for Redis with Microsoft Entra Authentication configured
    text: az redis create --location westus2 --name MyRedisCache --resource-group MyResourceGroup --sku Premium --vm-size p1 --redis-configuration @"config_enable-aad.json"
    crafted: true    
"""

helps['redis export'] = """
type: command
short-summary: Export data stored in a Redis cache.
examples:
  - name: Use managed identity to export cache data
    text: az redis export -n testCacheName -g testResourceGroup --prefix examplePrefix --container containerUrl  --preferred-data-archive-auth-method ManagedIdentity
    crafted: true
"""

helps['redis firewall-rules'] = """
type: group
short-summary: Manage Redis firewall rules.
"""

helps['redis firewall-rules create'] = """
type: command
short-summary: Create a redis cache firewall rule.
long-summary: Usage example - az redis firewall-rules create --name testCacheName --resource-group testResourceGroup  --start-ip 10.10.10.10 --end-ip 20.20.20.20 --rule-name 10to20
"""

helps['redis firewall-rules update'] = """
type: command
short-summary: Update a redis cache firewall rule.
"""

helps['redis import'] = """
type: command
short-summary: Import data into a Redis cache.
examples:
  - name: Use managed identity to import cache data
    text: az redis import -n testCacheName -g testResourceGroup --files blobUrl --preferred-data-archive-auth-method ManagedIdentity
    crafted: true
"""

helps['redis list'] = """
type: command
short-summary: List Redis Caches.
long-summary: Lists details about all caches within current Subscription or provided Resource Group.
"""

helps['redis patch-schedule'] = """
type: group
short-summary: Manage Redis patch schedules.
"""

helps['redis patch-schedule create'] = """
type: command
short-summary: Create patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule create --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis patch-schedule update'] = """
type: command
short-summary: Update the patching schedule for Redis cache.
long-summary: Usage example - az redis patch-schedule update --name testCacheName --resource-group testResourceGroup --schedule-entries '[{"dayOfWeek":"Tuesday","startHourUtc":"00","maintenanceWindow":"PT5H"}]'
"""

helps['redis server-link'] = """
type: group
short-summary: Manage Redis server links.
"""

helps['redis server-link create'] = """
type: command
short-summary: Adds a server link to the Redis cache (requires Premium SKU).
long-summary: Usage example - az redis server-link create --name testCacheName --resource-group testResourceGroup --cache-to-link secondTestCacheName --replication-role Secondary
"""

helps['redis update'] = """
type: command
short-summary: Update a Redis cache.
long-summary: Scale or update settings of a Redis cache.
examples:
  - name: Update the maxmemory-policy for your Azure Cache for Redis named MyRedisCache
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set "redisConfiguration.maxmemory-policy"="allkeys-lru"
    crafted: true
  - name: Disable the RDB back up data persistence for Premium Azure Cache for Redis
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set "redisConfiguration.rdb-backup-enabled"="false"
    crafted: true
  - name: Configure the RDB back up enabled data persistence for already created Premium Azure Cache for Redis
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set "redisConfiguration.rdb-storage-connection-string"="BlobEndpoint=https//..." "redisConfiguration.rdb-backup-enabled"="true" "redisConfiguration.rdb-backup-frequency"="15" "redisConfiguration.rdb-backup-max-snapshot-count"="1"
    crafted: true
  - name: Scale an Azure Cache for Redis Instance - Update to different size (An example to scale from c0 to c1).
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set "sku.capacity"="2"
    crafted: true
  - name: Scale an Azure Cache for Redis Instance - Update to different tier (From Basic to Standard or Standard to Premium).
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set "sku.name"="Premium" "sku.capacity"="1" "sku.family"="P"
    crafted: true
  - name: Scale an Azure Cache for Redis Instance - Enable Clustering.
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set shardCount=1
    crafted: true
  - name: Scale an Azure Cache for Redis Instance in/out using Redis Cluster.
    text: az redis update --name MyRedisCache --resource-group MyResourceGroup --set shardCount=2
    crafted: true
"""

helps['redis force-reboot'] = """
type: command
short-summary: Reboot specified Redis node(s).
long-summary: Usage example - az redis force-reboot --name testCacheName --resource-group testResourceGroup --reboot-type {AllNodes, PrimaryNode, SecondaryNode}  [--shard-id]
"""

helps['redis import-method'] = """
type: command
short-summary: Import data into Redis cache.
long-summary: Usage example - az redis import-method --name testCacheName --resource-group testResourceGroup --files [--file-format]
"""

helps['redis patch-schedule delete'] = """
type: command
short-summary: Deletes the patching schedule of a redis cache.
long-summary: Usage example - az redis patch-schedule delete --name testCacheName --resource-group testResourceGroup
"""

helps['redis patch-schedule show'] = """
type: command
short-summary: Gets the patching schedule of a redis cache.
long-summary: Usage example - az redis patch-schedule show --name testCacheName --resource-group testResourceGroup [--query-examples]
"""

helps['redis regenerate-keys'] = """
type: command
short-summary: Regenerate Redis cache's access keys.
long-summary: Usage example - az redis regenerate-keys --name testCacheName --resource-group testResourceGroup --key-type {Primary, Secondary}
"""

helps['redis identity'] = """
type: group
short-summary: Manage identity assigned to Azure cache for Redis.
"""

helps['redis identity assign'] = """
type: command
short-summary: Assign identity for Azure cache for Redis.
"""

helps['redis identity remove'] = """
type: command
short-summary: Remove the identity already assigned for Azure cache for Redis.
"""

helps['redis identity show'] = """
type: command
short-summary: Show the identity assigned for Azure cache for Redis.
"""

helps['redis access-policy'] = """
type: group
short-summary: Manage access policies for Redis Cache
"""

helps['redis access-policy create'] = """
type: group
short-summary: Adds an access policy to the Redis Cache
"""

helps['redis access-policy update'] = """
type: group
short-summary: Updates an access policy of the Redis Cache
"""

helps['redis access-policy delete'] = """
type: group
short-summary: Deletes an access policy from the Redis Cache
"""

helps['redis access-policy show'] = """
type: group
short-summary: Gets the detailed information about an access policy of the Redis Cache
"""

helps['redis access-policy list'] = """
type: group
short-summary: Gets the list of access policies associated with the Redis Cache
"""