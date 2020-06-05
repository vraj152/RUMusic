from bs4 import BeautifulSoup
import requests

def getMetaInfo(trackID):
    albumArt = ""
    artistURL = ""
    artistImage = ""
    artistID = ""

    page = requests.get("https://open.spotify.com/track/" + str(trackID))
    soup = BeautifulSoup(page.content,'html.parser')

    divs = soup.findAll("div",{"class":"bg lazy-image"})
    
    for eachDiv in divs:
        if "https:" not in eachDiv.get("data-src"):
            artistImage = "https:" + eachDiv.get("data-src")
        
    allMetas = soup.findAll("meta")
    
    flag1, flag2 = False, False
        
    for row in allMetas:
        if(not (flag1 and flag2)):
            if(row.get('property')=="og:image"):
                albumArt = row.get('content')
                flag1 = True
            if(row.get('property')=="music:musician"):
                artistURL = row.get('content')
                artistID = artistURL.split("/")[4]
                flag2 = True
        else:
            break
     
    return (albumArt,artistURL,artistImage,artistID)