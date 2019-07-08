import json

import requests

headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:66.0) Gecko/20100101 Firefox/66.0"}

askreddit_url = "https://www.reddit.com/r/AskReddit"


def add_json_sufix(url):
    return url if url.endswith('.json') else url + '.json'


def get_with_headers(url):
    return requests.get(url, headers=headers)


def get_subreddit_posts(subreddit_url):
    print(f"Getting posts from {subreddit_url}...")
    subreddit_url = add_json_sufix(subreddit_url)
    response = get_with_headers(subreddit_url)
    raw_posts = response.json()['data']['children']

    posts = []
    for raw_post in raw_posts:
        post = {}
        raw_post = raw_post['data']
        post['title'] = raw_post['title']
        post['score'] = raw_post['score']
        post['url'] = raw_post['url']
        post['nsfw'] = raw_post['over_18']

        posts.append(post)

    posts = sorted(posts, key=lambda post: post['score'])
    return posts


def get_comments_from_post(post_url):
    post_url = add_json_sufix(post_url)

    print(f"Getting comments from {post_url}...")
    response = get_with_headers(post_url)
    raw_comments = response.json()[1]['data']['children']

    comments = []

    for raw_comment in raw_comments:
        comment = {}
        try:
            raw_comment = raw_comment['data']
            comment['score'] = raw_comment.get('score', 0)
            comment['content'] = raw_comment['body']
            comments.append(comment)
        except:
            pass
    comments = sorted(comments, key=lambda comment: comment['score'])
    if len(comments) > 5:
        comments = comments[:5]
    return comments


posts = sorted(get_subreddit_posts(askreddit_url), key=lambda post: post['score'])
for post in posts:
    post['comments'] = sorted(get_comments_from_post(post['url']), key=lambda comment: comment['score'])

with open('results.json', 'w') as output_file:
    json.dump(posts, output_file, sort_keys=True, indent=4)
