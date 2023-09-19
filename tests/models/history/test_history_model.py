import json
from src.models.history_model import HistoryModel


# Req. 7
def test_request_history():
    list = [
        {
            "text_to_translate": "Hello, I like videogame",
            "translate_from": "en",
            "translate_to": "pt",
        },
        {
            "text_to_translate": "Do you love music?",
            "translate_from": "en",
            "translate_to": "pt",
        },
    ]
    response = json.loads(HistoryModel.list_as_json())
    expected = list

    for object in response:
        object.pop("_id")

    assert response == expected
