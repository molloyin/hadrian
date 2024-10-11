from openai import OpenAI
from requests import Session
from dataclasses import dataclass, field

@dataclass
class ChatGPTData:
    api_key: str
    api_url: str
    model: str
    image_data: bytes = field(default=None, init=False)
    responses: list[str] = field(default_factory=list, init=False)

    @property
    def response(self) -> str:
        if self._responses:
            return self._responses[-1]
        return "No response yet"

    def set_response(self, response: str) -> None:
        print("testing response setter")
        print(response)
        self.responses.append(response)

    def set_image_data(self, data: bytes) -> None:
        print("testing imgdata setter")
        if not data:
            raise ValueError("Image data cannot be empty")
        self.image_data = data

@dataclass
class ChatGPTClient:
    data: ChatGPTData
    client = OpenAI()

    def query(self):
        completion = self.client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": "five words on why you are the best!."
                }
            ]
        )

        self.data.set_response(completion.choices[0].message)
        #print(completion.choices[0].message)

    @staticmethod
    def validate_response(resp: str) -> str:
        return ""