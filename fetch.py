import requests 

class Fetch:
    def __init__(self):
        self.base_url = "https://yts.mx/api/v2/"

    def fetch_data(self, end_url):
        return requests.get(f"{self.base_url}{end_url}").json()
    