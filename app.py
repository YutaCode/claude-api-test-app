import os
import base64
import anthropic
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.environ.get("ANTHROPIC_API_KEY"),
)

with open("image.jpg", "rb") as image: #読み込ませたい画像をimage.jpgとしてディレクトリ内に配置
    encoded_image = base64.b64encode(image.read()).decode("utf-8")

message = client.messages.create(
    model="claude-3-opus-20240229",
    max_tokens=1000,
    temperature=0,
    messages=[
        {"role": "user",
         "content": f"Here is an image: <image>{encoded_image}>\nWhat does image look like?"},
    ]
)
print(message.content[0].text)
