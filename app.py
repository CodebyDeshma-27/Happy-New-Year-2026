from flask import Flask, render_template, request
from datetime import datetime
import random

app = Flask(__name__)

QUOTES = [
    "New year. New energy. Same unstoppable you. 🚀",
    "May 2026 reward your discipline more than your luck ✨",
    "Dreams don’t expire — they evolve. Welcome 2026 🌱",
    "Small steps daily create giant wins yearly 🧠🔥",
    "Let consistency be your superpower in 2026 ⚡"
]

@app.route("/", methods=["GET", "POST"])
def home():
    name = None
    message = None
    quote = None

    if request.method == "POST":
        name = request.form.get("name")
        message = f"🎉 Happy New Year 2026, {name}! 🎆"
        quote = random.choice(QUOTES)

    return render_template(
        "index.html",
        message=message,
        quote=quote
    )

if __name__ == "__main__":
    app.run(debug=True)
