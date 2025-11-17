import json
import requests

def emotion_detector(text_to_analyse):
    url = "https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict"
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    request_body = { "raw_document": { "text": text_to_analyse } }

    response = requests.post(url, json = request_body, headers=headers)

    if response.status_code != 200:
        return {
            "anger": None, 
            "disgust": None, 
            "fear": None, 
            "joy": None, 
            "sadness": None, 
            "dominant_emotion": None
        }

    response_dict = json.loads(response.text)
    
    emotion_scores = response_dict["emotionPredictions"][0]["emotion"]
    emotion_score_pairs = emotion_scores.items()
    emotion_score_pair_with_max_score = max(emotion_score_pairs, key=lambda v: v[1])
    
    return {
        **emotion_scores,
        "dominant_emotion": emotion_score_pair_with_max_score[0]
    }