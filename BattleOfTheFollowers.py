# PSEUDOCODE
'''
This program will access Spotify's API using the client ID and secret provided to the user upon registration as a developer on the Spotify website.
It will then query the amount of followers Drake and Rihanna currently have.
Lastly it will use Matplotlib to print a graph showing the follow count of each artist.
'''

import sys
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import numpy as np

import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials



# This will allow access into Spotify's API using the client ID and secret
#provided to the user upon registration as a developer on the Spotify
client_credentials_manager = SpotifyClientCredentials(client_id = 'your_client_id',

                                                      client_secret = 'your_client_secret',
                                                      )

#Declare sp variable that makes a call to the API when used
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


#Declaring empthy list
artists_uri = []
artists_name = []
artists_followers = []

#Using numpy to declare x as a range for the tick distance on the graph
x = np.arange(4)


def artist_details(self):
        'To go through the nested dictionaries and add the artist uri, name, and follower amount'
    
        for i, item in enumerate(self['artists']['items']):
                artists_uri.append(item['id'])
                artists_name.append(item['name'])
                artists_followers.append(item['followers']['total'])


def millions(x, pos):
    'The two args are the value and tick position'
    
    return '%1.1fM' % (x * 1e-6)


# Looking up both artist in the API
artist_1 = sp.search('drake', limit=1, offset=0, type='artist', market=None)

artist_2 = sp.search('rihanna', limit=1, offset=0, type='artist', market=None)


# Calling the artist detail methond to retive artist information
artist_details(artist_1)
artist_details(artist_2)


#Formating the graph and assigning the x and y axis
formatter = FuncFormatter(millions)
fig, axs = plt.subplots()
axs.yaxis.set_major_formatter(formatter)
plt.bar(artists_name,artists_followers)
    

#Setting graph axis labels and title
fig.suptitle('Spotify followers to date')
axs.set_xlabel('Artists')
axs.set_ylabel('Followers')


#Print the graph
plt.show()

