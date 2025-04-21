from  flask import  Flask, render_template, request, url_for, session
import os
from dotenv import load_dotenv
from pyexpat.errors import messages
from werkzeug.utils import redirect
load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("FLASK_SECRET_KEY")

birds_list = {"actually_grey.jpg": ["blue crane", "bloukransvoel", "bloukrans voel"],
         "bury_head.jpg": ["ostrich", "volstruis"],
         "dikkop.jpg": ["thick-knee", "thick knee", "dikkop"],
         "favorite.jpg": ["guinea-fowl", "guinea fowl", "tarentaal"],
         "kiewiet.jpg": ["crowned lapwing", "kiewiet"],
         "mossie.jpg": ["cape sparrow", "mossie"],
         "pikkie.jpg": ["penguin", "pikkewyn"],
         "quack.jpg": ["duck", "eend"],
         "sea_rat.jpg": ["seagull", "seemeeu"],
         "vink.jpg": ["geelvink", "vink"]}

mammals_list = {"ahooo.jpg": "wolf",
           "big_dolphin.jpg": ["orca", "killer whale"],
           "big_guinea_pig.jpg": "capybara",
           "don't_need_humans.jpg": "cat",
           "funny_bear.jpg": "panda",
           "man's_best_friend.jpg": "dog",
           "not_a_weasel.jpg": "ferret",
           "not_a_wolf.jpg": "coyote",
           "not_red.jpg": "red panda",
           "orange.jpg": "fox",
           "stripey_eyes.jpg": "goat",
           "trash_hamster.jpg": "rat",
           "trash_panda.jpg": "raccoon"}

reptiles_list = {"boring_pet.jpg": "bearded dragon",
            "looks_everywhere.jpg": "chameleon",
            "not_a_crocodile.jpg": "alligator",
            "not_a_tortoise.jpg": "turtle",
            "not_an_alligator.jpg": "crocodile",
            "round_toes.jpg": "gecko",
            "slither.jpg": "snake",
            "venomoos.jpg": ["komodo dragon", "monitor lizard"],
            "not_a_turtle.jpg": "tortoise"}

bird_image_list = list(birds_list.keys())
mammal_image_list = list(mammals_list.keys())
reptile_image_list = list(reptiles_list.keys())

@app.route("/")

def home():
    return render_template("home.html")

@app.route("/birds", methods=["GET", "POST"])

def birds():
    if "bird_index" not in session:
        session["bird_index"] = 0
    if "bird_reveal" not in session:
        session["bird_reveal"] = False

    message = ""
    current_index = session["bird_index"]
    current_image = bird_image_list[current_index]
    correct_answer = birds_list[current_image]

    if isinstance(correct_answer, str):
        correct_answer = [correct_answer.lower()]
    else:
        correct_answer = [ans.lower() for ans in correct_answer]

    try:
        if request.method == "POST":
            if "next" in request.form:
                session["bird_index"] = (current_index + 1) % len(bird_image_list)
                session["bird_reveal"] = False
                return redirect(url_for("birds"))

            elif "previous" in request.form:
                session["bird_index"] = (current_index - 1) % len(bird_image_list)
                session["bird_reveal"] = False
                return redirect(url_for("birds"))

            elif "bird_reveal" in request.form:
                session["bird_reveal"] = True
                return  redirect(url_for("birds"))

            elif "submit_guess" in request.form:
                guess = request.form["guess"].strip().lower()
                if guess in correct_answer:
                    message = f"✔️ Correct! It's a/an {correct_answer[0].lower()}"
                else:
                    message = "❌ Incorrect! Try again..."

        image_path = f"bird_pics/{current_image}"
        revealed_answer = correct_answer[0].title() if session.get("bird_reveal") else None

        return render_template("birds.html", image=image_path, message=message, answer=revealed_answer)

    except FileNotFoundError:
        return "File not found..."
    except (ValueError, TypeError):
        return "Invalid Input..."

@app.route("/mammals", methods=["GET","POST"])

def mammals():
    if "mammal_index" not in session:
        session["mammal_index"] = 0
    if "mammal_reveal" not in session:
        session["mammal_reveal"] = False

    message = ""
    current_index = session["mammal_index"]
    current_image = mammal_image_list[current_index]
    correct_answer = mammals_list[current_image]

    if isinstance(correct_answer, str):
        correct_answer = [correct_answer.lower()]
    else:
        correct_answer = [ans.lower() for ans in correct_answer]

    try:
        if request.method == "POST":

            if "next" in request.form:
                session["mammal_index"] = (current_index + 1) % len(mammal_image_list)
                session["mammal_reveal"] = False
                return redirect(url_for("mammals"))

            elif "previous" in request.form:
                session["mammal_index"] = (current_index - 1) % len(mammal_image_list)
                session["mammal_reveal"] = False
                return redirect(url_for("mammals"))

            elif "mammal_reveal" in request.form:
                session["mammal_reveal"] = True
                return redirect(url_for("mammals"))

            elif "submit_guess" in request.form:
                guess = request.form["guess"].strip().lower()
                if guess in correct_answer:
                    message = f"✔️ Correct! It's a/an {correct_answer[0].title()}"
                else:
                    message = "❌ Incorrect! Try again..."

        image_path = f"mammal_pics/{current_image}"
        revealed_answer = correct_answer[0].title() if session.get("mammal_reveal") else None

        return render_template("mammals.html", message=message, image=image_path, answer=revealed_answer)

    except FileNotFoundError:
        return "File not found..."
    except (ValueError, TypeError):
        return "Invalid input..."

@app.route("/reptiles", methods=["GET", "POST"])

def reptiles():
    if "reptile_index" not in session:
        session["reptile_index"] = 0
    if "reptile_reveal" not in session:
        session["reptile_reveal"] = False

    message = ""
    current_index = session["reptile_index"]
    current_image = reptile_image_list[current_index]
    correct_answer = reptiles_list[current_image]

    if isinstance(correct_answer, str):
        correct_answer = [correct_answer.lower()]
    else:
        correct_answer = [ans.lower() for ans in correct_answer]

    try:
        if request.method == "POST":

            if "next" in request.form:
                session["reptile_index"] = (current_index + 1) % len(reptiles_list)
                session["reptile_reveal"] = False
                return redirect(url_for("reptiles"))

            elif "previous" in request.form:
                session["reptile_index"] = (current_index - 1) % len(reptiles_list)
                session["reptile_reveal"] = False
                return redirect(url_for("reptiles"))

            elif "reptile_reveal" in request.form:
                session["reptile_reveal"] = True
                return redirect(url_for("reptiles"))

            elif "submit_guess" in request.form:
                guess = request.form["guess"].lower()
                if guess in correct_answer:
                    message = f"✔️ Correct! It's a/an {correct_answer[0].title()}"
                else:
                    message = "❌ Incorrect! Try again..."

        image_path = f"reptile_pics/{current_image}"
        revealed_answer = correct_answer[0].title() if session.get("reptile_reveal") else None

        return render_template("reptiles.html", message=message, image=image_path, answer=revealed_answer)

    except FileNotFoundError:
        return "File not found..."
    except (ValueError, TypeError):
        return "Invalid Input..."

if __name__ == "__main__":
    app.run(debug=True)