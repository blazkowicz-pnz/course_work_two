from flask import Blueprint, render_template, send_from_directory, request
from main.utils import load_data_from_json, search_post_by_id, get_comment_by_post_id, get_post_by_user_name, get_posts_by_word
import config


posts_blueprint = Blueprint("posts_blueprint", __name__, static_folder="static", template_folder="templates")


#Вывод всех постов
@posts_blueprint.route("/")
def index_page():
    data = load_data_from_json(config.POSTS)
    return render_template("index.html", data=data)


#Вывод поста по ID
@posts_blueprint.route("/post/<int:id>")
def post_contetn(id):
    post = search_post_by_id(id)
    comments = get_comment_by_post_id(id)
    return render_template("post.html", post=post, comments=comments)



@posts_blueprint.route("/users/<username>")
def user_posts(username):
    user_posts = get_post_by_user_name(username)
    return render_template("user-feed.html", user_posts=user_posts)


@posts_blueprint.route("/search/")
def search_posts():
    word = request.args.get("word")
    posts = get_posts_by_word(word)
    return render_template("search.html", word=word, posts=posts)


#открываем доступ к "img"
@posts_blueprint.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)
