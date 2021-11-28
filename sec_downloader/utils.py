"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
import requests
import json

USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
             'Chrome/93.0.4577.82 Safari/537.36'


def get_json_data(url: str) -> dict:
    """Downloads data in a json format.

    :param url: URL address of the source.
    :return: A dictionary of data from source.
    """
    session = requests.session()
    data = session.get(url, headers={'User-Agent': USER_AGENT})
    data = json.loads(data.content)
    return data


def transform_recent_filings(data: dict) -> dict:
    """Transforms the recent filings data from the SEC format to a more comprehensive data format.

    :param data: Data including the recent filings.
    :return: A dictionary of the recent filings data by the company.
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
