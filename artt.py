# A simple webapp to simulate user login and logout

from flask import Flask, render_template, redirect, url_for, request, session
from flask_session import Session

app = Flask(__name__)

app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

credentials = ('admin', 'admin')

@app.route('/')
def index():
    # Try and see if logged_in session variable exists, if not set it to false
    try:
        session["logged_in"] == True
    except KeyError:
        session["logged_in"] = False
    # nothing to show in the index, redirect to login page
    return redirect(url_for('login'))


@app.route('/login')
def login(alert="Login to continue", alert_type="alert-primary"):
    # set default alert and alert type for login page
    if request.args.get('failed'):
        # if user has typed wrong credentials it reports as 'failed'
        alert = "Try again! Validation failed :("
        alert_type = "alert-danger"
    elif request.args.get('invalid'):
        # if user tries to access welcome page with out logging in first reports 'invalid'
        alert = "You must login to continue :("
        alert_type = "alert-warning"

    if session['logged_in']:
        # if user is logged in take them to welcome page
        return redirect(url_for('welcome'))
    # if not logged in render the login page
    return render_template('login.html', alert=alert, alert_type=alert_type)


@app.route('/welcome')
def welcome():
    if session['logged_in']:
        # if user is logged in only then render the welcome page
        return render_template('welcome.html')
    else:
        # otherwise take them to login page
        return redirect(url_for('login', invalid="true"))


@app.route('/validate', methods=['POST'])
def validate():
    if session['logged_in'] or request.form.get('username') == credentials[0] and request.form.get('password') == credentials[1]:
        # if user is logged in or they give in the correct credentials then take them to welcome page
        session['logged_in'] = True
        return redirect(url_for('welcome'))
    else:
        # if not logged in or they give wrong credentials take them to login page
        return redirect(url_for('login', failed='true'))


@app.route('/logout')
def logout():
    # logout method logs out the user and takes them back to login page
    session['logged_in'] = False
    return redirect(url_for('login'))
