from flask import Flask, render_template, request, redirect

from database import db
from models import Employee


app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@db/employees'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)


@app.route('/')
def index():

    employees = Employee.query.all()

    return render_template('index.html', employees=employees)


@app.route('/add', methods=['GET', 'POST'])
def add_employee():

    if request.method == 'POST':

        employee = Employee(
            name=request.form['name'],
            email=request.form['email'],
            department=request.form['department']
        )

        db.session.add(employee)

        db.session.commit()

        return redirect('/')

    return render_template('add_employee.html')


@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_employee(id):

    employee = Employee.query.get(id)

    if request.method == 'POST':

        employee.name = request.form['name']

        employee.email = request.form['email']

        employee.department = request.form['department']

        db.session.commit()

        return redirect('/')

    return render_template('edit_employee.html', employee=employee)


@app.route('/delete/<int:id>')
def delete_employee(id):

    employee = Employee.query.get(id)

    db.session.delete(employee)

    db.session.commit()

    return redirect('/')


if __name__ == '__main__':

    with app.app_context():
        db.create_all()

    app.run(host='0.0.0.0', port=5000)
