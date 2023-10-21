
from flask import render_template, request, redirect, url_for, flash, session
from flask_bcrypt import Bcrypt  
from datetime import datetime, timedelta

from app import app

from app.models.users import User


bcrypt = Bcrypt(app)


@app.route("/")
def index():

    return render_template("index.html")


@app.route("/login/", methods=["POST"])
def login():
    data = {
        "email": request.form["email"],
        "password": request.form["password"]
    }
    
    user = User.get_by_email(data)

    if user:
        is_correct_password = bcrypt.check_password_hash(user.password, data["password"])
        if is_correct_password:
            user = {
                "id": user.id,
                "name": user.first_name,
                "email": user.email,
            }
            session["user"] = user
            flash("¡Bienvenido de nuevo!")
            return redirect(url_for("upload"))
        
    flash("Email o contraseña incorrectos")
    return redirect(url_for("index"))


@app.route("/logout/")
def logout():
    if "user" not in session:
        return redirect(url_for("index"))

    session.clear()
    flash("¡Hasta luego!", "success")
    return redirect(url_for("index"))


@app.route("/register/", methods=["POST"])
def register(): 

    password_hash = bcrypt.generate_password_hash(request.form["password"])

    data = {
        "first_name": request.form["first_name"],
        "email": request.form["email"],
        "password": password_hash,
    }

    if User.get_by_email(data):
        flash("¡El correo electrónico ya está registrado!")
        return redirect(url_for("index"))
    
    password = request.form["password"]
    confirm_password = request.form["password_confirm"]

    if password != confirm_password:
        flash("La contraseñas tienen que ser iguales.")
        return redirect(url_for("index"))
    
    if len(password) < 8:
        flash("La contraseña debe tener al menos 8 caracteres.")
        return redirect(url_for("index"))
    
    
    user = User.register(data)
    if user:
        session["user"] = {
            "id": user.id,
            "first_name": user.first_name,
            "email": user.email,
        }
        flash("¡Registro exitoso!")
        return redirect(url_for("index"))
    
    return redirect(url_for("index"))