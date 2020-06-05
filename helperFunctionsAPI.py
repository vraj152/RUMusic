import pandas as pd
import k_nn as knn
import youtube_dl
import getYouTubeVideoLink as gt

merged_file = pd.read_csv("data/mergedFile.csv")
item_profile = pd.read_csv("data/item_profile.csv")

def getDataFromQuery(song_input,artist_input,album_input):
    response = {}
    if(artist_input!=""):
        song_result = merged_file.loc[(merged_file["song"].str.lower()==song_input.lower()) | (merged_file["artist"].str.lower().str.contains(artist_input.lower())) | (merged_file["album"].str.lower()==album_input.lower())]
    else:
        song_result = merged_file.loc[(merged_file["song"].str.lower()==song_input.lower()) | (merged_file["album"].str.lower()==album_input.lower())]
    
    for index, row in song_result.iterrows():
        response[row.id] = row.to_dict()
    
    return response

def getRecommendations(featureVector, way, K, trackId):
    for i in range(len(featureVector)):
        if(i!=0):
            featureVector[i] = float(featureVector[i])

    recommendations = knn.getKNN(item_profile, way, K, trackId, featureVector)
    print(recommendations)
    response = {}
    for eachItem in recommendations.items():
        response[eachItem[0]] = getInformationFromID(eachItem[0])
    
    return response

def getInformationFromID(trackID):
    specificSongDetail = merged_file.loc[merged_file["id"]==trackID]
    temp = {}

    for index, row in specificSongDetail.iterrows():
        keys = row.keys()
        rowData = row        
    
    for eachKey in keys:
        temp[eachKey] = rowData[eachKey]
    
    return temp

#%%
def getMP3URL(songName):
    youtubeLink = "https://www.youtube.com" + gt.getYouTubeLink(songName)
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s'})
    ydl.add_default_info_extractors()

    result = ydl.extract_info(youtubeLink,download=False)

    if 'entries' in result:
        video = result ['entries'] [0]
    else:
        video = result
    for format in video['formats']:
        if format['ext'] == 'm4a':
            audio_url = format['url']
        
    print(audio_url)
    
getMP3URL("tu hi he aashiqui")