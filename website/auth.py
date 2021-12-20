from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    return render_template("login.html")

@auth.route('logout')
def logout():
    return "<p>Logout</p>"

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    data = request.form
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = data.get('firstName')
        password1 = data.get('password1')
        password2 = data.get('password2')
    return render_template("signup.html")