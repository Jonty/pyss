from datetime import datetime
import json

from flask import Flask, request, Response
import ephem

app = Flask(__name__)

@app.route('/')
def get_iss_position():
    now = datetime.utcnow()
    
    earth = ephem.Observer()
    earth.elevation = 80 # Meters
    earth.date = now
     
    tle_file = file('iss_tle.txt', 'r')
    iss_tle = tle_file.read().splitlines()
    tle_file.close()

    iss = ephem.readtle(*iss_tle)
    iss.compute(earth)

    response = json.dumps({
        'date': now.isoformat(),
        'lat':  iss.sublat,
        'long': iss.sublong
    })

    content_type = 'application/json'
    callback = request.args.get('callback', '')
    if callback:
        content_type = 'application/javascript'
        response = '%s(%s);' % (callback, response)

    resp = Response(response, content_type=content_type)
    return resp

if __name__ == '__main__':
    app.run()
