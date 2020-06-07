from bs4 import BeautifulSoup
import requests

def getYouTubeLink(songName, artist):
    youTubeLink = ""
    baseURL = "https://www.youtube.com/results?search_query="
    
    try:
        page = requests.get(baseURL + songName + " by " + artist)
        soup = BeautifulSoup(page.content,'html.parser')
        h3Results = soup.findAll("h3",{"class":"yt-lockup-title"})
        youTubeLink = h3Results[0].find("a")['href']
        if(youTubeLink==None):
            getYouTubeLink(songName, artist)
        return youTubeLink
    except:
        youTubeLink = getYouTubeLink(songName, artist)
        return youTubeLink