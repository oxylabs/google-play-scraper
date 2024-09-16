# Google Play Scraper

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

[Google Play Scraper](https://oxylabs.io/products/scraper-api/serp/google) enables fast and efficient application data
extraction from Google Play, including title, price, version number,
download rates, reviews, and more. This short tutorial will show you how
to scrape Google Play using Oxylabs’ [<u>Scraper
API</u>](https://oxylabs.io/products/scraper-api).

## Free Google Play Scraper

A free tool used to get data for apps, books or movies from Google Play for a provided search query.

### Prerequisites

To run this tool, you need to have Python 3.11 installed in your system.

### Installation

Open up a terminal window, navigate to this repository and run this command:

```make install```

### Scraping Google Play

To scrape data from Google Play, first choose one of these categories, that are available in Google Play:

- `apps`
- `movies`
- `books`

The default category in the tool is `apps`, so feel free to omit the `CATEGORY` parameter from the command if that's the category you need.

If you prefer to choose a different category than `Apps`, run this command in your terminal:

```make scrape QUERY="<your_query>" CATEGORY="<your_chosen_category>```

Otherwise, the command should look like this:

```make scrape QUERY="<your_query>"```

Make sure the category is in lowercase. 


For this example, let's try scraping Google Play results for movies about fishing. The command should look something like this:

```make scrape QUERY="fishing" CATEGORY="movies"```

Make sure to enclose your query and category in quotation marks, otherwise the tool might have trouble parsing it.

After running the command, your terminal should look something like this:

<img width="845" alt="image" src="https://github.com/user-attachments/assets/622cda14-820c-42ec-810b-f099b5561dbf">

After the tool has finished running, you should see a file named `movies_play_items.csv` in your current directory.

This file contains Google Play items for the query and category you entered. 

The file name will always be in this format: `{category}_play_items.csv`.

The generated CSV file contains these columns of data:

- `title` - The title of the movie.
- `price` - The price of the movie to rent.
- `rating` - The rating of the movie.
- `cover_url` - The URL to the image of the cover for the movie.
- `url` - The URL for the movie.

Here's an example of how the data can look like:

<img width="982" alt="image" src="https://github.com/user-attachments/assets/066e25bf-c4e8-4144-95bf-942453dd484f">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Scrape Google Play data with Oxylabs Scraper API

You can retrieve Google Play results by providing your target URLs and
forming a payload with job parameters. Our API will return the HTML of
any public Google Play page you have provided.

### Python code example

The following examples demonstrate how you can get Google Play results
in HTML format. To begin, you need to send the request to our API using
the
[<u>Push-Pull</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/integration-methods/push-pull)
method:

```python
import requests
from pprint import pprint

# Structure payload.
payload = {
   'source': 'google',
   'url': 'https://play.google.com/store/games?hl=en_GB&gl=UK',
   'user_agent_type': 'desktop_edge',
   'render': 'html',
   'geo_location': 'United Kingdom',
   'locale': 'en-gb'
}

# Get response.
response = requests.request(
    'POST',
    'https://data.oxylabs.io/v1/queries',
    auth=('USERNAME', 'PASSWORD'), #Your credentials go here
    json=payload
)

# Instead of response with job status and results url, this will return the
# JSON response with results.
pprint(response.json())
```

Once the job is finished, you can then send another request to retrieve
the Google Play results. Here, you must use the **job ID** value that’s
provided in the response of the above code sample:

```python
import requests
from pprint import pprint

# Get response.
response = requests.request(
    'GET',
    'http://data.oxylabs.io/v1/queries/{job_id}/results',
    auth=('USERNAME', 'PASSWORD')
)

# This will return the JSON response with results.
pprint(response.json())
```

Visit our
[<u>documentation</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/google/url)
for more information.

### Output example

The response will be in JSON format, containing HTML content and details about the job itself:

```json
{
  "results": [
    {
      "content": "<!DOCTYPE html><html lang=\"en\" dir=\"ltr\"><head><meta http-equiv=\"origin-trial\" content=\"Az520Inasey3TAyqLyojQa8MnmCALSEU29yQFW8dePZ7xQTvSt73pHazLFTK5f7SyLUJSo2uKLesEtEa9aUYcgMAAACPeyJvcmlnaW4iOiJodHRw...",
      "created_at": "2023-08-28 14:14:59",
      "updated_at": "2023-08-28 14:15:35",
      "page": 1,
      "url": "https://play.google.com/store/games?hl=en_GB&gl=US",
      "job_id": "7101930169060862977",
      "status_code": 200
    }
  ]
}
```

With Oxylabs’ Google Play Scraper API, the data extraction process is
as easy as it gets. Feel free to contact our 24/7 support team via live
chat or [<u>email</u>](mailto:support@oxylabs.io) if you need
assistance.

Read More Google Scraping Related Repositories: [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How to Scrape Google Shopping Results](https://github.com/oxylabs/scrape-google-shopping), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights), [How To Scrape Google Images](https://github.com/oxylabs/how-to-scrape-google-images), [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)
