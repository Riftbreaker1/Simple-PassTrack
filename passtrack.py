import pandas as pd
import plotly.express as px
import requests
import time
import math
from datetime import datetime, timezone

apikey = ""
norad = input("NORAD ID:")
if norad == "":
    norad = "33591"

print("https://api.n2yo.com/rest/v1/satellite/radiopasses/" + norad + "/52.429/-1.887/" + "0/2/11/&apiKey=" + apikey)

response = requests.get("https://api.n2yo.com/rest/v1/satellite/radiopasses/" + norad + "/52.429/-1.887/" + "0/2/11/&apiKey=" + apikey)
data = response.json()

passes = data["passes"]
max_elevations = [p["maxEl"] for p in passes]
start_utcs = [p["startUTC"] for p in passes]

start_datetimes = pd.to_datetime(start_utcs, unit='s')

fig = px.scatter(x=start_datetimes, y=max_elevations,
                  labels={"x": "Pass Time (UTC)", "y": "Max Elevation (°)"})
fig.show()
