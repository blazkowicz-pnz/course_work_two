import json
import config


PATH = config.POSTS
COMMENTS_PATH = config.COMMENTS
BOOKMARKS_PATH = config.BOOKMARKS


# загрузка данных из json
def load_data_from_json(PATH):
    try:
        with open(PATH, "r", encoding="utf-8") as file:
            posts = json.load(file)
            return posts
    except FileNotFoundError:
        return "File not found"
    except json.JSONDecodeError:
        return "Json file don't decode"


# получаем пост по его ID
def search_post_by_id(id):
    try:
        posts = load_data_from_json(PATH)
        for post in posts:
            if id == post["pk"]:
                return post
    except ValueError:
        return "Post not found"


# Получаем комментарии, соответствующие нужному пользователю
def get_comment_by_post_id(post_id):
    try:
        comment_list = []
        post = search_post_by_id(post_id)
        comments = load_data_from_json(COMMENTS_PATH)
        for comment in comments:
            if post["pk"] == comment["post_id"]:
                comment_list.append(comment)
        return comment_list
    except ValueError:
        return "Comments not found"


# поиск постов по имени пользователя, вернет список постов одного пользователя
def get_post_by_user_name(user_name):
    try:
        posts = load_data_from_json(PATH)
        users_post_list = []
        for post in posts:
            if post["poster_name"] == user_name:
                users_post_list.append(post)
        return users_post_list
    except ValueError:
        return "Users posts is not found"


# поиск постов по слову, вернет список из 10 постов
def get_posts_by_word(word):
    try:
        posts_list = []
        posts = load_data_from_json(PATH)
        for post in posts:
            if str(word).lower() in post["content"].lower():
                posts_list.append(post)
        return posts_list[:10]
    except:
        return "posts by word is not found"


# Поиск постов, содержащих тэги, запись в список
def get_posts_by_tag(tag, flag="#"):
    try:
        posts_list_tag = []
        posts = load_data_from_json(PATH)
        for post in posts:
            content_list = post["content"].split(" ")
            for word in content_list:
                if word[0] == flag:
                    if word[1:] == tag:
                        posts_list_tag.append(post)
        return posts_list_tag
    except:
        return "posts with words'#' not found"


# Добавление поста в закладки - файл bookmarks.json. Убедитесь, что bookmarks.json не пустой и содержит список. При необходимости создайте его (список)
def add_to_bookmarks(content):
    try:
        with open(BOOKMARKS_PATH, "r", encoding="utf-8") as file:
            data = json.load(file)
            data.append(content)
            with open(BOOKMARKS_PATH, "w", encoding="utf-8") as file:
                data = json.dump(data, file, ensure_ascii=False)
        return (data)
    except FileNotFoundError:
        return "file not found"
    except json.JSONDecodeError:
        return "JSON file don't decode"


# удаление поста, в качестве аргумента передаем пост, который необходимо удалить!
def remove_post(post):
    try:
        with open(BOOKMARKS_PATH, "r", encoding='utf-8') as file:
            data = json.load(file)
            data.remove(post)
            with open(BOOKMARKS_PATH, "w", encoding="utf-8") as file:
                data = json.dump(data, file, ensure_ascii=False)
        return data
    except FileNotFoundError:
        return "file not found"




