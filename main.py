from flask import render_template, Flask, request

main = Flask(__name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/<url>')
def redirect(url):
    path = request.path
    url = path[1:len(path)]
    file = f'{url}.html'
    try:
        return render_template(file)
    except:
        return render_template('index.html', msg="URL does not exist")


if __name__ == '__main__':
    main.run()


