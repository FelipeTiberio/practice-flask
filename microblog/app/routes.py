from app import create_app

@create_app.route('/')
@create_app.route('/index')
def index():
    return "Hello, World!"
