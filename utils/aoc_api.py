import requests
from pathlib import Path
from http.cookiejar import MozillaCookieJar
from markdownify import markdownify as md
from bs4 import BeautifulSoup
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
        page_html = self._get(route).text
        soup_html = BeautifulSoup(page_html, features="html.parser")
        instructions_tag = soup_html.find("article")
        if instructions_tag is None:
            raise Exception("Couldn't find tag containing puzzle instructions.")
        return md("".join([str(elem) for elem in instructions_tag.contents]))

    def submit_puzzle_answer(self, day:int, year:int, answer) -> bool:
        "TODO: test and integrate"
        data = {"answer": answer}
        output = self._post(self._year_day_route(day, year), data)
        print(output.status_code)
        return True
    
    def _get(self, route:str):
        return requests.get(
            url=self.base_url + route,
            cookies=self.cookies
        )
    
    def _post(self, route:str, data):
        return requests.post(
            url=self.base_url + route,
            cookies=self.cookies,
            data=data
        )
    def _year_day_route(self, day:int, year:int) -> str:
        return f"{year}/day/{day}"
    """def _day_path(self, day:int, year:int):
        Path(BASE)"""

if __name__ == "__main__":
    aoc = AocAPI()
    print(md(aoc.get_puzzle_instructions(1, 2025)))
    with open("test.md", 'w') as f:
        f.write(md(aoc.get_puzzle_instructions(1, 2025)))
    