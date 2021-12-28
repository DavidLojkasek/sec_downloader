# sec-downloader
<table border=1 cellpadding="10"><tr><td>
    <p style="text-align:center;"><strong>*THIS IS NOT AN OFFICIAL LIBRARY BY THE SEC*</strong></p>
</td></tr></table>

The ```sec-downloader``` library offers a light downloader of Company data and their filings from the SEC.

For more information, data or code, please refer to the github page
[here](https://github.com/DavidLojkasek/sec_downloader).

## Installation
You can install sec_downloader with pip:
```
pip install -i https://test.pypi.org/simple/ sec-downloader==1.0.0.0
```

### Requirements
* beautifulsoup4==4.10.0
* certifi==2021.10.8
* charset-normalizer==2.0.8
* idna==3.3
* requests==2.26.0
* soupsieve==2.3.1
* urllib3==1.26.7

## How to use
### Company module
```
import sec_downloader as sec

tpr = sec.Company('TPR')  # or tpr = sec.Company('1116132') or tpr = sec.Company(1116132)

# Get identifiers
tpr.title
tpr.ticker
tpr.cik
### 'TAPESTRY, INC.'
### 'TPR'
### '1116132'

# Get basic info
tpr.info
### {'cik': '1116132', 'entityType': 'operating', 'sic': '3100', 'sicDescription': 'Leather & Leather Products',
### 'insiderTransactionForOwnerExists': 0, 'insiderTransactionForIssuerExists': 1, 'name': 'TAPESTRY, INC.',
### 'tickers': ['TPR'], 'exchanges': ['NYSE'], 'ein': '522242751', 'description': '', 'website': '',
### 'investorWebsite': '', 'category': 'Large accelerated filer', 'fiscalYearEnd': '0627', 'stateOfIncorporation':
### 'MD', 'stateOfIncorporationDescription': 'MD', 'addresses': {'mailing': {'street1': '10 HUDSON YARDS',
### 'street2': None, 'city': 'NEW YORK', 'stateOrCountry': 'NY', 'zipCode': '10001', 'stateOrCountryDescription': 'NY'},
### 'business': {'street1': '10 HUDSON YARDS', 'street2': None, 'city': 'NEW YORK', 'stateOrCountry': 'NY',
### 'zipCode': '10001', 'stateOrCountryDescription': 'NY'}}, 'phone': '2129468400', 'flags': '', 'formerNames':
### [{'name': 'COACH INC', 'from': '2000-10-04T00:00:00.000Z', 'to': '2017-10-11T00:00:00.000Z'}]}

# Get recent filings
tpr.recent_filings[0]
### {'accession_number': '0001225208-21-014047', 'filing_date': '2021-11-22', 'report_date': '2021-11-19',
### 'acceptance_datetime': '2021-11-22T17:58:20.000Z', 'act': '', 'form': '4', 'file_number': '', 'items': '',
### 'size': 9216, 'is_xbrl': 0, 'is_inline_xbrl': 0, 'primary_document': 'xslF345X03/doc4.xml',
### 'primary_doc_ description': ''}
```

### Filing module
```
import sec_downloader as sec

tpr_filing = sec.Filing('0001225208-21-014047')

# Get identifiers
tpr_filing.accession_number
tpr_filing.cik
tpr_filing.url

### '0001225208-21-014047'
### '0001225208'
### 'https://www.sec.gov/Archives/edgar/data/0001225208/000122520821014047/0001225208-21-014047-index.htm'

# Get files
tpr_filing.files

### {0: {'Seq': '1', 'Description': '', 'Document':
### 'https://www.sec.gov//Archives/edgar/data/1116132/000122520821014047/xslF345X03/doc4.xml', 'Type': '4', 'Size':
### '\xa0'}, 1: {'Seq': '1', 'Description': '', 'Document':
### 'https://www.sec.gov//Archives/edgar/data/1116132/000122520821014047/doc4.xml', 'Type': '4', 'Size': '7885'}, 2:
### {'Seq': '\xa0', 'Description': 'Complete submission text file', 'Document':
### 'https://www.sec.gov//Archives/edgar/data/1116132/000122520821014047/0001225208-21-014047.txt', 'Type': '\xa0',
### 'Size': '9216'}}
```

## License
<strong>MIT License</strong>

Copyright (c) 2021 David Lojkasek

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR  IMPLIED, INCLUDING BUT NOT LIMITED TO THE
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

## Author
Let me know if you have any questions or feedback!!!

**David Lojkasek, 2021**<br>
Email: [lojkasek.david@gmail.com](mailto:lojkasek.david@gmail.com)<br>
Twitter: [@DavidLojkasek](https://twitter.com/DavidLojkasek)
