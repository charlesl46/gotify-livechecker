# gotify-livechecker

`gotify-livechecker` is a simple script that checks whether a list of websites is online (responding with the expected HTTP status code), and sends a notification via [Gotify](https://gotify.net/) if any of them are down.

## Features

- Reads a list of websites to check from a JSON configuration file  
- Supports custom expected HTTP response codes for each site  
- Sends a push notification to a Gotify instance if one or more websites are unreachable or down  

## Minimal configuration

Create a JSON file with the following structure :

```json
{
  "websites": [
    "https://my.awesome.website.com",
    "another.web.site" // will default to https if no protocol is defined
  ],
  "gotify_url": "https://gotify.mydomain.com",
  "gotify_token": "my-gotify-token",
}
```

## Installation

You can run the script directly if Python and the dependencies are installed. You’ll need:

- requests
- gotify (Python client, must be installed or created)

Install dependencies with:


```sh
pip install requests gotify
```

## Usage

Run the checker script with your configuration file as an argument:

```sh
python checker.py my_config.json
```

If any of the websites return a different HTTP status code than expected, a notification will be sent via your Gotify instance. You can then put this script in a cron task to check your sites every 10 minutes for example.

## Notes

By default, the expected status code is **200**, in case you'd expect any other code, you can add it to the conf file as follows : 

```json
    "expected_code" : {
        "another.web.site" : 401 // behind an authwall
    }
```

You can also custom the format of the message you want to send : 

```json
    "notification_title" : "Websites are down",
    "notification_format" : "The websites {} are down, panic !!"
```