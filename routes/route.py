from flask import Blueprint
from controllers.controller import index

upload_route = Blueprint('upload', __name__)

upload_route.route('/upload', methods=['POST', 'GET'])(index)
