import json 
import base64
from openai import OpenAI
from dataclasses import dataclass, field

@dataclass
class ChatGPTData:
    image_base64: bytes = field(default=None, init=False)
    responses: list[str] = field(default_factory=list, init=False)

    @property
    def response(self) -> str:
        if self.responses:
            return self.responses[-1]
        return "No response yet"

    def set_response(self, response: str) -> None:
        print(f"testing response setter: {response}")
        self.responses.append(response)

    def set_image(self, image_path: str) -> None:
        print("testing imgdata setter")
        if not image_path:
            raise ValueError("Image path cannot be empty")
        self.image_base64 = self.encode_image(image_path)

    @staticmethod
    def encode_image(image_path: str) -> bytes:
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

@dataclass
class ChatGPTClient:
    data: ChatGPTData
    client = OpenAI()

    def query(self) -> None:
        img = self.data.image_base64
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "Content-Type": "application/json",
                    "content": (
                        "You are a helpful assistant and the driver of a RC car. Your goal is to reach "
                        "the basketball seen in the photo by replying with steering controls for the car! "
                        "Reply in JSON format with the following keys: 'forward' (true/false), 'forward_distance'(in metres), "
                        "'turn_direction (clockwise/anticlockwise)', 'turn_degrees [0,90]'. If you cannot see the target, stay still and rotate 90 degrees."
                    )
                },
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "How do I reach the ball?"
                        },
                        {
                            "type": "image_url",
                            "image_url": {
                                "url": f"data:image/jpeg;base64,{img}"
                            }
                        }
                    ]
                }
            ],
        )

        response_content = completion.choices[0].message.content
        print(response_content)

        try:
            response_json = json.loads(response_content)
        except json.JSONDecodeError:
            response_json = {"error": "Invalid JSON response"}

        self.data.set_response(response_json)


    @staticmethod
    def validate_response(resp: str) -> str:
        return ""