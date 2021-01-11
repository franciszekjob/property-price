# property-price
You can use this app to estimate You property price, based on its location, area, built year, number of rooms, level and state.

## Visit the app
App is currently hosted on heroku https://property-price.herokuapp.com/

## Description

The machine learning model was trained on over 2500 property data scraped form one of the biggest real estate website in Poland. The classifier bases on kNN algorithm and considers 6 features of each property:
* location
* area
* built year
* rooms
* level
* state

## Installing

To install the app download repo and install packages listed in `requirements.txt`.

## Built With

* Scikit-learn
* Flask
* Selenium
* Pandas
