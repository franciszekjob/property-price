from flask import Flask, render_template, request
from predicter import predict, load_model

app = Flask(__name__)

property_model = load_model('pickle_model_v3.pkl')


@app.route('/', methods=["GET"])
def index():
    return render_template('index.html', title='Home')


@app.route('/', methods=['POST'])
def calculate():
    location = int(request.form['location'])
    area = float(request.form['area'])
    year = int(request.form['year'])
    rooms = int(request.form['rooms'])
    level = int(request.form['level'])
    state = int(request.form['state'])
    city = int(request.form['city'])

    prediction = predict(location, area, year, rooms, level, state, property_model)

    if level == 0:
        level = "Parter"
    else:
        level = f"Poziom {level}"

    cities = [
        'Kraków', 'Warszawa', 'Łódź'
    ]

    locations = [
        'Bieńczyce',
        'Bieżanów - Prokocim',
        'Bronowice',
        'Dębniki',
        'Grzegórzki',
        'Krowodrza',
        'Łagiewniki - Borek Fałęcki',
        'Mistrzejowice',
        'Nowa Huta',
        'Podgórze',
        'Podgórze Duchackie',
        'Prądnik Biały',
        'Prądnik Czerwony',
        'Śródmieście',
        'Stare Miasto',
        'Swoszowice',
        'Wzgórza Krzesławickie',
        'Zwierzyniec'
    ]

    states = [
        'Do remontu',
        'Do wykończenia',
        'Do zamieszkania'
    ]

    context = {
        'prediction': prediction,
        'location': locations[location],
        'area': area,
        'year': year,
        'rooms': rooms,
        'level': level,
        'state': states[state],
        'city': cities[city]
    }

    return render_template('calculate.html', title='Home', context=context)


if __name__ == "__main__":
    app.run()
