from flask import Flask,request
from flask_cors import CORS
import json
import helperFunctionsAPI as hp

app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['GET'])
def searchResult():
    song_input = request.args.get('song_name')
    artist_input = request.args.get('artist_name')
    album_input = request.args.get('album_name')
    
    response = hp.getDataFromQuery(song_input, artist_input, album_input)
    return json.dumps(response)

@app.route('/recommend', methods=['GET'])
def generateRecommend():
    featureVector = json.loads(request.args.get("query"))["featureVector"]
    recommendations = hp.getRecommendations(featureVector,"fromProfile",50,"")
    return json.dumps(recommendations)

if __name__ == "__main__":
    app.run(host='0.0.0.0')