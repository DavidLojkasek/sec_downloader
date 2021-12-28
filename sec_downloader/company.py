"""
sec-downloader: SEC-registered company and SEC forms data downloader.

Copyright (c) 2021 David Lojkasek (lojkasek.david@gmail.com)
"""
from . import utils as _utils
from . import constants as _constants

CIK_TICKER_MAP_URL = _constants.CIK_TICKER_MAP_URL
company_profile_url = 'https://data.sec.gov/submissions/CIK{}.json'


class Company:
    """A class representing a company registered with the SEC.

    :param identifier: Either a CIK or ticker identifier.
    :type identifier: str.
    """

    def __init__(self, identifier: str):
        """Constructor method for the Company object.

        Pass an identifier, either the CIK or ticker. :method:'Company._find_ticker_cik' finds the remaining data. There
        are three in total: CIK, ticker, title.

        :param identifier: Either a CIK or ticker identifier.
        :type identifier: str.
        """
        self.identifier = str(identifier).upper().lstrip('0')

        data = self._find_ticker_cik()
        self.ticker = data.get(self.identifier).get('ticker')
        self.cik = data.get(self.identifier).get('cik')
        self.title = data.get(self.identifier).get('title')

        self._profile_url = company_profile_url.format(self.cik.zfill(10))

        self._info = None
        self._recent_filings = None

    def __repr__(self):
        return 'sec-downloader.Company object(' + self.identifier + ')'

    def _find_ticker_cik(self) -> dict:
        """Based on the identifier passed to the constructor, the method searches the SEC API for remaining identifiers.

        The method is called automatically during the construction of the Company object.

        :return: A dict of identifiers.
        :rtype: dict.
        """
        data = _utils.get_json_data(CIK_TICKER_MAP_URL)
        data = _utils.get_single_company_identifiers(data, self.identifier)

        return data

    def _get_info(self) -> dict:
        """Retrieves data, except for filings data, from the 'profile page' of the company at the SEC.

        This method is called automatically when the user calls :instance_attribute:'Company.info' and
        :instance_attribute:'Company._info' attribute is None. Filings data are retrieved by
        :method:'Company._get_recent_filings' method.

        :return: A dict of the basic information.
        :rtype: dict.
        """
        data = _utils.get_json_data(self._profile_url)
        data = {key: val for key, val in data.items() if key != 'filings'}

        return data

    def _get_recent_filings(self) -> dict:
        """Retrieves the filing data from the 'profile page' of the company at the SEC.

        This method is automatically called when the user calls :instance_attribute:'Company.recent_filings' and
        :instance_attribute:'Company._recent_filings' is None. The remainder of the data in the profile page, the basic
        data, are retrieved by :method:'Company._get_info'.

        :return: A dict of filings and their data.
        :rtype: dict.
        """
        data = _utils.get_json_data(self._profile_url).get('filings').get('recent')
        data = _utils.transform_recent_filings(data)

        return data

    @property
    def info(self):
        """Returns a dict of basic info data.

        :return: A dict of basic data of the company.
        :rtype: dict.
        """
        if self._info is None:
            self._info = self._get_info()

        return self._info

    @property
    def recent_filings(self):
        """Returns a dict of filings and their data.

        :return: A dict of filings and their data.
        :rtype: dict.
        """
        if self._recent_filings is None:
            self._recent_filings = self._get_recent_filings()

        return self._recent_filings
