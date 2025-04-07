from kafka import KafkaConsumer, KafkaProducer
from kafka.admin import KafkaAdminClient, NewTopic
import golf_config as gc
import golf_kafka_config as gkc

# Initialize Kafka broker
admin_client = KafkaAdminClient(
    bootstrap_servers=gkc.ip_address
)

# Initialize producer
producer = KafkaProducer(bootstrap_servers=[gkc.ip_address])

# Create topics if they don't already exist
try:
    topics = [NewTopic(name=f'scorecard_{name}', num_partitions=1, replication_factor=1) for name in gc.golfer_names]
    admin_client.create_topics(new_topics=topics, validate_only=False)
except Exception as e:
    print(e)
    pass

def send_message_to_topic(message, topic):
    producer.send(topic, value=message)
    producer.flush()
    print('Sent ', message)



























# CONSUMER = KafkaConsumer(
#     'camden_topic',
#     bootstrap_servers=[ip_address],
#     auto_offset_reset='earliest')

# [print(f"Received message: {m.value}") for m in CONSUMER]

# CONSUMER.close()
# print("Consumer closed")