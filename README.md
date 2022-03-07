# python-task-boilerplate
 Python Task boilerplate for datashop with Kafka ability

This is the boilerplate of Python task with Kafka communication ability for Datashop Project

### Post Configuration
```python
input_dict = request.get_json()
input_data = input_dict["dataFileURL"]
jobID = input_dict["jobID"]
kafka_URL = input_dict["kafkaBrokerURL"]
kafka_Group = input_dict["kafkaGroupId"]
kafka_Topic = input_dict["kafkaTopic"]
```

### Initial Kafka Producer
```python
producer = KafkaProducer(bootstrap_servers=input_kafka_URL)
```

### Sending Message
```python
producer.send(input_kafka_Topic, b'Job ' + str.encode(jobID) + b' Started.')
```