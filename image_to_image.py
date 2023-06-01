import os
import base64
import requests
from dotenv import load_dotenv
load_dotenv()
#==============================================================
api_key   = os.getenv('STABILITY_API_KEY')
api_host  = "https://api.stability.ai"
engine_id = "stable-diffusion-v1-5"
#==============================================================
if api_key is None:
    raise Exception("Missing Stability API key.")
#==============================================================
response = requests.post(f"{api_host}/v1/generation/{engine_id}/image-to-image",headers={
        "Accept": "application/json",
        "Authorization": f"Bearer {api_key}"
    },files={
        "init_image": open("./text_to_image_0.png", "rb")
    },data={
        "image_strength": 0.35,
        "init_image_mode": "IMAGE_STRENGTH",
        "text_prompts[0][text]": "Galactic dog with a cape",
        "cfg_scale": 7,
        "clip_guidance_preset": "FAST_BLUE",
        "samples": 1,
        "steps": 30,
    })
#==============================================================
if response.status_code != 200:
    raise Exception("Non-200 response: " + str(response.text))
#==============================================================
data = response.json()
#==============================================================
for i, image in enumerate(data["artifacts"]):
    with open(f"./image_to_image_{i}.png", "wb") as f:
        f.write(base64.b64decode(image["base64"]))
