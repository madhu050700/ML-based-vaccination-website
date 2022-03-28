import json, requests
url = 'https://api.foursquare.com/v2/venues/explore'

params = dict(
client_id='24BAGOCQB1CBUV3RKR0DTCEBUPPGHH1MFCOT5O0SH5MSCEBH',
client_secret='U1SGTRHPS0L0GSQINQKKHIXCQENGSXFFA2MQFQCGHMXKXZZD',
v='20180323',
near='Chennai',
query='hospital',
limit=5
)
resp = requests.get(url=url, params=params)
data = json.loads(resp.text)