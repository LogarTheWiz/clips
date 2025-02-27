from flask import Blueprint, render_template, redirect, url_for, flash, request, current_app
from flask_login import login_user, logout_user, login_required, current_user
from .models import User
from .send_email import send_email
from . import db, bcrypt

account = Blueprint('account', __name__)

@account.route("/account/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('routes.home'))

    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        user = User(username=username, email=email, password=hashed_password)
        db.session.add(user)
        db.session.commit()

        mail = current_app.extensions['mail']
        subject = "Welcome"
        body = f"Hello {username},\n\nThank you for registering!"
        html = render_template("emails/welcome.html", username=username)
        send_email(mail, subject, [email], body, html=html)

        flash("Your account has been created! You can now log in.", "success")
        return redirect(url_for('account.login'))

    return render_template("account/register.html")

@account.route("/account/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("routes.home"))

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]
        user = User.query.filter_by(email=email).first()
        if user and bcrypt.check_password_hash(user.password, password):
            login_user(user)
            flash("You have been logged in!", "success")
            return redirect(url_for("routes.home"))
        else:
            flash("Login Unsuccessful. Please check email and password.", "danger")
    
    return render_template("account/login.html")

@account.route("/account/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("account.login"))

@account.route("/account/forgot_password", methods=["GET", "POST"])
def forgot_password():
    return render_template("account/forgot_password.html")

@account.route("/account/reset_password", methods=["GET", "POST"])
def reset_password():
    return render_template("account/reset_password.html")