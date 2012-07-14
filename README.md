Pyss
====
A tiny JSON server that tells you where the International Space Station is.

Usage
=====
To get a JSON response containing the current latitude/longitude of the ISS, hit `localhost:5000` ([Demo URL](http://jonty.co.uk/bits/pyss))

    {"date": "2012-07-14T17:53:54.895522", "lat": 0.21487978100776672, "long": 2.6722369194030762}

To get a JSONP response, just specify the callback: `localhost:5000?callback=aFunctionName` ([Demo URL](http://jonty.co.uk/bits/pyss?callback=aFunctionName))

    aFunctionName({"date": "2012-07-14T17:53:54.895522", "lat": 0.21487978100776672, "long": 2.6722369194030762});

The ISS occasionally changes orbit, so you'll need to update the [TLE](http://en.wikipedia.org/wiki/Two-line_element_set) occasionally. A convenience utility named `update_iss_tle.py` is provided for this. 

Installing
==========
* `pip install -r requirements.txt` to get the dependencies installed
* `python pyss.py` to start a server running on http://localhost:5000
* You'll probably want to proxy it via Nginx or similar rather than serving it from flask directly
* Set up a cronjob to run `update_iss_tle.py` daily, or the position information will gradually become incorrect
