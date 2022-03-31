from flask import Blueprint, render_template, send_from_directory
from main.utils import load_posts_from_json, search_post_by_id
import config


posts_blueprint = Blueprint("posts_blueprint", __name__, static_folder="static", template_folder="templates")


#Вывод всех постов
@posts_blueprint.route("/")
def index_page():
    data = load_posts_from_json(config.POSTS)
    return render_template("index.html", data=data)


#Вывод поста по ID
@posts_blueprint.route("/post/<int:id>")
def post_contetn(id):
    post = search_post_by_id(id)
    return render_template("post.html", post=post)


#открываем доступ к "img"
@posts_blueprint.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img", path)
