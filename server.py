"""
Flask Server for Emotion Detector Application.

This module initiates a Flask application that performs emotion detection
on user-provided text and deploys it on localhost:5000.
"""

from flask import Flask, render_template, request
from EmotionDetector.emotion_detection import emotion_detector

app = Flask("Emotion Detector")


@app.route("/emotionDetector")
def emotion_detect():
    """
    Analyze emotions of text received from the HTML interface.

    Receives text via GET request, runs emotion detection,
    and returns the detected emotions and dominant emotion.

    Returns:
        str: Formatted string with detected emotions and dominant emotion, or error message.
    """
    # Retrieve text from GET request parameter
    text_to_analyze = request.args.get("textToAnalyze")

    # Check for empty or None input
    if not text_to_analyze or not text_to_analyze.strip():
        return "Invalid text! Please try again!"

    # Run emotion detection
    emotion_result = emotion_detector(text_to_analyze)

    # Check for invalid response
    if emotion_result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    # Format response message
    output = (
        f"For the given statement, the system response is "
        f"'anger': {emotion_result['anger']}, "
        f"'disgust': {emotion_result['disgust']}, "
        f"'fear': {emotion_result['fear']}, "
        f"'joy': {emotion_result['joy']} and "
        f"'sadness': {emotion_result['sadness']}. "
        f"The dominant emotion is {emotion_result['dominant_emotion']}."
    )
    return output


@app.route("/")
def render_index_page():
    """
    Render the main application page.

    Returns:
        str: Rendered HTML template for the index page.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
