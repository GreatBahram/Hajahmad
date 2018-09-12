from collections import namedtuple

from bs4 import BeautifulSoup

def overall_review_numbers(html_codes, uri, city):
    """ """
    soup = BeautifulSoup(html_codes, 'html.parser')
    overall_dict = {
            'hotels': 'hotels',
            'forum': 'forum',
            'restaurants': 'restaurants',
            'flights': 'flights', 
            'thingstodo': 'attractions',
            'vacationalrentals': 'vacationRentals',
            }
    for key in overall_dict:
        try:
            overall_dict[key] = soup.select('.{} .contentCount'.format(overall_dict[key]))[0].getText().split()[0]
        except IndexError:
            overall_dict[key] = 0

    overall_dict['URL'] = uri
    overall_dict['city'] = city

    return overall_dict