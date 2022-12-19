from flask import Response
import datetime

# Datetime helper
def deltaHours(timeA, timeB):
    duration = timeA - timeB
    duration = duration.total_seconds()
    hours = divmod(duration, 3600)[0]
    return hours

def RateLimiter(func):
    latestCallTimes = []
    
    def wrapper(timeOfCall = datetime.datetime.now()):
        nonlocal latestCallTimes
        
        now = datetime.datetime.now()
        latestCallTimes = [time for time in latestCallTimes if deltaHours(now, time) < 1.]
        
        if (len(latestCallTimes) < 100):
            latestCallTimes.append(timeOfCall)
            return func()
        else:
            duration = now - latestCallTimes[0]
            duration = duration.total_seconds()
            secondsLeft = 3600 - duration
            
            return Response("Rate limit exceeded. Try again in {0} seconds".format(secondsLeft),
                            status=429,
                            mimetype='application/json')

    return wrapper
