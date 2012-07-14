#!/bin/env python
import re
import requests
import ephem

request = requests.get(
    'http://spaceflight.nasa.gov/realdata/sightings/SSapplications/Post/JavaSSOP/orbit/ISS/SVPOST.html'
)

iss_traj = request.content
m = re.search('\n\s+(ISS)\n\s+(1 .*?)\n\s+(2 .*?)\n', iss_traj)

# Attempt to parse the TLE, this will chuck an exception if its invalid
ephem.readtle(m.group(1), m.group(2), m.group(3))

iss_tle = file('iss_tle.txt', 'w')
for i in range(1,4):
    iss_tle.write(m.group(i) + '\n')
iss_tle.close()

print "ISS TLE Successfully updated"
