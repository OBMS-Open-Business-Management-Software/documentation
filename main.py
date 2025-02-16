import requests

def define_env(env):
    @env.macro
    def include_url(url):
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            return f"Error fetching URL: {e}"
