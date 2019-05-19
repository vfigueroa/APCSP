from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    db = SQL("sqlite:///finance.db")
    rows = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = :user_id", user_id =  session["user_id"])
    print(rows)
    portfolio = []
    asset = 0
    for row in rows:
        shares = db.execute("SELECT SUM(bought_shares) FROM transactions WHERE symbol = :symbol", symbol =  row["symbol"])
        # shares comes out as [{'SUM(bought_shares)': number}]
        current_price = lookup(row["symbol"])
        print(current_price)
        real_shares = shares[0]["SUM(bought_shares)"]
        stock = {"symbol":row["symbol"], "shares":real_shares, "price_per_share":usd(current_price["price"]), "cost":(usd(float(current_price["price"]) * int(real_shares)))}
        #cost = (usd(float(current_price["price"]) * int(real_shares)))
        portfolio.append(stock)
        value = float(current_price["price"]) * int(real_shares) * 100
        print(value)

        for i in range(int(value)):
            asset = asset + 0.01
        print(portfolio)

    money = db.execute("SELECT cash FROM users WHERE id = :id", id =  session["user_id"])
    total_assets = usd(asset + (money[0]["cash"]))
    return render_template("index.html", portfolio = portfolio, money = usd(money[0]["cash"]), total_assets = total_assets)

@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        if not request.form.get("tickersymbol"):
            flash("must valid ticker symbol")

        shares = request.form.get("shares")
        if int(shares) < 0:
            flash("enter a valid number of shares")

        elif not lookup(request.form.get("tickersymbol")):
            flash("must provide valid ticker symbol")

        else:
            buy = lookup(request.form.get("tickersymbol"))
            trades = db.execute("INSERT INTO transactions (user_id, price, bought_shares, symbol) Values (:user_id, :stock_price, :bought_shares, :name)",
            user_id =  session["user_id"], stock_price = buy["price"], bought_shares = int(request.form.get("shares")), name = buy["name"])
            cost = float(buy["price"]) * int(request.form.get("shares"))
            old_cash = db.execute("SELECT cash FROM users WHERE id = :id",  id =  session["user_id"])

            if float(old_cash[0]["cash"]) > cost:
                db.execute("UPDATE users SET cash = :new_cash WHERE id = :id", new_cash = float(old_cash[0]["cash"]) - cost, id =  session["user_id"])
                return redirect("/")

            else:
                flash("insuficent funds")
                return redirect("/")

    else:
        return render_template("buy.html")



@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    history = db.execute("SELECT * FROM transactions WHERE user_id = :user_id", user_id =  session["user_id"])
    print(history)
    return render_template("history.html", history = history)


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
            return render_template("login.html")

        # Ensure password was submitted
        elif not request.form.get("password"):
            flash("must provide password")
            return render_template("login.html")

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = :username",
                          username=request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            flash("invalid username and/or password")
            return render_template("login.html")

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


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":

        if not request.form.get("tickersymbol"):
            flash("must provide a ticker symbol")

        elif not lookup(request.form.get("tickersymbol")):
            flash("must provide valid ticker symbol")

        else:
            quote = lookup(request.form.get("tickersymbol"))
            return render_template("quoted.html", name = quote["name"], price = quote["price"])

    else:
        return render_template("quote.html")

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
            return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        rows = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = :user_id", user_id =  session["user_id"])
        symbol = request.form.get("stock_name")
        current_shares = db.execute("SELECT SUM(bought_shares) FROM transactions WHERE symbol = :symbol AND user_id = :user_id", symbol = symbol, user_id =  session["user_id"])
        shares = current_shares[0]["SUM(bought_shares)"]
        if int(request.form.get("shares")) < 0:
            flash("must enter valid number of shares")

        elif int(request.form.get("shares")) > int(shares):
            message1 = ("You only have", current_shares, "shares of", symbol)
            flash(message1)

        else:
            symbol = request.form.get("stock_name")
            current_price = lookup(symbol)
            sell = db.execute("INSERT INTO transactions (user_id, price, bought_shares, symbol) VALUES (:user_id, :current_price, :sold_shares, :symbol)", user_id =  session["user_id"], current_price = current_price["price"], sold_shares = -1 * int(request.form.get("shares")), symbol = symbol)
            money = db.execute("SELECT cash FROM users WHERE id = :id", id =  session["user_id"])
            new_money = (current_price["price"] * (-1 * int(request.form.get("shares")))) + float(money[0]["cash"])
            new_cash = db.execute("UPDATE users SET cash = :new_money WHERE id = :id", new_money = new_money, id = session["user_id"])
            message2 = ("You have susscesfuly sold", int(shares), "of", symbol)
            flash(message2)
            return redirect("/")

    else:
        rows = db.execute("SELECT DISTINCT symbol FROM transactions WHERE user_id = :user_id", user_id =  session["user_id"])
        return render_template("sell.html", rows = rows)

@app.route("/name", methods=["GET", "POST"])
@login_required
def name():
    if request.method == "POST":

        if not request.form.get("username"):
            flash("must provide username")

        new_username = request.form.get("username")
        name = db.execute("UPDATE users SET username = :new_username WHERE id = :id", new_username = new_username, id = session["user_id"])
        message3 = ('You have changed your name to', new_username)
        flash(message3)
        return redirect("/")
    else:
        return render_template("name.html")


def errorhandler(e):
    """Handle error"""
    return apology(e.name, e.code)


# listen for errors
for code in default_exceptions:
    app.errorhandler(code)(errorhandler)
