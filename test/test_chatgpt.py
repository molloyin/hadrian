import pytest
from hadrian.connections.chatgpt import ChatGPTData

@pytest.fixture
def chatgpt_data():
    return ChatGPTData()

def test_set_response(chatgpt_data):
    response = '{"forward": true, "forward_distance": 1.0, "turn_direction": "clockwise", "turn_degrees": 45}'
    chatgpt_data.set_response(response)
    assert chatgpt_data.response == response

def test_set_image(chatgpt_data, tmp_path):
    image_path = tmp_path / "test_image.jpg"
    with open(image_path, "wb") as f:
        f.write(b"\xff\xd8\xff")

    chatgpt_data.set_image(str(image_path))
    assert chatgpt_data.image_base64 is not None
