import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "vendor"))

import datetime as dt
import requests

apikey = ""
norad = input("NORAD ID:") or "33591"

fact = requests.get("https://uselessfacts.jsph.pl/api/v2/facts/random").json()
print("Did you know?", fact["text"])
print()

url = f"https://api.n2yo.com/rest/v1/satellite/radiopasses/{norad}/52.429/-1.887/0/2/11/&apiKey={apikey}"
data = requests.get(url).json()

info = data["info"]
passes = data["passes"]
sat_name = info["satname"]

print(f"Upcoming radio passes for {sat_name}:")
print()

if not passes:
    print("No passes found (check your API key or NORAD ID).")
else:
    for p in passes:
        start = dt.datetime.fromtimestamp(p["startUTC"], tz=dt.timezone.utc)
        print(f"  {start:%Y-%m-%d %H:%M UTC}   max elevation {p['maxEl']}°")
