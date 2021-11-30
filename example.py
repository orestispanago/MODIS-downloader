import requests
from requests.auth import HTTPDigestAuth

url = "https://ladsweb.modaps.eosdis.nasa.gov/archive/allData/61/MYD05_L2/2021/091/MYD05_L2.A2021091.0015.061.2021091205501.hdf"
username = 'YourUsername'
password = 'YourPassword'

resp = requests.get(url, auth=HTTPDigestAuth(username, password))
if resp.status_code == 200:
    with open("a.hdf", 'wb') as f:
        f.write(resp.content)
else:
    print(resp.status_code)
