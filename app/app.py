from flask import Flask, render_template, request

app = Flask(__name__)

votes = {
    "Candidate A": 0,
    "Candidate B": 0
}

@app.route("/", methods=["GET", "POST"])
def vote():
    if request.method == "POST":
        candidate = request.form.get("candidate")
        if candidate in votes:
            votes[candidate] += 1
    return render_template("index.html", votes=votes)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

