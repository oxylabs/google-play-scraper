from pprint import pprint

import requests


# Structure payload.
payload = {
    "source": "google",
    "url": "https://play.google.com/store/games?hl=en_GB&gl=UK",
    "user_agent_type": "desktop_edge",
    "render": "html",
    "geo_location": "United Kingdom",
    "locale": "en-gb",
}

# Get response.
response = requests.request(
    "POST",
    "https://data.oxylabs.io/v1/queries",
    auth=("USERNAME", "PASSWORD"),  # Your credentials go here
    json=payload,
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
