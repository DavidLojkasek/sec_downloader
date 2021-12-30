"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
import requests
import json
from bs4 import BeautifulSoup

from . import constants as _constants

USER_AGENT = _constants.USER_AGENT


def get_page_contents(url: str) -> bytes:
    """ Returns the contents of the html page.

    :param url: The requested url.
    :type url: str.
    :return: Page contents.
    :rtype: bytes.
    """
    session = requests.session()
    page_contents = session.get(url, headers={'User-Agent': USER_AGENT}).content

    return page_contents


def get_json_data(url: str) -> dict:
    """Downloads data in a json format.

    :param url: URL address of the source.
    :type url: str.
    :return: A dictionary of data from source.
    :rtype: dict.
    """
    session = requests.session()
    data = session.get(url, headers={'User-Agent': USER_AGENT})
    data = json.loads(data.content)

    return data


def transform_recent_filings(data: dict) -> dict:
    """Transforms the recent filings data from the SEC format to a more comprehensive data format.

    :param data: Data including the recent filings.
    :type data: dict.
    :return: A dictionary of the recent filings data by the company.
    :rtype: dict.
    """
    filings = {}
    for count, filing in enumerate(data.get('accessionNumber')):
        filings[count] = {
            'accession_number': data.get('accessionNumber')[count],
            'filing_date': data.get('filingDate')[count],
            'report_date': data.get('reportDate')[count],
            'acceptance_datetime': data.get('acceptanceDateTime')[count],
            'act': data.get('act')[count],
            'form': data.get('form')[count],
            'file_number': data.get('fileNumber')[count],
            'items': data.get('items')[count],
            'size': data.get('size')[count],
            'is_xbrl': data.get('isXBRL')[count],
            'is_inline_xbrl': data.get('isInlineXBRL')[count],
            'primary_document': data.get('primaryDocument')[count],
            'primary_doc_description': data.get('primaryDocDescription')[count],
        }

    return filings


def get_single_company_identifiers(data: dict, identifier: str) -> dict:
    """Retrieves the three identifiers (CIK, ticker, title) of a single company.

    :param data: The dictionary mapping CIKs with tickers and title from the SEC.
    :type data: dict.
    :param identifier: The identifier passed by the user when constructing the object.
    :type identifier: str.
    :return: A dictionary with the identifiers.
    :rtype: dict.
    """
    data = {identifier: {
        'cik': str(data[c].get('cik_str')),
        'ticker': data[c].get('ticker'),
        'title': data[c].get('title')
    } for c in data if str(data[c].get('cik_str')) == identifier or data[c].get('ticker') == identifier}

    return data


def get_form_type(url: str):
    """Retrieves the form type from the filing page.

    :param url: The url of the filing page.
    :type url: str.
    :return: A string including the form type and description.
    :rtype: str.
    """
    filing_page = get_page_contents(url)
    soup = BeautifulSoup(filing_page, 'html.parser')
    form_type = soup.find('div', {'id': 'formName'}).text.strip()[:-1]  # Get rid of whitespace and the ':'.

    return form_type
