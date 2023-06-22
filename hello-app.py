from kafka import KafkaProducer
import logging
import time

# Set up Kafka producer
producer = KafkaProducer(bootstrap_servers='192.168.1.48:9092')

# Set up logger
logger = logging.getLogger('kafka_logger')
logger.setLevel(logging.INFO)

# Create a custom handler to send logs to Kafka
class KafkaLogHandler(logging.Handler):
    def emit(self, record):
        log_message = self.format(record)
        producer.send('registered_user', value=log_message.encode())

# Create an instance of the custom handler
kafka_handler = KafkaLogHandler()

# Add the Kafka handler to the logger
logger.addHandler(kafka_handler)

# Log "Hello World" every 1 second
while True:
    logger.info('Hello World')
    time.sleep(1)

# Close the Kafka producer (Note: This will not be reached in an infinite loop scenario)
producer.close()
