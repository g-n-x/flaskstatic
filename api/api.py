from flask import Blueprint, render_template

api = Blueprint('api', __name__, static_folder='static', template_folder='template')

@api.route('/gabaritos')
def gabaritos():
    return 'todos os gabaritos'
