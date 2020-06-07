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

@app.route('/getmp3url', methods=['GET'])
def getMP3URL():
    response = {}
    artist = request.args.get('artist')
    songInput = request.args.get('input')
    songId = request.args.get('songid')
    
    response["url"] = hp.getMP3URL(songInput, artist)
    response["data"] = hp.getInformationFromID(songId)
    
    return json.dumps(response)

@app.route('/recommendByTrack', methods=['GET'])
def recommendByTrack():
    songId = request.args.get("input")
    response = hp.getRecommendations([], "fromTrackID", 15, songId)
    return json.dumps(response)

if __name__ == "__main__":
    app.run(host='0.0.0.0')