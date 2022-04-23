from flask import Flask, render_template
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    data_list = []

    data_list.append(request.form.get('payment'))
    data_list.append(request.form.get('fname'))
    data_list.append(request.form.get('lname'))
    data_list.append(request.form.get('address'))
    data_list.append(request.form.get('place'))
    data_list.append(request.form.get('zipCode'))
    data_list.append(request.form.get('phone'))
    data_list.append(request.form.get('email'))
    data_list.append(request.form.get('password'))
    data_list.append(request.form.get('emailOffer'))
    data_list.append(request.form.get('emailFormat'))
    data_list.append(request.form.get('comments'))

    return render_template('register.html', data=data_list)