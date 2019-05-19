from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, flash
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash
from functools import wraps

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///final.db")

def login_required(f):
    """
    Decorate routes to require login.

    http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

@app.route("/")
@login_required
def index():
    #classes = db.execute("SELECT DISTINCT classes FROM users WHERE id = :id", id =  session["user_id"])
    #print(classes)
    #portfolio = []
    # for clas in classes:
    #     assignment = db.execute("SELECT name FROM assignments WHERE class = :clas", clas =  clas["name"])
    #     duedate = db.execute("SELECT due date FROM assignments WHERE class = :clas", clas =  clas["name"])
    #     discription = db.execute("SELECT discription FROM assignments WHERE class = :clas", clas =  clas["name"])
    #     hw = {"name" :clas["name"], "duedate" :duedate, "discription" :discription}
    #     portfolio.append(hw)
    return render_template("index1.html", classes = classes, assignments = assignments)#, save = save)#, portfolio = portfolio)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            flash("must provide username")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return redirect("/login")
            flash("invalid username and/or password")

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    if request.method == "POST":

        if not request.form.get("username"):
            flash("must provide username")

        rows = db.execute("SELECT * FROM users WHERE username = :username", username = request.form.get("username"))
        if len(rows) > 1:
            flash("Sorry that username is already in use")

        elif not request.form.get("password"):
            flash("must provide password")

        elif not request.form.get("confirmation"):
            flash("please confirm pasword")

        elif request.form.get("confirmation") != request.form.get("password"):
            flash("passwords must match")

        else:
            hash = generate_password_hash(request.form.get("password"))
            db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username = request.form.get("username"), hash = hash)
            flash("YOU HAVE REGISTERED")
            return render_template("login.html")
    else:
        return render_template("register.html")

# @app.route("/calender", methods=["GET", "POST"])
# def calender():
#     """make a calender for user's assignments"""
classes = []
#new_classes = []
@app.route("/add_class", methods=["GET", "POST"])
def add_class():
    """add class for user"""
    if request.method == "POST":

        if not request.form.get("name"):
            flash("must provide name of class")

        else:
            #figure out how to append lists to have all classes listed and then sort them alphabet
            #all_classes = db.execute("SELECT classes FROM users WHERE id = :id", id = session["user_id"])
            # print(all_classes)
            added_class = (request.form.get("name"))
            # all_classes.append({"classes":added_class})
            # print(all_classes)
            # new_classes = db.execute("UPDATE users SET classes = :classes WHERE id = :id", id = session["user_id"], classes = all_classes[0])
            # print(new_classes)
            classes.append(added_class)
            print(classes)
            #sql_classes = db.execute("INSERT INTO classes (user_id, class) VALUES(:user_id, :classs)", user_id = session["user_id"], classs = added_class)
            #new_classes = db.execute("SELECT DISTINCT class FROM classes WHERE user_id = :user_id", user_id = session["user_id"])
            #print(new_classes)
            flash("YOU HAVE SUCCESSFULY ADDED A NEW CLASS")
            return render_template("index1.html", classes = classes)#, new_classes = new_classes) #, all_classes = all_classes
    else:
        return render_template("add_class.html")
assignments = []
#save = []
@app.route("/add_assignment", methods=["GET", "POST"])
def add_assignment():
    """add againments for classes and order them in terms of priority"""
    if request.method == "POST":

        if not request.form.get("name"):
            flash("must provide name of class")

        else:
            hw = []
            assignment_name = request.form.get("name")
            assignment_priority = request.form.get("priority")
            assignment_class = request.form.get("class")
            assignment_duedate = request.form.get("due_date")
            assignment_discription = request.form.get("discription")
            print(assignment_name, assignment_priority, assignment_class, assignment_duedate, assignment_discription)
            hw.append(assignment_priority)
            hw.append(assignment_name)
            hw.append(assignment_class)
            hw.append(assignment_duedate)
            hw.append(assignment_discription)
            assignments.append(hw)
            print(assignments)
            assignments.sort()
            print(assignments)
            #save = db.execute("INSERT INTO assignments (user_id, priority, class, due_date, discription, name) VALUES(:user_id, :priority, :classs, :duedate, :discription, :name)",
               # user_id = session["user_id"], name = hw[1], priority = hw[0], classs = hw[2], duedate = hw[3], discription = hw[4])

            return redirect("/")
    else:
        return render_template("add_assignment.html", classes = classes, assignments = assignments)
# @app.route("/complete", methods=["GET", "POST"])
# def complete():
#     if request.method == "POST":
#             print(assignments)
#             completed_assignment = request.form.get("class")
#             print(completed_assignment)
#             assignments.remove(completed_assignment)
#             return render_template("index1.html")
#     else:
#         return render_template("complete.html", assignments = assignments)