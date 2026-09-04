import requests
from pathlib import Path
from http.cookiejar import MozillaCookieJar
from markdownify import markdownify as md
from bs4 import BeautifulSoup, Tag
from bs4.element import PageElement
class AocAPI():
    def __init__(self, base_url:str="https://adventofcode.com/"):
        self.base_url = base_url

        cookies = MozillaCookieJar()
        cookies.load("cookies.txt")
        self.cookies = cookies

    def get_puzzle_input(self, day:int, year:int) -> str:
        """Downloads puzzle input for a given day and year and stores it in its corresponding"""
        route = self._year_day_route(day, year) + "/input"
        output = self._get(route)
        return output.text

    def get_puzzle_instructions(self, day:int, year:int) -> str:
        route = self._year_day_route(day, year)
        response_html = self._get(route).text

        soup_html = self._beautiful_soup(response_html)
        article_tag = self._bs_find(soup_html, "article")
        if article_tag is None:
            raise Exception("Couldn't find tag containing puzzle instructions.")
        return md("".join([str(elem) for elem in article_tag.contents]))

    def submit_puzzle_answer(self, day:int, year:int, answer) -> bool:
        "TODO: test and integrate"
        data = {
            "answer": answer,
            "level": day
        }
        output = self._post(self._year_day_route(day, year) + "/answer", data)

        response_html = output.text
        soup_html = self._beautiful_soup(response_html)
        article_tag = self._bs_find(soup_html, "article")
        first_paragraph = self._bs_find(article_tag, "p")
        print(first_paragraph.text)
        answer_is_correct = "That's not the right answer." not in first_paragraph.text
        return answer_is_correct
    
    def _get(self, route:str):
        get_request = requests.get(
            url=self.base_url + route,
            cookies=self.cookies
        )
        #if get_request.status_code != 200:
        
        return get_request
    
    def _post(self, route:str, data):
        post_request = requests.post(
            url=self.base_url + route,
            cookies=self.cookies,
            data=data
        )

        #if post_request.status_code != 200:

        return post_request
    
    @staticmethod
    def _year_day_route(day:int, year:int) -> str:
        return f"{year}/day/{day}"
    
    @staticmethod
    def _beautiful_soup(html:str) -> BeautifulSoup:
        return BeautifulSoup(html, features="html.parser")
    """def _day_path(self, day:int, year:int):
        Path(BASE)"""

    @staticmethod
    def _bs_find(bs:Tag, tag_label:str) -> Tag:
        find_results = bs.find(tag_label)
        if not isinstance(find_results, Tag):
            raise Exception(f"Excepted to find a single '{tag_label}' tag, but didn't find any.")
        return find_results

if __name__ == "__main__":
    aoc = AocAPI()
    print(aoc.submit_puzzle_answer(1, 2025, 5))
    