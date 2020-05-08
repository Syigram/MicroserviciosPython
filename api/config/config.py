class Config(object):
    """Flask configuration object."""

    # General Flask Config
    SECRET_KEY = 'secret_key' #secret_key should be a Hash, ideally loaded from ENV
    FLASK_ENV = 'development'
    FLASK_DEBUG = 1

    # Database
    SQLALCHEMY_DATABASE_URI = "sqlite:///db_form.sqlite3"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
