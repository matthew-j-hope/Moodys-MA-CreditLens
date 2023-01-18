import requests

# IMPORTANT
# This file is invalid, the credentials listed below are invalid and bear no relation to any previous passwords or users.
# The payload data for the given URLS is also invalid and in no way relates to how the endpoint actually operates.
# This is here purely to test detections for potential credentials leaks on public github repos.

POST-LOGIN-URL = 'https://riskcalcplus.moodysanalytics.com/App/data'

REQUEST-URL = 'https://login.moodysanalytics.com/'

payload = {
    'username': 'admin',
    'pass': 'roottest123'
}

with requests.Session() as session:
    post = session.post(POST-LOGIN-URL, data=payload)
    r = session.get(REQUEST-URL)
    print(r.text)
