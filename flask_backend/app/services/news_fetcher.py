from dotenv import load_dotenv
import os
import requests
from datetime import datetime, timedelta


def fetch_news(category=None, country='us', page_size=20):
    """
    Fetches news articles from the NewsAPI (newsapi.org).

    If a category is provided, it uses the 'top-headlines' endpoint.\n
    If no category is provided, it uses the 'everything' endpoint with a default keyword query.

    Please review the API call restriction on the following websites:
     * https://newsapi.org/docs/endpoints/everything
     * https://newsapi.org/docs/endpoints/top-headlines

    **TODO: Important to mention it here, that the category should be determined based on the input of the User.
    An LLM should determine the article categorization of the User!**

    :param category: Optional; News category (e.g., 'technology', 'sports').
    :type category: str or None
    :param country: Optional; Country code for filtering (only for top-headlines).
    :type country: str
    :param page_size: Number of articles to retrieve (max 100 for top-headlines).
    :type page_size: int
    :return: A list of articles with key info.
    :rtype: list[dict]
    :raises ValueError: If API key is missing.
    :raises Exception: If the API request fails.
    """
    load_dotenv()
    API_KEY = os.getenv("NEWS_API_KEY")

    if not API_KEY:
        raise ValueError("NEWS_API_KEY is missing from environment variables")

    if category:
        # Use top-headlines endpoint
        base_url = "https://newsapi.org/v2/top-headlines"
        params = {
            "apiKey": API_KEY,
            "category": category,
            "country": country,
            "pageSize": page_size,
        }
    else:
        # Use everything endpoint with default keyword if category is not provided
        base_url = "https://newsapi.org/v2/everything"
        today = datetime.now().date()
        seven_days_ago = today - timedelta(days=7)
        params = {
            "apiKey": API_KEY,
            "q": "Global news around the world today",  #  One qKeyWord is required/mandatory, otherwise BAD_REQUEST
            "from": seven_days_ago.isoformat(),
            "to": today.isoformat(),
            "sortBy": "publishedAt",
            "language": "en",
            "pageSize": page_size
        }

    response = requests.get(base_url, params=params)

    if response.status_code != 200:
        raise Exception(f"NewsAPI Error {response.status_code}: {response.text}")

    data = response.json()
    articles = data.get("articles", [])

    return [
        {
            "title": a["title"],
            "description": a["description"],
            "url": a["url"],
            "publishedAt": a["publishedAt"],
            "source": a["source"]["name"]
        }
        for a in articles
    ]
