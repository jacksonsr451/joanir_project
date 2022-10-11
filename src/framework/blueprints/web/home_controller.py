from flask import render_template


def init_controller(app):
    @app.route('/')
    def home():
        return render_template('index.html')
