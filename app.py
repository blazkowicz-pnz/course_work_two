from flask import Flask
from main.views import posts_blueprint


app = Flask(__name__)
app.register_blueprint(posts_blueprint)



if __name__ == "__main__":
    app.run()