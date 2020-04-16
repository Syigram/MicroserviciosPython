from flask import Flask


APP = Flask(__name__)


@APP.route('/')
@APP.route('/index')
def hello_world():
    return 'Hello World!'


def main():
    APP.run(host='0.0.0.0', debug=True)


if __name__ == "__main__":
    main()
