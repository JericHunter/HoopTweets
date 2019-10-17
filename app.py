from flask import Flask, render_template, request
import requests
import json
import bs4
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("base.html")


@app.route('/player')
def player():
    player_query = request.args.get("q", None)
    if not player_query:
        return f"Couldn't find tweets for {player_query}"

    auth_params = {
        'app_key':'rCguhoSNkQGrj2WfowC0iI4rj',
        'app_secret':'nMU6MarVejiIpTPCx7aYrHwuiawbRywh13lXhXOuymbz77BieZ',
        'oauth_token':'992987135723687936-bJDIDdI8frBErPbyx6V9rYuneWtm3CX',
        'oauth_token_secret':'tkYmrFRQJFWYpS33AzAighKPIjTin4UJCOEcWRWeLvH2G'
    }

    # Creating an OAuth Client connection
    auth = OAuth1(
        auth_params['app_key'],
        auth_params['app_secret'],
        auth_params['oauth_token'],
        auth_params['oauth_token_secret']
    )

    q = f'{player_query} -filter:retweets AND -filter:replies'
    # url according to twitter API
    url_rest = "https://api.twitter.com/1.1/search/tweets.json"

    params = {'q': q, 'count': 1, 'lang': 'en',  'result_type': 'recent'}
    results = requests.get(url_rest, params=params, auth=auth)
    tweets = results.json()

    messages = [BeautifulSoup(tweet['text'], 'html5lib').get_text() for tweet in tweets['statuses']]
    print(messages)
    """Return homepage."""
    return render_template('player.html', q=q, tweets=tweets, messages=messages)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=os.environ.get('PORT', 5000))
