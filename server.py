from flask import Flask, render_template, request, redirect
from user import User
app = Flask(__name__)

@app.route('/')
def read_all():
    users = User.get_all()
    return render_template('Read(All).html', all_users = users)

@app.route('/create', methods=['POST'])
def create():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    id = User.save(data)
    print(id)
    return redirect(f"/show/{id}")

@app.route('/add')
def add():
    return render_template('Create.html')

@app.route('/home')
def home():
    return redirect('/')

@app.route('/show/<int:id>')
def read_one(id):
    data = {
        'id': id
    }
    return render_template('Read(One).html', user=User.get_one(data))

@app.route('/edit/<int:id>')
def edit(id):
    data = {
        'id': id
    }
    return render_template('Edit.html', user=User.get_one(data))

@app.route('/delete/<int:id>')
def delete(id):
    data = {
        'id': id
    }
    User.remove(data)
    return redirect('/')

@app.route('/update', methods=['POST'])
def update():
    User.improve(request.form)
    id = request.form['id']
    return redirect(f"/show/{id}")

if __name__ == '__main__':
    app.run(debug=True)