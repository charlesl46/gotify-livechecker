import requests
from gotify import Gotify
from dataclasses import dataclass,field
import json

@dataclass
class Configuration:
    websites : list
    gotify_url : str
    gotify_token : str
    expected_code: dict = field(default_factory=dict)
    notification_format : str = "The websites {} are down."
    notification_title : str = "Gotify Livechecker"
    
    @classmethod
    def from_file(cls,dict_path):
        with open(dict_path,"r") as file:
            content = json.load(file)
        return Configuration(**content)

def check_website(url : str, expected_code : int = 200):
    if not url.startswith("http"):
        url = f"https://{url}"
    
    try:
        response = requests.get(url)
        code = response.status_code
    except requests.exceptions.ConnectionError:
        code = None
    
    return expected_code == code

def send_gotify_notification(gotify_client : Gotify,websites_down : list[str],title : str,msg_format : str):
    message = msg_format.format(', '.join(websites_down))
    gotify_client.create_message(
        message=message,
        title=title
    )
