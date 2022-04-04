from app import app
from api.utils import load_data_from_json, load_post_by_id
from config import POSTS



def test_app():
    response = app.test_client().get("/api/posts")
    print(response.status_code)


def test_type_posts():
    data = load_data_from_json(POSTS)
    assert type(data) == list, TypeError



def test_type_post():
    data = load_data_from_json(POSTS)
    for d in data:
        id = d["pk"]
        post = load_post_by_id(id)
        assert type(post) == dict, TypeError



def post_keys():
    keys_list = []
    data = load_data_from_json(POSTS)
    for d in data:
        for key in d:
            keys_list.append(key)
