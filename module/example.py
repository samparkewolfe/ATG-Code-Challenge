from flask import Response
import uuid
import datetime
import csv

from RateLimiter import rateLimiter

class Server():
    @rateLimiter
    def getResponse(self):
        return Response("success", status=200, mimetype='application/json')

class Client():
    def __init__(self):
        self.uuid = uuid.uuid4()

server = Server()
clients = [Client(), Client(), Client()]

with open('example.csv', 'w') as file:
    writer = csv.writer(file)
    for client in clients:
        for i in range(1, 102):
            response = server.getResponse(client.uuid)
            writer.writerow([datetime.datetime.now(), client.uuid, response.status, response.get_data()])
