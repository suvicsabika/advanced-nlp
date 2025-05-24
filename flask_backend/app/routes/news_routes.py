from flask import Blueprint, jsonify
from app.services.news_fetcher import fetch_news

news_bp = Blueprint('news', __name__)

@news_bp.route('/api/news', methods=['GET'])
def get_news():
    try:
        news_data = fetch_news()
        return jsonify(news_data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
