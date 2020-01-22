# PSEUDOCODE
'''

'''
import sys

import matplotlib.pyplot as plt

from matplotlib.ticker import FuncFormatter

import numpy as np



import spotipy

import spotipy.util as util

from spotipy.oauth2 import SpotifyClientCredentials



client_credentials_manager = SpotifyClientCredentials(client_id='your_client_id',

                                                      client_secret='your_client_secret',

                                                      )



sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)



artists_uri = []

artists_name = []

artists_followers = []



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





artist_1 = sp.search('drake', limit=1, offset=0, type='artist', market=None)

artist_2 = sp.search('rihanna', limit=1, offset=0, type='artist', market=None)



artist_details(artist_1)

artist_details(artist_2)





formatter = FuncFormatter(millions)



fig, axs = plt.subplots()

axs.yaxis.set_major_formatter(formatter)

plt.bar(artists_name,artists_followers)



fig.suptitle('Spotify followers to date')

axs.set_xlabel('Artists')

axs.set_ylabel('Followers')



plt.show()
