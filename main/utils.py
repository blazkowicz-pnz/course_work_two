import json
import config


PATH = config.POSTS
COMMENTS_PATH = config.COMMENTS


def load_data_from_json(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        posts = json.load(file)
        return posts


def search_post_by_id(id):
    posts = load_data_from_json(PATH)
    for post in posts:
        if id == post["pk"]:
            return post


def get_comment_by_post_id(post_id):
    comment_list = []
    post = search_post_by_id(post_id)
    comments = load_data_from_json(COMMENTS_PATH)
    for comment in comments:
        if post["pk"] == comment["post_id"]:
            comment_list.append(comment)

    return comment_list

