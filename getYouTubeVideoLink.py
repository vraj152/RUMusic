from bs4 import BeautifulSoup
import requests

def getYouTubeLink(songName):
    youTubeLink = ""
    baseURL = "https://www.youtube.com/results?search_query="
    
    try:
        page = requests.get(baseURL + songName)
        soup = BeautifulSoup(page.content,'html.parser')
        h3Results = soup.findAll("h3",{"class":"yt-lockup-title"})
        youTubeLink = h3Results[0].find("a")['href']
        if(youTubeLink==None):
            getYouTubeLink(songName)
        return youTubeLink
    except:
        youTubeLink = getYouTubeLink(songName)
        return youTubeLink