#!/bin/env python
import requests
import ephem

request = requests.get(
    'http://www.celestrak.com/NORAD/elements/stations.txt'
)

tles = request.content.splitlines()
while tles:
    if tles[0].startswith('ISS (ZARYA)'):
        break
    tles.pop(0)

# Attempt to parse the TLE, this will chuck an exception if its invalid
ephem.readtle(*tles[0:3])

iss_tle = file('iss_tle.txt', 'w')
iss_tle.write('\n'.join(tles[0:3]))
iss_tle.close()

print "ISS TLE Successfully updated"
