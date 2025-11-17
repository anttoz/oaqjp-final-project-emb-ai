"""
This module contains a Flask app that provides API endpoints for
an emotion detection web app.
"""
from flask import Flask, request, render_template

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    """Route definition for the root path. Renders the web UI of the app."""
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    """
    Route definition for the '/emotionDetector' path.

    Returns the result of emotion detection API for
    the text given as 'textToAnalyze' query parameter.
    In the case of invalid input, returns an error message.
    """
    text_to_analyze = request.args["textToAnalyze"]

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!."

    response_html = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}."
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )

    return response_html

if __name__ == "__main__":
    app.run(debug=True)
