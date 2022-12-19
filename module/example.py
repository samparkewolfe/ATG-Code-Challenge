from flask import Response

from RateLimiter import RateLimiter

@RateLimiter
def request():
    return Response("success", status=200, mimetype='application/json')

for i in range(1, 102):
    response = request()
    print(i, response.status, response.get_data())
