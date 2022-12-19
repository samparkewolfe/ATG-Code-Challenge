# AT Code Challenge

I made this solution using TDD in Python inside a Jupyter Notebook.

Inside the Jupyter Notebook you can see the solution and the tests which I used to develop it.

I then moved the code into a python file so that it can be imported into an example python script inside the `module/` directory.

To run the example just use this command.
```
python example.py
```

You can also see at the top of the jupyter notebook a cell containing web links to things I had to research and learn while implementing.

## Reasoning behind the implementation 

I used a decorator pattern because it is very clean and I wanted to ensure maximum modularisation between the function which was being rate limited and the rate limiter itself. I would not want to see lots of rate limiter code around a function which has nothing to do with rate limiting.

I took inspiration from this [RateLimiter](https://pypi.org/project/ratelimiter/)'s interface.

The rate limiting algorithm itself is quite safe from a memory perspective in that it only ever stores the number of allowed calls in memory.

## Possible limitations
One limitation is that it can only be tested using one hours worth of requests because all requests over an hour old are not considered by the algorithm. This meant that I was only able to test the solution first returning a 200 and then returning a 429 when it was over requested. I couldn't test receiving 200's, then 429's and then back to 200's after an hour.

I believe that having a decorator pattern limits the object oriented-ness of the solution since I did not make the rate limiter itself an object. Because it holds a cache, it will be unclear to users the life cycle of this memory and will be hard to know when it is created and deleted.

The decorator pattern I also believe might causes issues because the cache can not be overridden making the function it is attached to have to be re-created in order to fully reset the cache.

I would have liked to extend the interface of the RateLimiter to match the other cases of the [RateLimiter](https://pypi.org/project/ratelimiter/) I took inspiration from. The state which the solution is in now, I do not think it would be very easy to extend the implementation to these interfaces. It would be better if I modularised the rate limiting functionality rather that writing it all inside the decorator `wrapper` function.

I also wasn't able to test the "seconds left" feature in the body of the response because by the time the value is passed to the test it is in the middle of a wordy string.

The algorithm itself could also be more efficient since an entirely new copy of the cache is made for every call when filtering times later than an hour. With some more time this could be optimised possibly using an iterator.
