#!/usr/bin/env python3

import twitter
from auth_lib import auth

auth = auth()
api = twitter.Api(consumer_key=auth.consumer_key,
                  consumer_secret=auth.consumer_secret,
                  access_token_key=auth.access_token_key,
                  access_token_secret=auth.access_token_secret)

t_search = api.GetSearch(term="@cloud_opinion",
                         count=1,
                         return_json=True)

[print(post['created_at'] + ":\n" + post['text']) for post in t_search['statuses']]
