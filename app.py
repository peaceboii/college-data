from flask import Flask, render_template, redirect, request, flash , jsonify
import mysql.connector
import re


app = Flask(__name__)

db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Kumar@2003",
    database="college"
)

app.secret_key = "secret123"

cursor = db.cursor()

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':

        student_name = request.form['student_name']
        student_name = student_name.strip()

    # VALIDATION
        if not re.match(r'^[A-Za-z ]+$', student_name):

            flash(
                "Name should contain only alphabets and spaces!",
                "error"
            )

            return redirect('/')
        
        if len(student_name) > 50:
            flash("Student name is too long","error")
    
            return redirect('/')
        
        query=  """
                SELECT * FROM Studenttbl
                WHERE student_name=%s
                """
        values=  (student_name,)

        cursor.execute(query,values)

        duplicate = cursor.fetchone()
        print(duplicate)
        if duplicate:

            flash(
                "Student name already exists",
                "error"
            )

            return redirect('/')

        
        query = """
        INSERT INTO Studenttbl(student_name)
        VALUES(%s)
        """

        values = (student_name,)

        cursor.execute(query, values)

        db.commit()
        flash(
            "Student Added Successfully!",
            "success"
        )

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

    query = """
    SELECT * FROM studenttbl
    WHERE id=%s
    """

    cursor.execute(query, (id,))

    student = cursor.fetchone()


    if not student:

        flash(
            "Student not found!",
            "error"
        )

        return redirect('/')


    student_name = student[1]


    if not re.match(r'^[A-Za-z ]+$', student_name):

        flash(
            "Invalid student name!",
            "error"
        )

        return redirect('/')
    
    if len(student_name) > 50:
        flash("Student name is too long","error")
    
        return redirect('/')
    
    return render_template(
        'edit.html',
        student=student
    )

@app.route('/update/<int:id>',methods =['POST'])
def update(id):
    student_name= request.form['student_name']

    student_name = student_name.strip()

    if not re.match(r'^[A-Za-z ]+$', student_name):

        flash(
            "Only alphabets allowed!",
            "error"
        )

        return redirect(f'/edit/{id}')
    
    if len(student_name) > 50:
        flash("Student name is too long","error")
    
        return redirect(f'/edit/{id}')
    
    query="""UPDATE studenttbl SET student_name=%s WHERE id=%s"""

    values = (student_name,id)

    cursor.execute(query,values)

    db.commit()
    flash(
        "Student Loaded Successfully!",
        "success"
    )

    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)