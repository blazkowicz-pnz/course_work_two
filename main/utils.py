import json
import config


PATH = config.POSTS


def load_posts_from_json(PATH):
    with open(PATH, "r", encoding="utf-8") as file:
        posts = json.load(file)
        return posts

print(load_posts_from_json(PATH))


def search_post_by_id(id):
    posts = load_posts_from_json(PATH)
    for post in posts:
        if id == post["pk"]:
            return post

