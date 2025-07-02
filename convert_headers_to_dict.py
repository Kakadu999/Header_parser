raw = '''GET / HTTP/2
Host: XXXXXXXXXXXXXX.net
Cookie: session=RBK6LA1OBwJWHJSgDUGrxl8KZvkgUpy4; TrackingId=zlYgnQS6xT5BcFIE
Cache-Control: max-age=0
Sec-Ch-Ua: "Brave";v="137", "Chromium";v="137", "Not/A)Brand";v="24"
Sec-Ch-Ua-Mobile: ?0
Sec-Ch-Ua-Platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8
Sec-Gpc: 1
Accept-Language: fr-FR,fr;q=0.8
Sec-Fetch-Site: cross-site
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Sec-Fetch-Dest: document
Referer: https://portswigger.net/
Accept-Encoding: gzip, deflate, br
Priority: u=0, i
'''

# Return Method, route, http ver and headers, convert Cookies to list
def convert_3(_raw : str) -> list:
	c = []
	b = {}
	for i in _raw.splitlines():
		try :
			splitted = i.split(':')
			b[splitted[0].strip()] = splitted[1].strip()
		except:
			c.append(i.split(" "))

	b['Cookie'] = [i.strip().split('=') for i in b['Cookie'].split(';')]
	c.append(b)

	return c


# Return Method, route, http ver and headers
def convert_2(_raw : str) -> list:
	c = []
	b = {}
	for i in _raw.splitlines():
		try :
			splitted = i.split(':')
			b[splitted[0].strip()] = splitted[1].strip()
		except:
			c.append(i.split(" "))

	c.append(b)

	return c

# Return only headers
def convert(_raw : str) -> dict:
	b = {}
	for i in _raw.strip().splitlines():
		try :
			splitted = i.split(':')
			b[splitted[0].strip()] = splitted[1].strip()
		except:
			pass

	return b

if __name__ == "__main__" : 
	b = convert(raw)
	for i, y in zip(b, b.values()):
		print(i,':', y)
