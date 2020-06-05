import pandas as pd
import generatingMoreData as gmd
import pickle
from tqdm import tqdm

spotify_data = pd.read_csv(r'data/spotifyCSV.csv')

#%%
"""
To find unique albums
"""
unique_albums = spotify_data.album.unique()

#%%
"""
Finding ID of first track in each album
"""
allId = []
for eachAlbum in unique_albums:
    allId.append(spotify_data.loc[spotify_data['album']==eachAlbum, 'id'].iloc[0])

#%%
"""
Mapping each ID with album 
"""

idToAlbum = {}
for i in range(len(allId)):
    idToAlbum[allId[i]] = unique_albums[i]
    
#%%
"""
Web scraps all data required and saves as piclke file so that we
can use it for later without web scrapping.
"""

temp = {}
for eachTrack in allId:
    response = gmd.getMetaInfo(eachTrack)
    temp[idToAlbum[eachTrack]] = {
        "albumart": response[0] , 
        "artistURL": response[1],
        "artist_image": response[2],
        "artist_id": response[3]
    }

with open('data/entireTemp.pickle', 'wb') as handle:
    pickle.dump(temp, handle, protocol=pickle.HIGHEST_PROTOCOL)
    
#%%
"""
Iterates through entire dataframe and it takes each album -> and
fetches appropriate album data (artist_image, artist_id, albumart
, artistURL) from "temp" dictionary. And it appends all details in
new dataframe called temp_df. 

* And finally merging it with spotify_data dataframe to get final
dataframe. (With common column ID) And then convert into csv.
"""

temp_new_columns = ["id","albumart", "artistURL", "artist_image", "artist_id"]
temp_df = pd.DataFrame(columns = temp_new_columns)

not_found = []
new_temp = {}
for index, row in tqdm(enumerate(spotify_data.itertuples()),position=0, leave=True):
    new_temp.clear()
    uString = ""    
    try:
        if(row.album=="TRUE"):
            uString = "True"
        elif(row.album[0]=="0" and row.album[2]==":"):
            uString = row.album[1:]
        elif(row.album =="99.90%"):
            uString = "99.9%"
            
        new_temp["id"] = row.id
        if(uString==""):
            new_temp.update(temp[row.album])
        else:
            new_temp.update(temp[uString])
            
        temp_df = temp_df.append(new_temp, ignore_index= True, sort=False)
    except:
        not_found.append([row.album])
        
result = pd.merge(spotify_data, temp_df, on = "id")
result.to_csv(r'data/mergedFile.csv', index=False)