"""
Ask Noah Shows Module.
Contains shows/feeds/helper methods
"""

FEED_BURNER = 'http://feeds2.feedburner.com/'
FEED_PRESS = 'http://feedpress.me/'
ASKNOAH_COM = 'http://podcast.asknoahshow.com'

# public methods

def get_all_shows():
    """
    Retuns all JB Shows
    """
    return _shows()

def get_active_shows():
    """
    Returns all JB shows where 'archive' is False
    """
    active_shows = {}

    for item_name, data in _shows().iteritems():
        if not data['archived']:
            active_shows[item_name] = data

    return active_shows

def get_archived_shows():
    """
    Returns all JB shows where 'archive' is True
    """
    archived_shows = {}

    for item_name, data in _shows().iteritems():
        if data['archived']:
            archived_shows[item_name] = data

    return archived_shows

def sort_shows(shows):
    """
    Returns shows sorted in a list where show
    name (kodi string index) is the outer
    """
    return sorted(shows.items(), key=_sort_key)



# private methods
def _shows():
    """
    List of available Ask Noah Show episodes.
    Indexes and plot point to resources/language/yourlanguageHere/strings.xml
    """

    shows = {}
    
    # Ask Noah
    shows[30000] = {
        'feed': 'http://podcast.asknoahshow.com/rss',
        'feed-low': 'http://podcast.asknoahshow.com/rss',
        'feed-audio': 'http://podcast.asknoahshow.com/rss',
        'image': 'asknoah.png',
        'plot': 30200,
        'genre': 'Technology',
        'archived': False
        }    


    return shows

def _sort_key(show):
    """
    Sets the key for sorting to be the lowercase show name
    """
    return (show[0]).lower()
