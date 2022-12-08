# dmotiv8
This tool will query Twitter with your search criteria and return a single response.

It was useful to return a recent tweet about a subject or from a person.


### THIS PROJECT IS DEPRECATED
Given the state of things at Twitter, I will likely not contribute to this project again.


### Usage
```
./dmotiv8.py "Hello, World"

Mon Aug 26 16:53:56 +0000 2019:
Hello World! Check this out!
```

```
./dmotiv8.py -h
usage: Enter a given Twitter search criteria and return a single response.

A simple utility to return a single tweet

optional arguments:
  -h, --help            show this help message and exit
  --search_criteria SEARCH_CRITERIA
                        Enter any search criteria
  --screen_name SCREEN_NAME
                        Enter any twitter screen name
```

### Requirements
- Check requirements.txt for dependencies or...

    `pip install -r requirements.txt`

- Make sure to update auth_lib.py with the following information:
    ```        
    self.consumer_key='<your consumer_key here>'
    self.consumer_secret='<your consumer_secret here>'
    self.access_token_key='<your access_token_key here>'
    self.access_token_secret='<your access_token_secret here>'
    ```
