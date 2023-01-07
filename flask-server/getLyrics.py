import re
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import requests
"""---------------------------------------------"""
# Google Search for required urls


def search(term, num_results=10, lang="en"):
    user_agent = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/61.0.3163.100 Safari/537.36"
    }

    def fetch_results(search_term, number_results, language_code):
        escaped_search_term = search_term.replace(" ", "+")
        google_url = "https://www.google.com/search?q={}&num={}&hl={}".format(
            escaped_search_term, number_results + 1, language_code
        )
        response = Request(url=google_url, headers=user_agent)
        response_open = urlopen(response)

        return response_open.read()

    def parse_results(raw_html):
        soup = BeautifulSoup(raw_html, "html.parser")
        result_block = soup.find_all("div", attrs={"class": "g"})
        for result in result_block:
            link = result.find("a", href=True)
            title = result.find("h3")
            if link and title:
                yield link["href"]

    html = fetch_results(term, num_results, lang)
    return list(parse_results(html))


class NoResultFound(Exception):
    """Raised if no result is found or there is a HTTP error"""

    pass


class TooManyRequests(Exception):
    """Raised when number of requests exceed than the expected"""

    pass


"""----------------------------------------------------------"""
# Getting lyrics from specified website


def _searchLyrics_(query):
    for url in search(f"site:genius.com {query}", num_results=5):
        if "genius" in str(url):
            return url


class GetLyrics:
    def __init__(self, query):
        url = _searchLyrics_(query)
        if not url:
            raise NoResultFound("No lyrics for this song found.")
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.3"
        }
        r = requests.get(url=url)
        # req = Request(url=url, headers=headers)
        # lyrics_page = urlopen(req).read()
        soup = BeautifulSoup(r.text, "html.parser")
        # print(soup)
        # self.url = _searchLyrics_(query)
        self._soup = soup

    def _lyricsType_(self, div):
        lyrics_container = self._soup.find("div", {"class": div})
        print(lyrics_container)
        data = ""
        for child in lyrics_container.children:
            data = data + str(re.sub("\n", "", str(child)))
        return data

    def romaji(self) -> str:
        romaji_lyrics = self._lyricsType_("Lyrics__Container-sc-1ynbvzw-6")
        return romaji_lyrics
