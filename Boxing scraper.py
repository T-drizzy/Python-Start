from bs4 import BeautifulSoup
import requests
import re
import time

# Get the search term from the user
search_term = input("Which fighter do you want to search for? ")
time.sleep(1)
print()
print("Loading...")
print()
# Formatting the input so it creates a correct url
search_term_formatted = search_term.lower().replace(" ", "-")
first_letter = search_term_formatted[0]

# Construct the URL to search for the product on Newegg
url = f"https://www.martialbot.com/boxing/{first_letter}/{search_term_formatted}.html"
page = requests.get(url).text
doc = BeautifulSoup(page,"html.parser")

# Find the div containing the fights
div = doc.find(class_ = "hscroller full-width")

fight_info_elements = div.find_all("td")

string_elements = [td.get_text(strip=True) for td in fight_info_elements]


# Length of the recurring pattern (6 elements per fight)
pattern_length = 6

# Number of fights we need to display --> (total elements divided by the pattern_length)
num_fights = len(string_elements) // pattern_length

for i in range(num_fights):
    # Calculate the start index for each fight
    start_index = i * pattern_length

    # Extract individual elements based on the pattern
    fight_number = string_elements[start_index]
    fight_date = string_elements[start_index + 1]
    fighter_age = string_elements[start_index + 2]
    opponent = string_elements[start_index + 3]
    fight_result = string_elements[start_index + 4]
    via_decision = string_elements[start_index + 5]

    # Print the information for each fight
    print("Fight Number:", fight_number)
    print("Fight Date:", fight_date)
    print("Fighter's Age:", fighter_age)
    print("Opponent:", opponent)
    print("Result:", fight_result)
    print("Via:", via_decision)
    print("-" * 20)  # Separator for better readability

# Checking the fighters win and loss amount 
w_count = 0
w_string = 'Win'
l_count = 0
l_string = 'Loss' 

for w_checker in string_elements:
    if w_checker == w_string:
        w_count += 1
    elif w_checker == w_string + '*':
        w_count += 1

for l_checker in string_elements:
    if l_checker == l_string:
        l_count += 1
    elif l_checker == l_string + '*':
        l_count += 1

# Printing the win and loss record for the fighter
print(f"{search_term}'s total wins: ", w_count)
print(f"{search_term}'s total losses: ", l_count)