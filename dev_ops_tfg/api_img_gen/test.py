import requests
import json
from PIL import Image
from io import BytesIO

from aux import img_desc, out_img

api_key = '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'
model = 'image-alpha-001'
# prompt = 'A pencil and watercolor drawing of a bright city in the future with flying cars'
prompt = img_desc

response = requests.post(
    'https://api.openai.com/v1/images/generations',
    headers={'Content-Type': 'application/json',
             'Authorization': f'Bearer {api_key}'},
    data=json.dumps({'model': model, 'prompt': prompt, 'num_images': 1})
)

if response.status_code == 200:
    response_json = json.loads(response.text)
    image_url = response_json['data'][0]['url']
    image_data = requests.get(image_url).content
    image = Image.open(BytesIO(image_data))
    # image.show()
    image.save(out_img)
else:
    print(f'Error: {response.status_code} {response.reason}')
