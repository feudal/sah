from flask import render_template, request, Blueprint

from myproject.models import Sahisti, ContentSahisti

sah = Blueprint('sah', __name__)


@sah.route('/')
def index():
    return render_template('index.html')


@sah.route('/jucatori')
def players():
    # sahisti = Sahisti.query.all()

    page = request.args.get('page', 1, type=int)
    sahisti = Sahisti.query.order_by(Sahisti.name).paginate(page=page, per_page=8)
    return render_template('players.html', sahisti=sahisti)


@sah.route('/jucator/<name>')
def player(name):
    sahist_content = ContentSahisti.query.filter_by(name=name).first()
    sahist = Sahisti.query.filter_by(name=name).first()
    return render_template('player.html', sahist=sahist, sahist_content=sahist_content)
