# app.py
from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

# Your sentiment analysis AI tool function
def analyze_sentiment(text):
    # Implement your sentiment analysis AI tool here
    # For simplicity, we'll use a basic rule-based approach
    positive_words = ['good', 'happy', 'excellent', 'love']
    negative_words = ['bad', 'sad', 'terrible', 'hate']

    text_lower = text.lower()
    words = text_lower.split()

    positive_count = sum(1 for word in words if word in positive_words)
    negative_count = sum(1 for word in words if word in negative_words)

    if positive_count > negative_count:
        return 'positive'
    elif positive_count < negative_count:
        return 'negative'
    else:
        return 'neutral'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/sentiment', methods=['POST'])
def analyze_sentiment_api():
    data = request.get_json()
    text = data.get('text')

    if text is None:
        return jsonify({'error': 'Text not provided'}), 400

    result = analyze_sentiment(text)
    return jsonify({'sentiment': result})

if __name__ == '__main__':
    app.run(debug=True)
