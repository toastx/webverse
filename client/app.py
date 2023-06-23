import api_functions
import os
from flask import Flask, render_template, request, session, redirect
from dotenv import load_dotenv
load_dotenv()

url = f"http://localhost:8000/api/v1"
app = Flask(__name__)
app.secret_key = os.getenv("secret_key")


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def student_signup():
    if request.method == 'POST':
        chk = 1
        name = request.form.get('name')
        regno = request.form.get('regno')
        block = request.form.get('block')
        password = request.form.get('password')
        roomno = request.form.get('roomno')
        register_result = api_functions.register_student(
            name, regno, block, password, roomno)
        if register_result:
            return redirect("login.html")
        else:
            return render_template("signup.html", errormessage="Some error")

    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def student_login():
    if request.method == 'POST':
        student_id = request.form.get('student_id')
        password = request.form.get('password')
        print(f"Student ID: {student_id}")
        print(f"Password: {password}")
        login_result, jwt_token = api_functions.login_student(
            student_id, password)
        print(login_result)
        if login_result:

            session['jwt_token'] = jwt_token
            print(session)
            return render_template('hm.html')
        else:
            return render_template('signup.html')

    return render_template('login.html')


if __name__ == '__main__':
    app.run(debug=True)
