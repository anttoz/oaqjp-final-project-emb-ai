from flask import Flask, request, render_template

from EmotionDetection import emotion_detector

app = Flask("Emotion Detector")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/emotionDetector")
def detect_emotion():
    text_to_analyze = request.args["textToAnalyze"]

    result = emotion_detector(text_to_analyze)

    response_html = (
        "For the given statement, the system response is "
        f"'anger': {result['anger']}, 'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, 'joy': {result['joy']} and 'sadness': {result['sadness']}."
        f"The dominant emotion is <b>{result['dominant_emotion']}</b>."
    )

    return response_html

if __name__ == "__main__":
    app.run(debug=True)