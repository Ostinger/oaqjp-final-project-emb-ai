"""
Flask server for Emotion Detection Application.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def render_index_page():
    """
    Render the main application page.
    """
    return render_template("index.html")

@app.route("/emotionDetector")
def analyze_emotion():
    """
    Analyze text input and return detected emotions.
    """
    user_text = request.args.get("textToAnalyze")
    result = emotion_detector(user_text)

    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!"

    return (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
