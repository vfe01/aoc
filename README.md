# ``aoc`` - Solutions to Advent of Code
This repository contains my solutions to advent of code. At the time of writing, the solutions are implemented solely using python.

## CLI
### Initialize directories and files for a day of a given year
Example for day 3 2025: ``python -m utils.cli init -y 2025 -d 3``

### Execute solution
Example for day 3 2025, regular input: ``python -m utils.cli execute -y 2025 -d 6``
Example for day 3 2025, test input (test input needs to be manually inserted into the file ``test_input``): ``python -m utils.cli execute -y 2025 -d 6 -t``

## Website scraping automation
To automatically fetch problems, instructions, and submit anwers, cookies need to be provided. Go to the site, log in, and download cookies. Store the cookies in a file called "cookies.txt" placed in the root directory of the project.

## Note:
Puzzle input typically has double new-line at the end. The solution may or may not account for this (unlikely for 2025 01-04), although the standard should be using the input as-is with the double new-line.