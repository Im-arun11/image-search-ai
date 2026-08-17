import requests
import os 
from dotenv import load_dotenv
load_dotenv()
COLAB_API_URL = os.getenv("COLAB_API_URL")
def analyse_image(uploaded_image):
    url = COLAB_API_URL.rstrip("/") + "/analyze"
    response = requests.post(
        url,
        files={
            "image": (
                uploaded_image.name,
                uploaded_image.getvalue(),
                uploaded_image.type
            )
        },
        headers={
            "ngrok-skip-browser-warning": "true"
        }
    )
    print("Request URL:", url)
    response.raise_for_status()
    return response.json()["description"]