from flask import render_template, request, Blueprint

from myproject.models import Sahisti, ContentSahisti, Grandmasters, ContentGrandmasters

sah = Blueprint('sah', __name__)


@sah.route('/')
def index():
    return render_template('index.html')


@sah.route('/players')
def players():
    # sahisti = Sahisti.query.all()

    page = request.args.get('page', 1, type=int)
    sahisti = Sahisti.query.order_by(Sahisti.name).paginate(page=page, per_page=12)
    return render_template('players.html', sahisti=sahisti)


@sah.route('/other_players')
def other_players():
    # sahisti = Grandmasters.query.all()

    page = request.args.get('page', 1, type=int)
    sahisti = Grandmasters.query.order_by(Grandmasters.name).paginate(page=page, per_page=12)
    return render_template('other_players.html', sahisti=sahisti)


@sah.route('/player/<name>')
def player(name):
    sahist_content = ContentSahisti.query.filter_by(name=name).first()
    sahist = Sahisti.query.filter_by(name=name).first()
    return render_template('player.html', sahist=sahist, sahist_content=sahist_content)


@sah.route('/other_player/<name>')
def other_player(name):
    sahist_content = ContentGrandmasters.query.filter_by(name=name).first()
    sahist = Grandmasters.query.filter_by(name=name).first()
    return render_template('other_player.html', sahist=sahist, sahist_content=sahist_content)
