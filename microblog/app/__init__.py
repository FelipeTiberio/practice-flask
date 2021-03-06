from flask import Flask

create_app = Flask(__name__)

'''
	One aspect that may seem confusing at first is that
there are two entities named app. The app package 
is defined by the app directory and the __init__.py script,
and is referenced in the from app import routes statement.
The app variable is defined as an instance
of class Flask in the __init__.py script, which makes it a member of the app package. '''
from app import routes
