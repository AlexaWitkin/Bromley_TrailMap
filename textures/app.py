"""
app.py
TrailMapInterface V1.0
"""

from flask import Flask, render_template


app = Flask(__name__)

lock_button_text = 'Lock Door'
light_button_text = 'Light On'

# all code that needs to be executed at the start of the program
# makes sure the buttons have the appropriate initial text based on servo position
def onLoad():
    RS422.loadCurrentStates()
    if RS422.lightState == 'on\n':
        global light_button_text
        light_button_text = 'Light Off'


    if RS422.doorState == 'locked\n':
        global lock_button_text
        lock_button_text = 'Unlock Door'


onLoad()

@app.route("/lock_door", methods=["POST"])
def lock_door_url():
    print("Lock door")
    RS422.lock_door()
    return "ok"

@app.route("/unlock_door", methods=["POST"])
def unlock_door_url():
    print("Unlock door")
    RS422.unlock_door()
    return "ok"

@app.route("/light_on", methods=["POST"])
def light_on_url():
    print("Light on")
    RS422.light_on()
    return "ok"

@app.route("/light_off", methods=["POST"])
def light_off_url():
    print("Light off")
    RS422.light_off()
    return "ok"

@app.route("/", methods=["GET"])
def home():
    return render_template("templates/buttons.html", title="Bromley TrailMap", lockButtonText=lock_button_text, lightButtonText=light_button_text)