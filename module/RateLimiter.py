from flask import Response
import datetime

# Datetime helper
def deltaHours(timeA, timeB):
    duration = timeA - timeB
    duration = duration.total_seconds()
    hours = divmod(duration, 3600)[0]
    return hours

def rateLimiter(func):
    latestCallTimes = {}
    
    def wrapper(obj, uuid, timeOfCall = datetime.datetime.now()):
        nonlocal latestCallTimes
        
        now = datetime.datetime.now()
        
        if uuid in latestCallTimes:
            latestCallTimes[uuid] = [time for time in latestCallTimes[uuid] if deltaHours(now, time) < 1.]
        else:
            latestCallTimes[uuid] = []
        
        if (len(latestCallTimes[uuid]) < 100):
            latestCallTimes[uuid].append(timeOfCall)
            return func(obj)
        else:
            duration = now - latestCallTimes[uuid][0]
            duration = duration.total_seconds()
            secondsLeft = 3600 - duration
            
            return Response("Rate limit exceeded. Try again in {0} seconds".format(secondsLeft),
                            status=429,
                            mimetype='application/json')
    
    wrapper.cache_reset = lambda : latestCallTimes.clear()
    
    return wrapper
