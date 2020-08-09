import requests


class ShoePage:
    def __init__(self, shoeName, category="men"):
        self.shoeName = (shoeName.replace(" ", "-")).lower()
        if category != "kids":
            self.category = category + "s"
        self.thisSession = requests.Session()

    def main_page(self):
        website = "https://www.footlocker.com/"
        headers = {
            'if-none-match': 'W/"6fd9d-pAosbgjIELpgH0o0zhJZFsK9a2E"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': "1",
            "Set-Cookie": "_abck=C7FFD60E70AC191FEC630220D170F5DE~-1~YAAQpgNAF4Idms9zAQAAvgejzwRATwIAsdnu0rmxFQUHkA6ygfNIUUqGWDsD9IHTSRJkR7xZWGHa0QCa0TH7YTXiLVFPaZGKLzuzI7JQnL+jz1TGmOOC4y5uejvPuY4WMlg2seKcTjf+9kgABOnsyJadcdVL5oBiyhPgNxr91UcuSY8TwjfTs1Sf+nQ3HoT6Q3efaHOkHTlJPrB6S1KUe+JIufyNRz7lpC1Ap0uMWUmOmNjW3roTT3n0A7mWwOK+xZBxwiFUg5dibBQySkJ4AaRwYKywn/MpLagWzRCmj1P2tpxp8/+zEndjnAsVfA==~-1~-1~-1; Domain=.footlocker.com; Path=/; Expires=Sun, 08 Aug 2021 19:53:54 GMT; Max-Age=31536000; Secure",
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36 Edg/84.0.522.52'
        }
        cookies = {
            "DCT_Exp_HUNDRED": "DCT",
            "ak_bmsc": "6C3612D59C5CD58DBB7017B5B2AF8280174003A6A74300004D022F5FCBCEEC55~plai7Drv2ap7oNdoU6i6mHLiaRxphkTIrY+r5KHj8HaUf/yBgtl8nl9QbLshZ96kZY3VEOEw8QW/BAZZJXOD0nnZN8C6z1x+w8QL0uNJka5qlfpLtGPNX0Wsx/XiSmPeMN/2cN3fywBlCNuBRLp/9idjO1JAR5x9qA5xa0Jqp+33VZOKkTp42A7facbUBgarLjfRInPBu+ty+eyrJ0rdTP1Oe5o4uI+Hk5HQi/TKaytgw=",
            "bm_sz": "71DBF4A77CE71EEDD2FDE14CAC2541E9~YAAQpgNAF+kUms9zAQAAKwChzwitj6+fKrkdsw5AUQkh2Kn6lukE2gbgrq3v2oBhnHY89WFX4gIwWmdSngA+sQsTtlTPwuus48DOuPeDiONMz/g4/dNcUJniTqPlnTwfEIg84rF2Py2Y7WmPU7D+yN0PZAg7L7lLwVH5cg3mQvVSVVmBXAGr15GfGyxaQJfetkvbOQ==",
            "_abck": "06980730E23276573CE468E25E0BD449~-1~YAAQpgNAF+oUms9zAQAAKwChzwTzi5hBw8M7SrIq2A8b07tZn/lpfBnwyLYJ17yaVqRmJ3WJUa7lly3STorTm2lTtxDgTnum2bJ/oh+ZShY4bd4ydAwqscGVlMPb9FKqZk5Wj+YIWnZ6TRpDdE7LFRDLMuezguXhAYdv4Lamn9xUqrIaLOEEesiNlvovGQWNPAgwpq5pHyRCazf89PiONKZPecjMRi5tZ7SAzXm8+WUYsKCQKatvvzfYjkETB794Bm0GVvOYncYz0+nlL2vGE9lGG7T8Vy/y5EC67soBxBsLvBVwTbc3TZqb2TtgYg==~-1~-1~-1"
        }
        response = self.thisSession.get(website, headers=headers, cookies=cookies)
        responseCookies = {}
        for c in response.cookies:
            responseCookies[c.name] = c.value
        responseHeaders = response.headers
        print(responseHeaders)

    def main_shoe_page(self):
        mainUrl = f"https://www.footlocker.com/product/{self.shoeName}-{category}/A0907002.html"
        print(mainUrl)
        response = self.thisSession.get(mainUrl)
        print(response.headers)
        print(response.status_code)


shoeName = "Nike Zoom Freak 2"
category = "men"

myShoe = ShoePage(shoeName, category)
myShoe.main_page()
