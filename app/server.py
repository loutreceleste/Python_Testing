import json
from datetime import datetime
from flask import Flask, render_template, request, redirect, flash, url_for
from jinja2 import Environment, FileSystemLoader, select_autoescape


# Function to load clubs from JSON file
def load_clubs():
    with open('clubs.json') as c:
         list_of_clubs = json.load(c)['clubs']
         return list_of_clubs

# Function to load competitions from JSON file
def load_competitions():
    with open('competitions.json') as comps:
         list_of_competitions = json.load(comps)['competitions']
         return list_of_competitions

# Flask application setup
app = Flask(__name__)
app.secret_key = 'something_special'
app.template_folder = '/home/edward/Documents/Repos/OpenClassRooms/Python_Testing/templates'

# Load competitions and clubs data
competitions = load_competitions()
clubs = load_clubs()

# Jinja2 environment setup
env = Environment(
    loader=FileSystemLoader(app.template_folder),
    autoescape=select_autoescape(['html', 'xml'])
)
env.globals['datetime'] = datetime
env.filters['strftime'] = lambda dt, fmt: dt.strftime(fmt) if dt else ''

# Home route - renders the index.html template
@app.route('/')
def index():
    return render_template('index.html')

# Route to handle form submission and display a summary
@app.route('/showSummary', methods=['POST'])
def show_summary():
    club_found = [club for club in clubs if club['email'] == request.form['email']]
    if club_found:
        current_time = datetime.now()
        club = [club for club in clubs if club['email'] == request.form['email']][0]
        return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)
    else:
        flash('No club associated with this email, please try again.')
        return render_template('index.html')

# Route to display booking page for a specific competition and club
@app.route('/book/<competition>/<club>')
def book(competition, club):
    found_club = [c for c in clubs if c['name'] == club][0]
    found_competition = [c for c in competitions if c['name'] == competition][0]
    if found_club and found_competition:
        return render_template('booking.html', club=found_club, competition=found_competition)
    else:
        flash("Something went wrong-please try again")
        return render_template('welcome.html', club=club, competitions=competitions)

# Route to handle place purchase and update competition and club data
@app.route('/purchasePlaces', methods=['POST'])
def purchase_places():
    competition = [c for c in competitions if c['name'] == request.form['competition']][0]
    club = [c for c in clubs if c['name'] == request.form['club']][0]
    club_name = request.form['club']
    current_time = datetime.now()
    try:
        places_required = int(request.form['places'])
    except ValueError:
        # Handle the case where the conversion fails
        flash("Invalid number of places selected. Please enter a valid number.")
        return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)

    if int(club['points']) - places_required < 0:
        flash("You can't book more places than you have!")
        return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)
    else:
        if competition:
            club_booking = competition.get(club_name, None)

            if club_booking:
                if (competition[club_name] + places_required) <= 12:
                    # Update competition, club, and flash message
                    competition[club_name] += places_required
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
                    club['points'] = int(club['points']) - places_required
                    flash('Great-booking complete!')
                    return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)
                else:
                    flash("You can't book more than 12 places by competition")
                    return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)
            else:
                if places_required <= 12:
                    # Update competition, club, and flash message
                    competition[club_name] = places_required
                    competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
                    club['points'] = int(club['points']) - places_required
                    flash('Great-booking complete!')
                    return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)
                else:
                    flash("You can't book more than 12 places by competition")
                    return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)

        # Update competition, club, and flash message
        competition['numberOfPlaces'] = int(competition['numberOfPlaces']) - places_required
        club['points'] = int(club['points']) - places_required
        flash('Great-booking complete!')
        return render_template('welcome.html', club=club, competitions=competitions, current_time=current_time)

# Route to display points information
@app.route('/pointsDisplay')
def points_display():
    return render_template('points.html', clubs=clubs)

# Route to handle logout and redirect to the index page
@app.route('/logout')
def logout():
    return redirect(url_for('index'))
