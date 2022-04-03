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

def get_post_by_user_name(user_name):
    posts = load_data_from_json(PATH)
    users_post_list = []
    for post in posts:
        if post["poster_name"] == user_name:
            users_post_list.append(post)
    return users_post_list


def get_posts_by_word(word):
    posts_list = []
    posts = load_data_from_json(PATH)
    for post in posts:
        if str(word).lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list

print(get_posts_by_word("еда"))


