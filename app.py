from flask import Flask, render_template, request
from ai.bot_engine import get_bot_response

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/get", methods=["POST"])
def chatbot_response():
    user_message = request.form["message"]
    bot_reply = get_bot_response(user_message)
    return render_template("index.html", bot_response=bot_reply, user_input=user_message)

if __name__ == "__main__":
    app.run(debug=True)
