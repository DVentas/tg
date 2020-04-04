from flask import Flask
from flask import request
import json
import datetime
from postgis_util import PostgisUtil


app = Flask(__name__)
postgisUtil = PostgisUtil()

def event_converter(o):
    if isinstance(o, datetime.datetime):
        return o.__str__()

@app.route("/near-events/", methods=['GET'])
def near_events():
    latitude = float(request.args.get('latitude'))
    longitude = float(request.args.get('longitude'))
    date = request.args.get('date', None)
    if date is None:
        date = datetime.datetime.now().__format__("%Y%m%d")
    events = postgisUtil.getEvents(latitude, longitude, date)
    return json.dumps(events, default = event_converter)


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=8080)
