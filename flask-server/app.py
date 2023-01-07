# imports for flask -- server

from flask import Flask
from flask_cors import CORS
from flask import request, jsonify

# imports for lyrics from animelyrics.com
import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import getLyrics

app = Flask(__name__)
CORS(app)


@app.route('/')
def hello_world():
    return 'This is a flask-server for Ani-oke'


@app.route('/getdata/<track>', methods=['GET', 'POST'])
def data_get(track):

    if request.method == 'POST':  # POST request
        print(request.get_text())  # parse as text
        return 'OK', 200

    else:  # GET request
        lyrics = getLyrics.GetLyrics(track)
        try:
            lyrics = lyrics.romaji()
        except:
            lyrics = "No Lyrics found"
        return jsonify({"tr": track, "ly": lyrics})


if __name__ == "__main__":
    app.run(debug=True)
