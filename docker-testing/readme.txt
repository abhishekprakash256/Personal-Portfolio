docker build -t flask-hello-world .

docker run -p 5000:5000 flask-hello-world

docker run --name flask-hello-world-2 --network my_network -p 5000:5000 flask-hello-world-2

mac commands 
brew services info mongodb-community
brew services stop mongodb-community
brew services stop redis


running container 
docker network create my_network
docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest
docker run -d --name redis --network my_network -p 6379:6379 redis:latest
docker run -d --name flask-app --network my_network -p 5000:5000 flask-app



steps- 

1. Change the clinet to --
    - client = MongoClient('mongo', 27017, serverSelectionTimeoutMS=2000)  # 2-second timeout
    -  client = redis.Redis(host='redis', port=6379, db=0, decode_responses=True)

2. Create the network 
    - docker network create my_network

3. For running the container 
    - run the redis and the mongo conatiner using the commands
        docker run -d --name mongo --network my_network -p 27017:27017 mongo:latest
        docker run -d --name redis --network my_network -p 6379:6379 redis:latest


4. To build the docker file 
    - docker build -t personal-website .

5. Run the flask container as 
    docker run -d --name personal-website --network my_network -p 5000:5000 personal-website





docker build -t personal-website .



#port binding was the problem 