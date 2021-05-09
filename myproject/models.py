from myproject import db


class Sahisti(db.Model):
    __tablename__ = 'sahisti'
    name = db.Column(db.String, unique=True, nullable=False)
    sex = db.Column(db.String)
    dob = db.Column(db.String)
    place_dob = db.Column(db.String)
    title = db.Column(db.String)
    max_rating = db.Column(db.String)
    actual_rating = db.Column(db.String)
    fide_link = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)
    have_img = db.Column(db.Boolean)

    # posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, name, sex=None, dob=None, place_dob=None, title=None, max_rating=None, actual_rating=None,\
                 fide_link=None, has_img=False):
        self.name = name
        self.sex = sex
        self.dob = dob
        self.place_dob = place_dob
        self.title = title
        self.max_rating = max_rating
        self.actual_rating = actual_rating
        self.fide_link = fide_link
        self.has_img = has_img

    def __repr__(self):
        return f'name {self.name}'


class Grandmasters(db.Model):
    __tablename__ = 'grandmasters'
    name = db.Column(db.String, unique=True, nullable=False)
    sex = db.Column(db.String)
    dob = db.Column(db.String)
    place_dob = db.Column(db.String)
    country = db.Column(db.String)
    title = db.Column(db.String)
    max_rating = db.Column(db.String)
    actual_rating = db.Column(db.String)
    fide_link = db.Column(db.String)
    have_img = db.Column(db.Boolean)
    id = db.Column(db.Integer, primary_key=True)

    # posts = db.relationship('BlogPost', backref='author', lazy=True)

    def __init__(self, name, sex=None, dob=None, place_dob=None, country=None, title=None, max_rating=None, \
                 actual_rating=None, fide_link=None, has_img=False):
        self.name = name
        self.sex = sex
        self.dob = dob
        self.place_dob = place_dob
        self.country = country
        self.title = title
        self.max_rating = max_rating
        self.actual_rating = actual_rating
        self.fide_link = fide_link
        self.has_img = has_img

    def __repr__(self):
        return f'name {self.name}'


class ContentSahisti(db.Model):
    __tablename__ = 'content_sah'

    # users = db.relationship(User)

    name = db.Column(db.String, unique=True, nullable=False)
    main = db.Column(db.String)
    biography = db.Column(db.String)
    family = db.Column(db.String)
    sport_carrier = db.Column(db.String)
    personal_life = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, main=None, biography=None, family=None, sport_carrier=None, personal_life=None):
        self.name = name
        self.main = main
        self.biography = biography
        self.family = family
        self.sport_carrier = sport_carrier
        self.personal_life = personal_life


class ContentGrandmasters(db.Model):
    __tablename__ = 'grandmasters_content'

    # users = db.relationship(User)

    name = db.Column(db.String, unique=True, nullable=False)
    main = db.Column(db.String)
    biography = db.Column(db.String)
    family = db.Column(db.String)
    sport_carrier = db.Column(db.String)
    personal_life = db.Column(db.String)
    id = db.Column(db.Integer, primary_key=True)

    def __init__(self, name, main=None, biography=None, family=None, sport_carrier=None, personal_life=None):
        self.name = name
        self.main = main
        self.biography = biography
        self.family = family
        self.sport_carrier = sport_carrier
        self.personal_life = personal_life

