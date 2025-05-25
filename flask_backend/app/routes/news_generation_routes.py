from flask import Blueprint, jsonify
from app.services.generate_headline import get_news_with_headlines

news_generation_bp = Blueprint('news_generation', __name__)

@news_generation_bp.route('/api/news_with_headlines', methods=['POST'])
def news_with_headlines():
    """
    Handles the API route '/api/news_with_headlines' for generating news articles
    with headlines. This route processes a POST request and invokes the
    `get_news_with_headlines` function to retrieve the required responses.

    Returns the generated news with headlines in JSON format upon success or an error
    message with details in case of failure.

    **Important to mention it here that this route is only for demonstration purposes... TODO**

    :raises Exception: If any error occurs during the news-headline generation process

    :return: A tuple containing the JSON response and the HTTP status code
    :rtype: tuple
    """
    try:
        response = get_news_with_headlines()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            "error": "Something went wrong in the news-headline generation process.",
            "details": str(e)
        }), 500
