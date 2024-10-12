import base64
from openai import OpenAI
from dataclasses import dataclass, field

@dataclass
class ChatGPTData:
    #api_key: str
    #api_url: str
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
    def encode_image(image_path: str):
        with open(image_path, "rb") as image_file:
            return base64.b64encode(image_file.read()).decode('utf-8')

@dataclass
class ChatGPTClient:
    data: ChatGPTData
    client = OpenAI()

    def query(self):
        img = self.data.image_base64
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "system", 
                    "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": "What is this image?"
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

        self.data.set_response(completion.choices[0].message)
        #print(completion.choices[0].message)

    @staticmethod
    def validate_response(resp: str) -> str:
        return ""