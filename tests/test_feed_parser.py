"""
Test Feed Parser
"""
import sys
import os
import unittest
import mock

# local imports
from feed_parser import FeedParser

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../..'))


class TestFeedParser(unittest.TestCase):
    """
    Add feed parser test methods to this class
    """

    # mock request call and just read the file
    def mocked_requests_get(*args, **kwargs):
        class MockResponse:
            def __init__(self, text, status_code):
                self.status_code = status_code
                self.text = text

        # current working dir
        cwd = os.getcwd()

        if args[0] == 'AskNoah.single.item.xml':
            return MockResponse(open(cwd + '/tests/resources/feeds/feedburner.AskNoah.single.item.xml', 'r').read(), 200)
        elif args[0] == 'AskNoah.4.19.2019.xml':
            return MockResponse(open(cwd + '/tests/resources/feeds/feedburner.AskNoah.4.19.2019.xml', 'r').read(), 200)

        return MockResponse(None, 404)

    # Test code
    def setUp(self):
        pass

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_feed_burner_parsing_single_item(self, mock_requests):
        """
        Using a static feedburner xml feed
        verifies expected outcome of shows/pagnation
        """

        # load static feeds
        feeds = _feed_data()
        page = 0
        episodes_per_page = 25
        name = 'testFeed'

        feedParser = FeedParser(name, feeds['feed_burner_single_item']['url'], episodes_per_page, page )
        feedParser.parseXML()

        self.assertEquals(feeds['feed_burner_single_item']
                        ['episodes'], feedParser.getTotalItems())

        for item in feedParser.getItems():
            self.assertEquals(feeds['feed_burner_single_item']
                            ['title'],  feedParser.parseTitle(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['size'],  feedParser.parseVideoSize(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['video'],  feedParser.parseVideo(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['pubDate'],  feedParser.parsePubDate(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['summary'],  feedParser.parsePlotOutline(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['description'],  feedParser.parsePlot(item))
            self.assertEquals(feeds['feed_burner_single_item']
                            ['director'],  feedParser.parseAuthor(item))

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_page_1_feed_burner_pagination_25_per_page(self, mock_requests):
        """
        Using a static feedburner xml verify
        pagination - page 1
        """
        feeds = _feed_data()
        page = 0
        episodes_per_page = 25
        name = 'testPagination25EpisodesPerPage'

        feedParser = FeedParser(name, feeds['feed_burner_pagination_25']['url'], episodes_per_page, page )
        feedParser.parseXML()

        countInfo = self._pagination_loop(feeds, feedParser)

        self.assertEquals(countInfo['beforePageCount'], 0)
        self.assertEquals(countInfo['itemCount'], episodes_per_page)
        self.assertEquals(countInfo['endOfPageCount'], 1)

    @mock.patch('requests.get', side_effect=mocked_requests_get)
    def test_page_2_feed_burner_pagination_13_per_page(self, mock_requests):
        """
        Using a static feedburner xml verify
        pagination - page 2
        """

        feeds = _feed_data()
        page = 1
        episodes_per_page = 13
        name = 'testPagination13EpisodesPerPage'

        feedParser = FeedParser(name, feeds['feed_burner_pagination_25']['url'], episodes_per_page, page )
        feedParser.parseXML()

        countInfo = self._pagination_loop(feeds, feedParser)

        self.assertEquals(countInfo['beforePageCount'], episodes_per_page)
        self.assertEquals(countInfo['itemCount'], episodes_per_page)
        self.assertEquals(countInfo['endOfPageCount'], 1)

    def _pagination_loop(self, feeds, feedParser):
        """
        This loop is designed to match the pagination loop
        in default.py as much as possible with exception
        to creating the show data and added separate variables
        to track expected items
        """

        countInfo = {
            'beforePageCount': 0,
            'itemCount': 0,
            'endOfPageCount': 0
        }

        # keep separate tracking of current item
        # to verify against feed parser
        expected_current_item = 0
        for item in feedParser.getItems():
            if feedParser.isItemBeforeCurrentPage():
                countInfo['beforePageCount'] += 1
                feedParser.nextItem()
                expected_current_item += 1
                # Skip this episode since it's before the page starts.
                continue
            if feedParser.isPageEnd():
                countInfo['endOfPageCount'] += 1
                break

            # assert correct order of shows,
            # + 1 to change to base 1 like parseTitle does
            if expected_current_item + 1 in (12, 25, 26, 49, 100, 135, 174):
                self.assertEquals(feedParser.parseTitle(item),
                                feeds['feed_burner_pagination_25'][expected_current_item + 1])

            expected_current_item += 1
            countInfo['itemCount'] += 1
            feedParser.nextItem()

        return countInfo


def _feed_data():
    """
    Add feed data here for validation
    """

    feeds = {}

    # Feeds
    feeds['feed_burner_pagination_25'] = {
        'url': 'AskNoah.4.19.2019.xml',
        'episodes': 123,
        12: '12. Episode 112: New Software Everywhere',
        25: '25. Episode 99: ArcoLinux with Erik Dubois',
        49: '49. Episode 75: Dell Precision 5510 Review',
        73: '73. Episode 51: Linux Users Trust Him',
        100: '100. Episode 24: Linux Home Theater',
    }

    feeds['feed_burner_single_item'] = {
        'url': 'BsdNow.single.item.xml',
        'episodes': 1,
        'title': 'Episode 123: Locking it Down with Yubikey',
        'pubDate': 'Tue, 16 Apr 2019 19:00:00 -0500',
        'director': 'Ask Noah Show',
        'description': 'Venkat Venkataraju principal software engineer from Yubico joins us this hour to share the exciting new features and functionality Yubico is bringing to the table!<'
    }

    return feeds
