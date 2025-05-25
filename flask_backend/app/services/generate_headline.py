from flask import request, jsonify

def get_news_with_headlines():
    """
    Handles the route for retrieving news articles and generates headlines based on
    provided user preferences. The endpoint allows clients to filter news articles
    by category, country, and page size. It also takes into account user profile
    preferences like style for generating fake headlines... TODO

    :param data: JSON request payload containing the following keys:
        - category (str, optional): Specifies the category of news articles.
            Defaults to "technology".
        - country (str, optional): Specifies the country for news articles.
            Defaults to "us".
        - page_size (int, optional): Number of articles to retrieve. Defaults
            to 5.
        - user_profile (dict, optional): User preferences for headline
            generation. Contains:
            - style (str, optional): Style of the fake headline. Defaults
              to "neutral".

    :return: A JSON response containing a list of fake articles. Each article
        in the list contains:
        - original_title (str): Fake title of the article.
        - generated_headline (str): Generated headline based on user preferences.
        - url (str): URL to the fake article.
        - source (str): Source of the article (mock value).
        - publishedAt (str): Publication date and time in ISO 8601 format.
    :rtype: Tuple[Response, int]
    """

    data = request.get_json()

    category = data.get("category", "technology")
    country = data.get("country", "us")
    page_size = data.get("page_size", 5)
    user_profile = data.get("user_profile", {})

    # Fake response (at this moment, no API calls, no LLM models **YET**)
    dummy_articles = []
    for i in range(page_size):
        dummy_articles.append({
            "original_title": f"Dummy Article {i+1} in category {category}",
            "generated_headline": f"[{user_profile.get('style', 'neutral').capitalize()}] Dummy Headline {i+1}",
            "url": f"https://example.com/article{i+1}",
            "source": "MockSource",
            "publishedAt": "2025-05-24T12:00:00Z"
        })

    return {"generated_headline": dummy_articles}  , 200
