from flask import Blueprint, jsonify
from app.services.news_fetcher import fetch_news

news_bp = Blueprint('news', __name__)

@news_bp.route('/api/news', methods=['GET'])
def get_news():
    """
    Retrieve the latest news and return it as a JSON response.

    This function fetches news content from an external source, processes it,
    and returns the data in a JSON format. If an error occurs during the
    fetching or processing of the news, it returns an error message
    with the corresponding HTTP status code.

    :raises Exception: If there is an error during news fetching or processing.
    :return: A JSON response containing the news data if successful,
             or an error message if an exception occurs.
    :rtype: Tuple[flask.Response, int]
    """
    try:
        news_data = fetch_news()
        return jsonify(news_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
