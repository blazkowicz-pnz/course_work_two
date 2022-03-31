from flask import Flask, render_template, send_from_directory,request


from utils import load_posts_from_json,search_post_by_id

app = Flask("__name__")
app.config.from_pyfile("config.py")
json_data = app.config.get("DATA")

#Вывод всех постов
@app.route("/")
def index_page():
    data = load_posts_from_json(json_data)
    return render_template("index.html", data=data)


#Вывод поста по ID
@app.route("/post/<int:id>")
def post_contetn(id):
    post = search_post_by_id(id)
    return render_template("post.html", post=post)



#доступ к папке с изображениями
@app.route("/img/<path:path>")
def static_dir(path):
    return send_from_directory("img",path)

if __name__ == "__main__":
    app.run()


