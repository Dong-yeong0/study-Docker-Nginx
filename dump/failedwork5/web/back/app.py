from flask import Flask

from route.test_route import my_test

app = Flask(__name__)

app.register_blueprint(my_test)

if __name__ == "__main__":
    app.run("0.0.0.0",port=5000, debug=True)