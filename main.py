from flask import render_template, Flask

main = Flask(__name__)


@main.route('/')
def home():
    return render_template('index.html')


@main.route('/services')
def services():
    return render_template('services.html')


@main.route('/corporate')
def corporate():
    return render_template('b2b.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/macbook')
def macbook():
    return render_template('macbook.html')
# @main.route('/services')

# if __name__ == '__main__':
#     app.run()
