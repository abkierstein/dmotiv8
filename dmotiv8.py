#!/usr/bin/env python3

import argparse
import twitter
from auth_lib import auth


def t_search(search_criteria):
    """
    Search twitter for a given criteria

    Return a single post

    The intended usage of this function is to grab a single post from a user
    """
    search = api.GetSearch(term=search_criteria, count=1, result_type="recent", return_json=True)
    output = [post['created_at'] + ":\n" + post['text'] for post in search['statuses']][0]
    return output

parser = argparse.ArgumentParser(usage="Enter a given Twitter search criteria and return a single response.",
                                 description="A simple utility to return a single tweet")
parser.add_argument('search_criteria',
                    type=str,
                    help="Enter any search criteria")
args = parser.parse_args()


if __name__ == "__main__":
    auth = auth()
    api = twitter.Api(consumer_key=auth.consumer_key,
                      consumer_secret=auth.consumer_secret,
                      access_token_key=auth.access_token_key,
                      access_token_secret=auth.access_token_secret)

    print(t_search(args.search_criteria))
