import time
import giphy_client
from giphy_client.rest import ApiException
from pprint import pprint
from App.settings import GIPHY_API_KEY

def get_giphy_api_client(query):
    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    q = 'cheeseburgers' # str | Search query term or prhase.
    limit = 1 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)
    return api_instance.gifs_search_get(GIPHY_API_KEY, query, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)
 
def get_busy_url_for_person(person_id):
    return get_giphy_api_client('cheeseburgers')

def get_not_busy_url_for_person(person_id):
    return get_giphy_api_client('frenchfries')