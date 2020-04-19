import time
import random
import giphy_client 
from giphy_client.rest import ApiException
from pprint import pprint
from App.settings import GIPHY_API_KEY

class BusyGiphyClient():
    @staticmethod
    def get_giphy_shuffle_image_url(query_term):
        # create an instance of the API class
        api_instance = giphy_client.DefaultApi()
        value = api_instance.gifs_search_get(GIPHY_API_KEY, query_term, limit=100) 
        data_length = len(value.data)
        if (value and value.data and data_length > 0):
            return value.data[random.randint(0, data_length-1)].images.downsized_large.url
        else:
            return None

    @staticmethod
    def get_giphy_top_search_image_url(query_term):
        # create an instance of the API class
        api_instance = giphy_client.DefaultApi()
        value = api_instance.gifs_search_get(GIPHY_API_KEY, query_term, limit=1) 
        if (value and value.data and len(value.data) > 0):
            return value.data[0].images.downsized_large.url
        else:
            return None

    @staticmethod
    def get_giphy_random_image_url(query_term):
        # create an instance of the API class
        api_instance = giphy_client.DefaultApi()
        value = api_instance.gifs_random_get(GIPHY_API_KEY, tag=query_term) 
        if (value and value.data):
            return value.data.image_url
        else:
            return None