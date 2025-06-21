from argparse import ArgumentParser
from utils import Configuration,check_website,send_gotify_notification
from gotify import Gotify


def main():
    parser = ArgumentParser("gotify-livechecker")
    parser.add_argument("configfile",help="the required configuration file")
    args = parser.parse_args()

    conf = Configuration.from_file(args.configfile)
    gotify_client = Gotify(base_url=conf.gotify_url,app_token=conf.gotify_token)
    
    websites_nok = []
    for website in conf.websites:
        expected = conf.expected_code.get(website)
        if not expected:
            expected = 200
        
        if not check_website(website,expected_code=expected):
            websites_nok.append(website)
    
    if len(websites_nok) > 0:
        send_gotify_notification(gotify_client=gotify_client,websites_down=websites_nok,title=conf.notification_title,msg_format=conf.notification_format)

if __name__ == "__main__":
    main()