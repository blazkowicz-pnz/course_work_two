import pytest
from main.utils import load_data_from_json, search_post_by_id
from config import POSTS


def test_load_json_data():
    data = load_data_from_json(POSTS)
    assert type(data) == list, TypeError


def test_search_post_by_id():
    data = load_data_from_json(POSTS)
    for d in data:
        id = d["pk"]
        post = search_post_by_id(id)
        assert type(post) == dict, TypeError