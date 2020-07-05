import requests


class Http:
    @staticmethod
    def get(url, is_json=True):
        response = requests.get(url)
        if response.status_code != 200:
            return {} if is_json else ''

        return response.json() if is_json else response.text
