import requests

root_url : str = requests.get("status/")
status_url : int = root_url.status_code



