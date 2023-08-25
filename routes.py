from flask import render_template, redirect, request, session, make_response
import usertools
import experimenttools
import admintools
from app import app


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login",methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")

    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        if usertools.login(email, password):
            if usertools.is_admin(email):
                return redirect("/admin")
            return redirect("/")
        return render_template("invalid.html", message="Invalid username or password!")


@app.route("/newuser",methods=["GET", "POST"])
def newuser():
    if request.method == "GET":
        return render_template("newuser.html")

    if request.method == "POST":
        email = request.form["email"]
        if len(email) < 4:
            return render_template("invalid.html",
                    message="The provided email is too short. Please include the whole address!")

        password = request.form["password"]
        passwordrepeat = request.form["passwordrepeat"]
        if password != passwordrepeat:
            return render_template("invalid.html",
                    message="The provided passwords do not match!")
        if len(password) < 4:
            return render_template("invalid.html",
                    message="The provided password is too short!")

        if usertools.newuser(email, password):
            return redirect("/")
        return render_template("invalid.html",
                message="An account associated with this email already exists!")


@app.route("/experiment",methods=["GET", "POST"])
def experiment():
    user = session["email"]
    if not usertools.terms_accepted(user):
        return redirect("/terms")
    votes = []

    if request.method == "GET":
        global profiles
        profiles = experimenttools.select_posts(3)
        return render_template("experiment.html", profiles=profiles)

    if request.method == "POST":
        for i in range(1, len(profiles) + 1):
            vote = request.form[str(i)]
            votes.append(vote)
        accuracy = experimenttools.record_votes(profiles, votes)
        experimenttools.record_accuracy(accuracy)
        return render_template("result.html", profiles=profiles, accuracy=accuracy)


@app.route("/admin")
def admin():
    participants = admintools.get_participants()
    responses = admintools.total_responses()
    accuracy = admintools.average_accuracy()
    if accuracy is None:
        accuracy = 0
    return render_template("admin.html",
            participants=participants,
            responses=responses,
            accuracy=accuracy)

    # if session["admin"]:
    #     participants = admintools.get_participants()
    #     responses = admintools.total_responses()
    #     accuracy = admintools.average_accuracy()
    #     if accuracy is None:
    #         accuracy = 0
    #     return render_template("admin.html",
    #             participants=participants,
    #             responses=responses,
    #             accuracy=accuracy)
    # return render_template("invalid.html",
    #         message="Access denied!")


@app.route("/remove", methods=["GET", "POST"])
def remove():
    participants = admintools.get_participants()

    if request.method == "GET":
        return render_template("removeuser.html", participants=participants)

    if request.method == "POST":
        user = request.form["email"]
        user_id = admintools.get_id(user)
        if user_id is None:
            return render_template("adminerror.html",
                    message="Please enter a valid email from the list!")

        admintools.remove_user(user_id[0])
        return redirect("/admin")    

    # if session["admin"]:
    #     participants = admintools.get_participants()

    #     if request.method == "GET":
    #         return render_template("removeuser.html", participants=participants)

    #     if request.method == "POST":
    #         user = request.form["email"]
    #         user_id = admintools.get_id(user)
    #         if user_id is None:
    #             return render_template("adminerror.html",
    #                     message="Please enter a valid email from the list!")

    #         admintools.remove_user(user_id[0])
    #         return redirect("/admin")
    # return render_template("invalid.html",
    #         message="Access denied!")


@app.route("/logout")
def logout():
    del session["email"]
    del session["user_id"]
    del session["csrf_token"]
    return redirect("/")


@app.route("/show/<int:image_id>")
def show(image_id):
    data = experimenttools.select_image(image_id)
    response = make_response(bytes(data))
    response.headers.set("Content-Type", "image/jpeg")
    return response


@app.route("/terms",methods=["GET", "POST"])
def terms():
    if request.method == "GET":
        return render_template("terms.html")

    if request.method == "POST":
        response = request.form["response"]
        if response == "1":
            user = session["email"]
            usertools.accept_terms(user)
            return redirect("/experiment")
        return redirect("/")
