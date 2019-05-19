from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    print("Looks like I still work")
    counter = 0;
    if request.method =="POST":
        name = request.form.get("name")
        print(name)

        if request.form.get("show") == "1":
            counter = counter + 2
        if request.form.get("show") == "2":
            counter = counter + 1
        if request.form.get("show") == "3":
            counter = counter - 3
        if request.form.get("show") == "4":
            counter = counter + 2
        if request.form.get("show") == "5":
            counter = counter - 20

        color = request.form.get("color")
        if color == "blue":
            counter = counter + 1
        if color == "yellow":
            counter = counter + 2
        if color == "green":
            counter = counter + 3
        if color == "red":
            counter = counter + 4
        if color == "color is arbatrary and no two people see color the same anyways":
            counter = counter + 8

        if request.form.get("food") == "burger":
            counter = counter + 1
        if request.form.get("food") == "pizza":
            counter = counter + 2
        if request.form.get("food") == "tacos":
            counter = counter + 4
        if request.form.get("food") == "easymac":
            counter = counter - 3
        if request.form.get("food") == "sushi":
            counter = counter + 6
        if request.form.get("food") == "vindaloo":
            counter = counter + 8

        book = request.form.get("books")
        if book == "1":
            counter = counter + 10
        if book == "2":
            counter = counter + 1
        if book == "3":
            counter = counter + 2
        if book == "4":
            counter = counter + 5
        if book == "5":
            counter = counter + 5
        if book == "6":
            counter = counter - 5
        if book == "7":
            counter = counter + 3
        if book == "8":
            counter = counter + 3
        response = request.form.get("y/n")
        if counter <= 0:
            answer = "you dont seem to get out of your comfort zone. You like many of the same things that majority of Americans like. I suggest that you attempt to try new foods and read less common books."
        if counter > 0 and counter <= 5:
            answer = "you have some creativity, but still lack anything unique. You picked some of the most common answers."
        if counter > 5 and counter<= 10:
            answer = "you are officaly better than majoryity of quiz takers. You have quality tastes and picked uquie answers"
        if counter > 10 and counter<= 15:
            answer = "wow you deffinatly have some great tastes. I think we could have a great friendship"
        if counter > 15 and counter<= 20:
            answer = "finally someone that enjoys the same things as me"
            if counter > 20:
                answer = "you're either a lier or my clone, I personaly would discribe you as an absoulte weirdo."
        print(counter)

        if response == "yes":
            return render_template("answers.html", name = name, answer = answer)
        else:
            return render_template("wow.html", name = name)
    else:
        return render_template("index.html")