# Installing to bluemix container

1. After signing in to bluemix, head to the catalog section. Pick containers from the drawer menu in the Apps section.

2. Click on the 'upload an image' button

3. Follow the instructions

Alternative
1. Open command prompt or terminal. Install CloudFoundry CLI, Bluemix CLI and Docker CLI

2. Type in the following commands:
	- bluemix plugin install IBM-Containers -r Bluemix
	- bluemix login -a https://api.eu-gb.bluemix.net
	- bluemix ic init
 
3. Type in the setting you will be presented. They will look as follows:
	- set DOCKER_HOST=tcp://containers-api.eu-gb.bluemix.net:8443
	- set DOCKER_CERT_PATH=C:\Users\user\.ice\certs\containers-api.eu-gb.bluemix.net\9889...
	- set DOCKER_TLS_VERIFY=1
	
4. create a namespace

5. Open the Dockerfile and add the ip of the container to the variable ENV KAFKA_ADVERTISED_HOST_NAME "ip"

6. Use the following command to build this repo to a bluemix container

	- ## bx ic build -t namespace/kafka-docker ##
	
7. After the 27 steps of building and pushing to the container, open bluemix catalog. Go to the containers section in the app and click on your uploaded image.

8. Enter the image name and create the image. 

9. Your image will be running.

Test your installation using the python files attached. Change the ip's before you run them.

Done!!!


# Credit goes to https://github.com/mohamnag/docker-kafka-zookeeper
# Kafka & Zookeeper in one image
This image is **NOT** for production use but rather for testing purposes.

This is a sum of following two image:
 - https://github.com/wurstmeister/zookeeper-docker
 - https://github.com/wurstmeister/kafka-docker
 
So the credit goes mainly to their creators.

## Usage
This runs both Kafka and Zookeeper inside. Kafka is configured to use 
port `9092` internally and ZK the port `2181`. At least these two ports 
should be bound to host for external usage. If you bind the Kafka port 
to any other port on the host, you have to set the env variable 
`KAFKA_ADVERTISED_PORT` to that one.

The `KAFKA_ADVERTISED_HOST_NAME` has to be set to the host's name or IP
for Kafka to accept incoming connections.