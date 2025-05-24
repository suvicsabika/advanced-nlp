from flask import Blueprint, jsonify, request
from app.services.news_fetcher import fetch_news

news_bp = Blueprint('news', __name__)

@news_bp.route('/api/news', methods=['GET'])
def get_news():
    """
    Handles a GET request to retrieve news articles based on given parameters.
    Provides an endpoint to fetch news information filtered optionally by category
    and country. Supports pagination through the `page_size` parameter.

    Parameters are taken from query arguments:
    - `category`: Optionally specify the category of news.
    - `country`: Specify the country for news localization. Defaults to 'us' if
      not provided.
    - `page_size`: Specify how many news items should be fetched. Defaults to 20
      if not provided.

    On success, the endpoint returns a JSON object containing the news data.
    In case of an error, an appropriate JSON response along with the HTTP status
    code is returned.

    :param category: Optional; Filter news by category.
    :param country: Filter news localization by country. Defaults to 'us'.
    :param page_size: Number of articles to retrieve. Defaults to 20. Must be an
      integer.
    :type category: str, optional
    :type country: str
    :type page_size: int, optional

    :return: JSON response containing the news data along with HTTP 200 status on
      success, or an error message with an appropriate HTTP status code in case
      of failure.
    """
    category = request.args.get('category')  # optional
    country = request.args.get('country', 'us')  # default: 'us'
    page_size = request.args.get('page_size', 20)

    try:
        page_size = int(page_size)
    except ValueError:
        return jsonify({
            'error': 'Invalid page_size. Must be an integer.'
        }), 400

    try:
        news_data = fetch_news(
            category=category,
            country=country,
            page_size=page_size
        )
        return jsonify(news_data), 200
    except Exception as e:
        return jsonify({
            'error': 'Something went wrong while fetching news.',
            'details': str(e)
        }), 500
