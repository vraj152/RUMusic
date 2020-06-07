# RUMusic
Song recommendations using K-NN Algorithm.

* Used a subset of data released by EchoNest in a challenge called [Milion Song Dataset Challenge](http://millionsongdataset.com/).
* I haven't uploaded data used to build this application. (Exceeded the storage limit ~128 MB.)
* Data is freely available at -> [Here](https://components.one/).  
* Dataset information -> [Here](https://components.one/datasets/billboard-200/)
* Developed web portal using Spring framework, for that I needed album art and artist image. For that I scraped data from spotify.
  * There are ~340K songs, and scrapping them and adding them in appropriate dataframe was headache. So, I scrapped data based on albums.
  * Fetched all unique albums and scrap data, and append accordingly. It saved hell lot of time. :relieved:
  * [Scraping code](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/util_one_time/generatingMoreData.py#L4)
* After getting all the data -> I used K-NN algorithm to find K nearest neighbours using measure called _Cosine distance_. And those who have more similarity, will be recommended to user.
* Also for the web portal I needed MP3 file. So, I did following steps.
  * Scrapped YouTube for the youtube link of particular track.
    * _For Example:_ If song is [faded by Ben Harper](https://open.spotify.com/track/3Bt5vZFjstranJlqhwpuZz) then by simply scrapping YouTube's first video won't really help.
    It will definitely give you results based on popularity, hence faded by Alan Walker. So, search query should be <br> "_(song_name)+by+(artist_name)_".
    Scrapping code -> [Here](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/getYouTubeVideoLink.py#L4)
  * From YouTube video link, I used library called [youtube-dl](https://github.com/ytdl-org/youtube-dl) for getting temporary MP3 URL. And used it on front end.
* Finally developed web API using Flask. End points are as following.
  * [(/search) searchResult](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/flaskAPI.py#L10):- Fetched the data based on query given by the user.
    * Query Parameter: song_input, artist_input and album_input. Uses [getDataFromQuery](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/helperFunctionsAPI.py#L9) as helper function. <br>
    It fetches data from the .csv file.
  * [(/recommend) generateRecommend](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/helperFunctionsAPI.py#L21):- Generates recommendations from the input data given by the user. (More in JAVA repo.) <br>
    * Query Parameter: FeatureVector provided from the client. Used as input to our KNN algorithm and generates K=50 nearest neighbors and recommends the same.<br>
    Helper function is -> [getRecommendations](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/helperFunctionsAPI.py#L21).
  * [(/getmp3url) getMP3URL](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/flaskAPI.py#L24):- It generates MP3 URL for the track seleced by the user.<br>
    * Query Parameter: Artist name, song name, song id. Uses [this](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/helperFunctionsAPI.py#L46) as helper function. It returns MP3 URL of that song.
  * [(/recommendByTrack) recommendByTrack](https://github.com/vraj152/RUMusic/blob/3753826ae6c062e0bfe8de34109ca052ff12b3fc/flaskAPI.py#L37):- It recommends similar songs to the song, which user wanted to play.<br>
    * Query Parameter: Song id. And it uses the same helper function which we used to recommend songs from the feature vector.
      * To bifurcate both the methods -> I used one parameter called _way_. <br>
      If we were to recommend songs from the feature vector extracted from the user input then way would be "fromProfile". Otherwise "fromTrackID".
<br><br>

* Web portal is developed in Spring framework(J2EE), which I will be uploading in another repo called "RUMusicPortal".
* Output demo:
<p align="center">
  <img src="output/NewGIF.gif" width="450" title="Application Output">
</p>
* Let me know if you have got question.:raising_hand:
