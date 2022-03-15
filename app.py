# The Boilerplate is created based on existing Python Project: Background-Removal (Manas Palaparthi)
# Background-Removal Git: https://github.com/ashith-cloud/background-removal
from flask import Flask, request, after_this_request
from flask_restful import Resource, Api
from kafka import KafkaProducer
import os, shutil
import json
import time

app = Flask(__name__)
api = Api(app)


class Predict(Resource):
    @staticmethod
    def post():
        try:
            input_dict = request.get_json()

            input_data = input_dict["dataFileURL"]
            jobID = input_dict["jobID"]
            kafka_URL = input_dict["kafkaBrokerURL"]
            kafka_Group = input_dict["kafkaGroupId"]
            kafka_Topic = input_dict["kafkaTopic"]

            if "".__eq__(kafka_URL) and "".__eq__(kafka_Group) and "".__eq__(kafka_Topic):
                return "ERROR NO KAFKA CONFIGURATION"

            # 1 Initial Kafka Connection and Send message
            producer = KafkaProducer(bootstrap_servers=kafka_URL)

            # 2 Send Esential Job Stauts to Kafka
            producer.send(kafka_Topic, b'Job ' + str.encode(jobID) + b' Started.')

            # 3 DOING YOUR FUNCTION
            time.sleep(5)

            # 4 Update Jobstatus again when finished.
            producer.send(kafka_Topic, b'Job ' + str.encode(jobID) + b' Finished.')

            # Quit Kafka
            producer.close()

        except Exception as e:
            return "ERROR"


api.add_resource(Predict, '/predict')


def localTest():
    kafka_URL = "localhost:9092"
    kafka_Group = "DataShop-Test"
    kafka_Topic = "JobStatus-Test"

    if "".__eq__(kafka_URL) and "".__eq__(kafka_Group) and "".__eq__(kafka_Topic):
        print("ERROR NO KAFKA CONFIGURATION")

    # 1 Initial Kafka Connection and Send message
    producer = KafkaProducer(bootstrap_servers=kafka_URL)

    # 2 Send Esential Job Stauts to Kafka
    message = {
        "insightFileURL": "Dummy String for insightFileURL",
        "jobid": "622ff7c2d257c6b8b6f0a3e4",
        "jobStatus": "success"
    }
    producer.send(kafka_Topic, str.encode(json.dumps(message)))

    # Quit Kafka
    producer.close()


if __name__ == '__main__':
    # app.run()
    localTest()
