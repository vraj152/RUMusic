from scipy import spatial
from itertools import islice

def take(n, iterable):
    return dict(islice(iterable, n))
    
def getProfileFromTrackID(item_profile, trackID):
    query_vector = item_profile.loc[item_profile["id"]==trackID]
    for index,row in query_vector.iterrows():
        query_vector = row.to_list()
    
    return query_vector

def getKNN(item_profile, way, K, trackID, query_vector):
    if(way=="fromTrackID"):
        query_vector = getProfileFromTrackID(item_profile, trackID)

    each_item_vector = item_profile.iloc[:,1:11].values
    each_item_id = item_profile.iloc[:,0].values

    cosine_distances = {}
    i = 0

    while (i != len(each_item_vector)):
        cosine_distance = spatial.distance.cosine(query_vector[1:11],each_item_vector[i])
        cosine_distances[each_item_id[i]] = (1-cosine_distance)
        i = i + 1
    
    cosine_distances = {k: v for k, v in sorted(cosine_distances.items(), key=lambda item: item[1], reverse=True)}

    k_items = take(K, cosine_distances.items())
    return k_items