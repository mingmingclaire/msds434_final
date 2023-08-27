from flask import Flask, render_template, request
#from flask import jsonify
import google.auth
import pandas as pd
from google.cloud import bigquery
import sys 

app = Flask(__name__)

credentials, project_id = google.auth.default(
    scopes=["https://www.googleapis.com/auth/cloud-platform"]
)
project_id = 'finalproject-396805'
bqclient = bigquery.Client(credentials= credentials,project=project_id)

@app.route('/get_data')
def input():
    return render_template('input.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():

    if request.method == 'POST':
        data = request.form
        user_review = str(data['review_text'])

        prediction_input = [{
            "review_text": user_review
        }]

        df = pd.DataFrame(
            prediction_input,
            columns=[
                "review_text"
            ]
        )
    
    job_config = bigquery.LoadJobConfig(
        schema = [
            bigquery.SchemaField('review_text', bigquery.enums.SqlTypeNames.STRING)
        ],
        write_disposition = 'WRITE_TRUNCATE',
    )
    
    ingest = bqclient.load_table_from_dataframe(
        df, 'finalproject-396805.imdb_movie_reviews.movie_review_input', job_config=job_config
    )

    ingest.result()

    query_string= """
    SELECT
        predicted_review_label
    FROM
        ML.PREDICT(MODEL `finalproject-396805.imdb_movie_reviews.train_model1`,
            ( 
                SELECT 
                    ML.NGRAMS(bt.words_array, [1,2]) as ngrams
                FROM  
                    (SELECT 
                        REGEXP_EXTRACT_ALL(LOWER(r.review_text ), '[a-z]+') as words_array
                    FROM (SELECT string_field_0 as review_text 
                          FROM `finalproject-396805.imdb_movie_reviews.movie_review_new_dp`
                          WHERE string_field_0 != 'review_text') r
                    ) bt
            )
        ) 
    """
    query_job = bqclient.query(query_string)
    results = query_job.result()
    # for row in results:
    #     Movie_Review_Text = row.user_review
    #     Pred_label = row.predicted_review_label

    val = {"MovieReviewUserInput":user_review, "PredictedSentimentCategory":results}

    return render_template("page.html", title="Predicted Movie Review Sentiment Category",jsonfile = val)

  
if __name__ == '__main__':

    #predict()
 
    #app.run(host='127.0.0.1', port=8080, debug = True)
    app.run(host='0.0.0.0')
