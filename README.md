# Kafka-ELK
1.STEP
docker-compose -f elasticsearch-kibana-docker-compose.yaml up

2.STEP
docker-compose -f kafka-docker-compose.yaml up

3.STEP
Installing Logstash to Ubuntu host nad configuration.
apt install logstash
add pipeline.conf to /etc/logstash/conf.d/ directory.
start logstash service.

4.STEP
Go to https://192.168.1.48:9000 and Create Kafka cluster and Topic.

5.STEP
Go to Kibana and create Index Pattern named "registered-user".

6.STEP
Run python code which logging "Hello World" to Kafka. (I use Python for Logging Application)

7.STEP
Go to Kibana Dashboard.

![1111](https://github.com/huseynadm/Kafka-ELK/assets/98022012/63be66cc-bf41-42e3-b3a1-cf40361d0f32)
