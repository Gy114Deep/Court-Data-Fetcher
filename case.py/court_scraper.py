import requests
from bs4 import BeautifulSoup
def fetch_case(case_type,case_number,filling_year):
    url="https://services.ecourts.gov.in/ case_type={case_type}& case_number={case_number}& case_year={filing_year}"
    headers={'Agent':'Mozilla/5.0'}
    try:
        response=requests.get(url,headers,timeout=10)
        if response.status_code==200:
            return {f'Error:Error ❌occured!:{response.status_code}'}
        result = {"Parties":"ABC" ,
            "Filing Date":"12th March 2025" ,
            "Next Hearing":"18th August 2025"}
        return result
    except Exception as e:
        return f"something went wrong {str(e)}"
        