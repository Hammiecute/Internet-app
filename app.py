from flask import Flask, render_template, request

# instatiate or initialize
app = Flask(__name__)


@app.route("/", methods=["POST", "GET"])
def home():
    location = request.form['location']
    network = request.form['network']
    network_use = request.form['network-use']
    rating = request.form['rating']

    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)
