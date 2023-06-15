import requests
from datetime import datetime
import time

electives = [439, 452, 468]

my_cookies = dict(remember_token='603|f3dbd865b9ac2329a4ce7d03acc37d780e01fd650c5698efda468ca715a42d9e8082326684810c5677135332dadc7fd05739e5bdb7cd793d42c72296fa2fccb6')
while True:
    if datetime.now() == datetime.strptime("15/06/23 06:30", "%d/%m/%y %H:%M"):
        
        for i in electives:
            s = requests.Session()
            res = s.get(f'https://go.gencyber.camp/register/{i}', cookies=my_cookies)
            time.sleep(1)

        break
    
print("Done.")
