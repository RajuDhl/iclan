from flask import render_template, Flask, request

main = Flask(__name__)


@main.route('/')
def home():
    # req2 = request.script_root
    # print(req2, "HERE")
    return render_template('index.html')


@main.route('/<url>')
def redirect(url):
    path = request.path
    url = path[1:len(path)]
    file = f'{url}.html'
    return render_template(file)


if __name__ == '__main__':
    main.run()

# # @main.route('/services')
# # def services():
# #     return render_template('services.html')
#
#
# @main.route('/corporate')
# def corporate():
#     return render_template('b2b.html')
#
#
# @main.route('/contact')
# def contact():
#     return render_template('contact.html')
#
#
# @main.route('/about')
# def about():
#     return render_template('about.html')
#
#
# @main.route('/macbook')
# def macbook():
#     return render_template('macbook.html')
# # @main.route('/services')
#
# # if __name__ == '__main__':
# #     app.run()
