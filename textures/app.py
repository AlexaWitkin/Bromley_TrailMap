"""
app.py
TrailMapInterface V1.0
this app.py includes all code that must be included in onload
"""

from flask import Flask, render_template
import HC_05

app = Flask(__name__)

open_button_chase_it = 'Open Trail'
delayed_button_chase_it = 'Delayed Trail'
closed_button_chase_it = 'Closed Trail'

# all code that needs to be executed at the start of the program
# makes sure the buttons have the appropriate initial text based on servo position
def onLoad():
    HC_05.loadCurrentStates()

    """
    Ensure correct labels are on Chase It buttons
    """
    if HC_05.chaseItState == 'Open Trail\n':
        global open_button_chase_it
        open_button_chase_it = 'OPEN'
    elif HC_05.chaseItState == 'Delayed Trail\n':
        global delayed_button_chase_it
        delayed_button_chase_it = 'DELAYED'
    elif HC_05.chaseItState == 'Closed Trail\n':
        global closed_button_chase_it
        closed_button_chase_it = 'CLOSED'


onLoad()

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
    return render_template("templates/buttons.html", title="Bromley TrailMap", openChaseItButtonText=open_button_chase_it, delayedChaseItButtonText=delayed_button_chase_it, closedChaseItButtonText=closed_button_chase_it)