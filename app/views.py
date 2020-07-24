from app import app, api
from app.api_resource import ContactResource


@app.route('/heart-beat')
def hello_world():
    return 'Running...'


api.add_resource(ContactResource, '/api/contact')
