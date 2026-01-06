"""
Emotion Detection Module using Watson NLP Library.

This module provides functionality to analyze emotions in text using
the Watson NLP Emotion Predict service.
"""

import json
import requests


def emotion_detector(text_to_analyze):
    """
    Analyze the emotions of the provided text using Watson NLP.

    Args:
        text_to_analyze (str): The text to be analyzed for emotions.

    Returns:
        dict: A dictionary containing the detected emotions and dominant emotion.
    """
    # Check for empty or None input
    if not text_to_analyze or not text_to_analyze.strip():
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "dominant_emotion": None,
        }

    # Watson NLP emotion prediction endpoint
    url = (
        "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/"
        "NlpService/EmotionPredict"
    )
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}

    try:
        # Send POST request to Watson NLP service
        response = requests.post(url, json=myobj, headers=headers, timeout=30)

        # Extract emotion information
        if response.status_code == 200:
            # Parse JSON response
            formatted_response = json.loads(response.text)
            emotions = formatted_response["emotionPredictions"][0]["emotion"]
            # Find the dominant emotion
            dominant_emotion = max(emotions, key=emotions.get)

            return {
                "anger": emotions["anger"],
                "disgust": emotions["disgust"],
                "fear": emotions["fear"],
                "joy": emotions["joy"],
                "sadness": emotions["sadness"],
                "dominant_emotion": dominant_emotion,
            }
    except requests.exceptions.RequestException:
        # Handle request exceptions
        pass

    # Handle non-200 status codes or exceptions
    return {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }
