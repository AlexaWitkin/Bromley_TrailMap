"""
app.py
TrailMapInterface V1.0
"""

from flask import Flask, render_template
import HC_05

app = Flask(__name__)

@app.route("/open_button_chase_it", methods=["POST"])
def open_button_chase_it_url():
    print("Open Chase It")
    HC_05.chaseIt_open()
    return "ok"

@app.route("/delayed_button_chase_it", methods=["POST"])
def delayed_button_chase_it_url():
    print("Delayed Chase It")
    HC_05.chaseIt_delayed()
    return "ok"

@app.route("/closed_button_chase_it", methods=["POST"])
def closed_button_chase_it_url():
    print("Closed Chase It")
    HC_05.chaseIt_closed()
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("templates/buttons.html", title="Bromley TrailMap")

app.run(host='0.0.0.0')