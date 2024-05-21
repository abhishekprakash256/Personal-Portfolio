import redis

r = redis.Redis(host='localhost', port=6379, db=0)

#r.hset('test-hash','name', 'Alice')
#r.hset('test-hash','name2','Tom')

r.delete('test-hash')

#print(r.hget('test-hash','name').decode())
#print(r.hget('test-hash','name2').decode())