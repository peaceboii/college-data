from flask import Flask, render_template, redirect, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kumar@2003",
    database="college"
)

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        student_name = request.form['student_name']

        query = """
        INSERT INTO Studenttbl(student_name)
        VALUES(%s)
        """

        values = (student_name,)

        cursor.execute(query, values)

        db.commit()

        return redirect('/')

    cursor.execute("SELECT * FROM Studenttbl")

    students = cursor.fetchall()

    return render_template(
        'index.html',
        students=students
    )

@app.route('/delete/<int:id>')
def delete(id):
    query= """DELETE FROM studenttbl WHERE id=%s"""

    cursor.execute(query ,(id,))

    db.commit()

    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    query ="""SELECT * FROM studenttbl WHERE id=%s"""

    cursor.execute(query,(id,))

    student =cursor.fetchone()

    return render_template('edit.html',student=student)

@app.route('/update/<int:id>',methods =['POST'])
def update(id):
    student_name= request.form['student_name']

    query="""UPDATE studenttbl SET student_name=%s WHERE id=%s"""

    values = (student_name,id)

    cursor.execute(query,values)

    db.commit()

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)