from pymemcache.client import base


#Set the connection
elasticache_endpoint = 'PUT THE ELASTICACHE ENDPOINT HERE'
client = base.Client((elasticache_endpoint, 11211))

#set value
client.set('greeting', 'aloha world!')

#retrieve value
val = client.get('greeting')
print(val)