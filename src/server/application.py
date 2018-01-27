from flask import Flask
from flask_restplus import Api
from src.routes.status import api as status_api


def create_app(config=None):
    app = Flask(__name__)
    app.config.update(config or {})

    api = Api(app,
              version='1.0',
              title='Sample API',
              description='A sample API returning server status.')

    define_routes(api)

    return app

def define_routes(api):
    api.add_namespace(status_api, path='/api/v1/status')

def init():
    app = create_app()
    app.run(debug=False)

if __name__ == '__main__':
    init()
