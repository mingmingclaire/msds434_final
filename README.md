# Covid19
Project contains a flask app that queries google big query storage (holds two arima models and etl of NYT Covid19 dataset) and returns latest cases/deaths stats for US and territories, along with prediction for cases/deaths 30 days out.
Vyzytor-patch-1 is the development environment, subject to linting from both CircleCI and GitActions. Master is the production environment that is linked to Google Cloud Platform.

main.py – the primary application file that retrieves data from Google Big Query and uses flask to deliver the data and render the web page

templates/page.html – the web page

static/styles/covid19.css – style sheet for the web page

static/styles/CovidTransparent.jpg – image used on the web page. Note: image is free and sourced from unsplash.com

app.yaml – configuration file for application

requirements.txt – holds all requirements (includes) for application. pip install -r requirements.txt will install all requirements with one command

.github/workflows/main.yml – workflow file for GitActions

.github/workflows/linter.yml – lint file for GitActions
