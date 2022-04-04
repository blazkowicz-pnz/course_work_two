from flask import flash, Blueprint, render_template, jsonify, config
from api.utils import load_data_from_json, load_post_by_id
from config import POSTS

api_blueprint = Blueprint("api_blueprint", __name__, static_folder="static", )


@api_blueprint.route("/api/posts")
def get_json_data():
    data_json = load_data_from_json(POSTS)
    return jsonify(data_json)


@api_blueprint.route("/api/posts/<int:id>")
def get_post_as_json(id):
    json_post = load_post_by_id(id)
    return jsonify(json_post)
