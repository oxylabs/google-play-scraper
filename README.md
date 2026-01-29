# Google Play Scraper

[![Oxylabs promo code](https://raw.githubusercontent.com/oxylabs/google-news-scraper/refs/heads/main/Scrape%20Google%20data%20with%20Web%20Scraper%20API.png)](https://oxylabs.io/products/scraper-api/serp/google?utm_source=877&utm_medium=affiliate&groupid=877&utm_content=google-play-scraper-github&transaction_id=102c8d36f7f0d0e5797b8f26152160)

[![](https://dcbadge.limes.pink/api/server/Pds3gBmKMH?style=for-the-badge&theme=discord)](https://discord.gg/Pds3gBmKMH) [![YouTube](https://img.shields.io/badge/YouTube-Oxylabs-red?style=for-the-badge&logo=youtube&logoColor=white)](https://www.youtube.com/@oxylabs)

This tutorial will show you how to gather public data from the Google Play store, including data points like title, price, version number, download rates, reviews, and more. In this repository, you can find a free Google Play scraper tool, designed for smaller-scale scraping tasks. If you want to increase your scraping scale, the second part of this guide will show you how to utilize a far more effective Oxylabs' [Scraper API](https://oxylabs.io/products/scraper-api). It comes with a **free trial**, which you can claim by registering a free account on the [dashboard](https://dashboard.oxylabs.io/).

- [Free Google Play Scraper](#free-google-play-scraper)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Scraping Google Play](#scraping-google-play)
    + [1. Select a category:](#1-select-a-category)
    + [2. Use a search keyword:](#2-use-a-search-keyword)
  * [Notes](#notes)
- [Scrape Google Play data with Oxylabs Scraper API](#scrape-google-play-data-with-oxylabs-scraper-api)
  * [Python code example](#python-code-example)
  * [Output example](#output-example)

## Free Google Play Scraper

A free tool which you can use to get data for apps, books, or movies from Google Play using a specific search query.

### Prerequisites

To run this tool, you need to have Python `3.11` or later installed on your system.

### Installation

Open up a terminal window, navigate to this repository, and run this command:

```make install```

### Scraping Google Play

#### 1. Select a category:

To scrape data from Google Play, first choose one of these categories, that are available in Google Play:

- `apps`
- `movies`
- `books`

The default category in the tool is `apps`, so feel free to omit the `CATEGORY` parameter from the command if that's the category you need. 

If you prefer to choose a different category than `apps`, run this command in your terminal:

```bash
make scrape QUERY="<your_query>" CATEGORY="<your_chosen_category>
```

Otherwise, the command should look like this:

```bash
make scrape QUERY="<your_query>"
```

> [!NOTE]
> Make sure the category name is in **lowercase**. 


#### 2. Use a search keyword:

For this example, let's try scraping Google Play results for movies about fishing. The command should look like this:

```bash
make scrape QUERY="fishing" CATEGORY="movies"
```

> [!NOTE]
> Make sure to enclose your query and category in quotation marks. Otherwise, the tool might have trouble parsing it.

After running the command, you should see a similar output in your terminal:

<img width="845" alt="image" src="https://github.com/user-attachments/assets/622cda14-820c-42ec-810b-f099b5561dbf">

After the tool finishes running, you can find a file named `movies_play_items.csv` in your current working directory. This file contains Google Play items for the query and category you entered. The file name will always be in this format: `{category}_play_items.csv`. The generated CSV file contains these columns of data:

- `title` - The title of the movie.
- `price` - The price of the movie to rent.
- `rating` - The rating of the movie.
- `cover_url` - The URL to the image of the cover for the movie.
- `url` - The URL for the movie.

Here's an example of how the scraped and parsed data should look like:

<img width="982" alt="image" src="https://github.com/user-attachments/assets/066e25bf-c4e8-4144-95bf-942453dd484f">

### Notes

In case the code doesn't work or your project is of bigger scale, please refer to the second part of the tutorial. There, we showcase how to scrape public data with Oxylabs Scraper API.

## Scrape Google Play data with Oxylabs Scraper API

After purchasing access to the API or claiming your free trial, you'll have to use your API credentials for authentication.

You can retrieve Google Play results by providing your target URLs and
forming a `payload` with job parameters. [Scraper API](https://oxylabs.io/products/scraper-api) will return the **HTML** of
any public Google Play page you have provided.

### Python code example

The following examples demonstrate how you can get Google Play results
in HTML format. To begin, you need to send the request to the API using
the
[<u>Push-Pull</u>](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/integration-methods/push-pull)
method (or [other methods](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/integration-methods)):

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

# This will return a JSON response with job information and results URLs.
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

# This will return a JSON response with scraped results.
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
To get parsed results, use the free [Custom Parser](https://developers.oxylabs.io/scraper-apis/serp-scraper-api/features/custom-parser) feature. Check out this in-depth [Custom Parser tutorial](https://github.com/oxylabs/custom-parser-instructions) to learn how to use it.

You can also request Markdown output by using `"markdown: true"` flag to get an easy-to-read result format for various workloads and AI tools.

With Oxylabs’ Google Play Scraper API, the data extraction process is
as easy as it gets. Feel free to contact our 24/7 support team via live
chat or [<u>email</u>](mailto:support@oxylabs.io) if you need
assistance.

Read More Google Scraping Related Repositories: [Google Sheets for Basic Web Scraping](https://github.com/oxylabs/web-scraping-google-sheets), [How To Scrape Google Jobs](https://github.com/oxylabs/how-to-scrape-google-jobs), [Google News Scrpaer](https://github.com/oxylabs/google-news-scraper), [How to Scrape Google Scholar](https://github.com/oxylabs/how-to-scrape-google-scholar), [How to Scrape Google Flights with Python](https://github.com/oxylabs/how-to-scrape-google-flights), [How To Scrape Google Images](https://github.com/oxylabs/how-to-scrape-google-images), [Scrape Google Search Results](https://github.com/oxylabs/scrape-google-python), [Scrape Google Trends](https://github.com/oxylabs/how-to-scrape-google-trends)
