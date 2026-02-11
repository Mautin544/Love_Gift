import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("valentine.html")

if __name__ == "__main__":
    # This port logic is required for Render
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)