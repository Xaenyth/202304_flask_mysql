from flask_app import app
from flask_app.models.dojo import Dojo
from flask import render_template, request, redirect

@app.route('/dojos')
def showDojo():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def dojoCreate():
    Dojo.save(request.form)
    return redirect ('/dojos')

@app.route('/dojos/<int:id>')
def showSingleDojo(id):
    return render_template("show_dojos.html", dojo=Dojo.get_dojo_with_students({"id": id}))