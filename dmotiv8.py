#!/usr/bin/env python3


import argparse
import twitter
from auth_lib import auth


def t_search(search_criteria):
    """
    Search twitter for a given criteria

    Return a single post
    """
    search = api.GetSearch(term=search_criteria, count=1, result_type="recent", return_json=True)
    output = [post['created_at'] + ":\n" + post['text'] for post in search['statuses']][0]
    return output


def t_get_latest_tweet(screen_name):
    """
    Fetch the sequence of public Status messages for a single user

    Return a single post
    """
    search = api.GetUserTimeline(screen_name=screen_name, count=1)
    t_post = [post.created_at.split('+')[0] + "\n" + post.text for post in search][0]

    if 'http' in t_post:
        output = t_post.split('http')[0]
    else:
        output = t_post

    return output


parser = argparse.ArgumentParser(usage="Enter a given Twitter search criteria and return a single response.",
                                 description="A simple utility to return a single tweet")
parser.add_argument('--search_criteria',
                    help="Enter any search criteria")
parser.add_argument('--screen_name',
                    help="Enter any twitter screen name")
args = parser.parse_args()


if __name__ == "__main__":
    auth = auth()
    api = twitter.Api(consumer_key=auth.consumer_key,
                      consumer_secret=auth.consumer_secret,
                      access_token_key=auth.access_token_key,
                      access_token_secret=auth.access_token_secret)

    args.screen_name = "@boredelonmusk"
    if args.screen_name and not args.search_criteria:
        print(t_get_latest_tweet(args.screen_name))
    elif args.search_criteria and not args.screen_name:
        print(t_search(args.search_criteria))
