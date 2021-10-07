from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def read_all():
    users = User.show_me()
    return render_template('Read(All).html', all_users = users)

@app.route('/create', methods=['POST'])
def create_me():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/')

@app.route('/link')
def link():
    return render_template('Create.html')

@app.route('/home')
def home():
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)