"""
Unit tests for the emotion detection application.

This module tests the emotion_detector function with various statements
to validate the dominant emotion detection.
"""

import unittest
from EmotionDetector.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):
    """Test cases for the emotion_detector function."""

    def test_emotion_detector(self):
        """Test emotion detection for various statements."""
        result = emotion_detector("I am glad this happened")
        self.assertEqual(result["dominant_emotion"], "joy")

        result = emotion_detector("I am really mad about this")
        self.assertEqual(result["dominant_emotion"], "anger")

        result = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(result["dominant_emotion"], "disgust")

        result = emotion_detector("I am so sad about this")
        self.assertEqual(result["dominant_emotion"], "sadness")

        result = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(result["dominant_emotion"], "fear")


if __name__ == "__main__":
    unittest.main()
