from flask import Blueprint, render_template

app_route = Blueprint('first_route',__name__)

@app_route.route('/')
def index():
    print("API Called")
    return render_template('index.html')