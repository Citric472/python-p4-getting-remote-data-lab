import requests
import json

class GetRequester:

    def __init__(self, url):
        self.url = url

    def get_response_body(self):
        response = requests.get(self.url)
        return response.content  # Use content instead of text to get bytes

    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            response_text = response_body.decode('utf-8')  # Decode bytes to string
            return json.loads(response_text)  # Parse string as JSON
        else:
            return None