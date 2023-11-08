# !/usr/bin/python3
# BurpSuite Scraper v1.1
# By ConfusedCharacter

# BurpSuite Filename: "test/timeir.xml"
# Time: "Wed Nov 08 14:24:26 IRST 2023"
# Request url: "https://time.ir/"
# Request method: "GET"
# Request status: "301"
# Base64 Raw Request: R0VUIC8gSFRUUC8xLjENCkhvc3Q6IHRpbWUuaXINClNlYy1DaC1VYTogIkNocm9taXVtIjt2PSIxMTkiLCAiTm90P0FfQnJhbmQiO3Y9IjI0Ig0KU2VjLUNoLVVhLU1vYmlsZTogPzANClNlYy1DaC1VYS1QbGF0Zm9ybTogIkxpbnV4Ig0KVXBncmFkZS1JbnNlY3VyZS1SZXF1ZXN0czogMQ0KVXNlci1BZ2VudDogTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzExOS4wLjYwNDUuMTA1IFNhZmFyaS81MzcuMzYNCkFjY2VwdDogdGV4dC9odG1sLGFwcGxpY2F0aW9uL3hodG1sK3htbCxhcHBsaWNhdGlvbi94bWw7cT0wLjksaW1hZ2UvYXZpZixpbWFnZS93ZWJwLGltYWdlL2FwbmcsKi8qO3E9MC44LGFwcGxpY2F0aW9uL3NpZ25lZC1leGNoYW5nZTt2PWIzO3E9MC43DQpTZWMtRmV0Y2gtU2l0ZTogbm9uZQ0KU2VjLUZldGNoLU1vZGU6IG5hdmlnYXRlDQpTZWMtRmV0Y2gtVXNlcjogPzENClNlYy1GZXRjaC1EZXN0OiBkb2N1bWVudA0KQWNjZXB0LUVuY29kaW5nOiBnemlwLCBkZWZsYXRlLCBicg0KQWNjZXB0LUxhbmd1YWdlOiBlbi1VUyxlbjtxPTAuOQ0KUHJpb3JpdHk6IHU9MCwgaQ0KQ29ubmVjdGlvbjogY2xvc2UNCg0K
# Base64 Raw Response: SFRUUC8yIDMwMSBNb3ZlZCBQZXJtYW5lbnRseQ0KQ29udGVudC1UeXBlOiB0ZXh0L2h0bWw7IGNoYXJzZXQ9VVRGLTgNCkxvY2F0aW9uOiBodHRwczovL3d3dy50aW1lLmlyLw0KVmFyeTogQWNjZXB0LUVuY29kaW5nDQpBbHQtU3ZjOiBoMz0iOjQ0MyI7IG1hPTg2NDAwOyBwZXJzaXN0PTENCkFjY2Vzcy1Db250cm9sLUFsbG93LU9yaWdpbjogKg0KQWNjZXNzLUNvbnRyb2wtQWxsb3ctSGVhZGVyczogY29udGVudC10eXBlDQpYLUZyYW1lLU9wdGlvbnM6IFNBTUVPUklHSU4NClB1YmxpYy1LZXktUGluczogcGluLXNoYTI1Nj0iZVdDVUMxeTh6a3pzaHZKMmlyZ3EzSG1HSGt0OCtmSUFrRU1pVVpsdVdQaz0iOyBtYXgtYWdlPTMxNTM2MDAwDQpTdHJpY3QtVHJhbnNwb3J0LVNlY3VyaXR5OiBtYXgtYWdlPTMxNTM2MDAwOyBpbmNsdWRlU3ViRG9tYWluczsgcHJlbG9hZA0KRGF0ZTogV2VkLCAwOCBOb3YgMjAyMyAxMDo1NDoyNiBHTVQNCkNvbnRlbnQtTGVuZ3RoOiAxNDMNCg0KPGhlYWQ+PHRpdGxlPkRvY3VtZW50IE1vdmVkPC90aXRsZT48L2hlYWQ+Cjxib2R5PjxoMT5PYmplY3QgTW92ZWQ8L2gxPlRoaXMgZG9jdW1lbnQgbWF5IGJlIGZvdW5kIDxhIEhSRUY9Imh0dHBzOi8vd3d3LnRpbWUuaXIvIj5oZXJlPC9hPjwvYm9keT4=

import requests

def MyRequest():
	headers = {
		'Sec-Ch-Ua': '"Chromium";v="119", "Not?A_Brand";v="24"',
		'Sec-Ch-Ua-Mobile': '?0',
		'Sec-Ch-Ua-Platform': '"Linux"',
		'Upgrade-Insecure-Requests': '1',
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.105 Safari/537.36',
		'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
		'Sec-Fetch-Site': 'none',
		'Sec-Fetch-Mode': 'navigate',
		'Sec-Fetch-User': '?1',
		'Sec-Fetch-Dest': 'document',
		'Accept-Encoding': 'gzip, deflate, br',
		'Accept-Language': 'en-US,en;q=0.9',
		'Priority': 'u=0, i',
		'Connection': 'close',
		}
	response = requests.get(
		url='https://time.ir/',
		headers=headers,
		)

	return response

	