# Google Play Scraper API

Google Play Scraper enables fast and efficient application data
extraction from Google Play, including title, price, version number,
download rates, reviews, and more. This short tutorial will show you how
to scrape Google Play using Oxylabs’ [<u>Scraper
API</u>](https://oxylabs.io/products/scraper-api).

## How it works

You can retrieve Google Play results by providing your target URLs and
forming a payload with job parameters. Our API will return the HTML of
any public Google Play page you have provided.

### Python code example

The following examples demonstrate how you can get Google Play results
in HTML format. To begin, you need to send the request to our API using
the
[<u>Push-Pull</u>](https://developers.oxylabs.io/scraper-apis/getting-started/integration-methods/push-pull)
method:

import requests

from pprint import pprint

\# Structure payload.

payload = {

'source': 'google',

'url': 'https://play.google.com/store/games?hl=en_GB&gl=UK',

'user_agent_type': 'desktop_edge',

'render': 'html',

'geo_location': 'United Kingdom',

'locale': 'en-gb'

}

\# Get response.

response = requests.request(

'POST',

'https://data.oxylabs.io/v1/queries',

auth=('USERNAME', 'PASSWORD'), \#Your credentials go here

json=payload

)

\# Instead of response with job status and results url, this will return
the

\# JSON response with results.

pprint(response.json())

Once the job is finished, you can then send another request to retrieve
the Google Play results. Here, you must use the **job ID** value that’s
provided in the response of the above code sample:

import requests

from pprint import pprint

\# Get response.

response = requests.request(

'GET',

'http://data.oxylabs.io/v1/queries/{job_id}/results',

auth=('USERNAME', 'PASSWORD')

)

\# This will return the JSON response with results.

pprint(response.json())

Visit our
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/google/url)
for more information.

### Output example

Here’s what the response in JSON format should look like after using the
above code sample:

{

"results": \[

{

"content": "\<!DOCTYPE html\>\<html lang=\\en\\
dir=\\ltr\\\>\<head\>\<meta http-equiv=\\origin-trial\\
content=\\Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRw...",

"created_at": "2023-08-28 14:14:59",

"updated_at": "2023-08-28 14:15:35",

"page": 1,

"url": "https://play.google.com/store/games?hl=en_GB&gl=US",

"job_id": "7101930169060862977",

"status_code": 200

}

\]

}

With Oxylabs’ Google Play Scraper API, the data extraction process is
as easy as it gets. Feel free to contact our 24/7 support team via live
chat or [<u>email</u>](mailto:support@oxylabs.io) if you need
assistance.
