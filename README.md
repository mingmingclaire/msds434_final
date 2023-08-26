# Movie Review Text Sentiment Classification App

Project contains a flask app that queries google big query storage (holds a classification model based on Kaggle Movie Review) and returns Positive or Negative category whichever has a high probability output from the model. Master is the production environment that is linked to Google Cloud Platform.

main.py – the primary application file that retrieves data from Google Big Query to train the model and uses flask to deliver the data and render the web page

templates/page.html – the web page

static/styles/moviereview.css – style sheet for the web page

static/styles/Movies.jpg – image used on the web page.

app.yaml – configuration file for application

requirements.txt – holds all requirements (includes) for application. pip install -r requirements.txt will install all requirements with one command

.github/workflows/main.yml – workflow file for GitActions

.github/workflows/linter.yml – lint file for GitActions
