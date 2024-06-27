from flask import Flask
from routes.route import upload_route

def create_app():
    app = Flask(__name__, static_folder='public')

    app.register_blueprint(upload_route)
    return app

if __name__ == '__main__':
    app = create_app()
    app.run(host='127.0.0.1', port=5000, debug=True)