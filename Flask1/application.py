from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print("yo, index")
    if request.method =="POST":
        name = request.form.get("name")
        print(name)
        if request.form.get("quest") == "grail":
            quest = "seek the grail"
        else:
            quest = "join the ratrace"
        color = request.form.get("color")
        if color == "oops":
            return render_template("oops.html", name = name)
        else:
            return render_template("cross.html", name = name, quest = quest)
    else:
        return render_template("index.html")