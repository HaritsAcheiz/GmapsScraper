import httpx
from selectolax.parser import HTMLParser
from dataclasses import dataclass

@dataclass
class GmapsScraper():

    def fetch(self, url):

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/111.0',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate, br',
            'Connection': 'keep-alive',
            # 'Cookie: 1P_JAR=2023-04-18-06; AEC=AUEFqZeTvKLRJ-6gtS7AgeYPSTxG368pp-XKjCglXDOJVnBeha-oCu1t5w; NID=511=MB_djzfDA19uvOFnFLcbwirEtByo6Q-xG-Ah93ltJEDrK4LiMc0o6DZKF8NJlPj8gjrU0g3EniMBraQ7LTZcT4mqjdH8gdJZOSk2LrMFNP-U58ny2-yhPY0DNd6JhBTd2ajbjeNESA1CVhcImSLQyMTUY3H5xYm5gb766XS3NhtJ9v7bIsgXx-oiWl0y8nXkwnJKq4sJAGNwYaEiTOl4QPvV70ToNSdhKh4PpFrU-kNXLHDyJHqYa0XSz5aWnkXxTpoBkk8uVnUz7-KZzMqo3WIxG65ec8sy5uFpZnkjfmnzef8I8QGhJt10edauOHEDxkcUznLzlESZ21oAb0V8YEhZd84heQxAk4F9NpVrLJRyxqJAu_SIfP7BOkPhC-u_umH6yhDviC5M5Ti9Y_uy5OxNXFKHpzGl2A; ANID=AHWqTUkmixJCqnYjAq1FE7nnyj_rsU0oppM7yllrG6HIeMhuIq-bxx24LgX_vbY6; SID=VAifUczjJvktzK0dwqffTbLU4Tr4rrO1v_tC3XOD11CUrzVpfdGUekzvlvfqrCeKqI2eAg.; __Secure-1PSID=VAifUczjJvktzK0dwqffTbLU4Tr4rrO1v_tC3XOD11CUrzVp2l1RGNPRR3klEomkIIez-Q.; __Secure-3PSID=VAifUczjJvktzK0dwqffTbLU4Tr4rrO1v_tC3XOD11CUrzVpanaEdcsE7lSicaFOxCfwUA.; HSID=AebFEd6iIc103zGZY; SSID=AY7boh4F4_NcKywnb; APISID=oA2WfnlQh3qDtJUQ/APSr-lf-yVEXXXf1G; SAPISID=1ye-txMxZJG1odQ7/Adbfs4akBGiCPYlmW; __Secure-1PAPISID=1ye-txMxZJG1odQ7/Adbfs4akBGiCPYlmW; __Secure-3PAPISID=1ye-txMxZJG1odQ7/Adbfs4akBGiCPYlmW; SIDCC=AP8dLtxdh6J2IyIf1rGT7_tkNWLalAnTbpwu90B9qc7w4ELUs-x-iNX7VfNJi1xgXB90ALTvjRQ; __Secure-1PSIDCC=AP8dLtz-T8ix8fpG8lv6YIFoCpXyb1ahHShFxRkZ1FjSwZ6ekXwf94XFxhX44JeAywiqSe9R2r-A; __Secure-3PSIDCC=AP8dLtwr66vCRMQBqGnUH-gKH_ypRAsmy8y3RJWpiy346Zeo37cdwhfEKgWH0PwQLYyz2BH7Esf5; SEARCH_SAMESITE=CgQIiZgB; OGPC=19034120-1:; OTZ=6955473_28_28__28_; S=billing-ui-v3=L8iUgw6GEy5xQCAQifLAMDFm8XMydX_Y:billing-ui-v3-efe=L8iUgw6GEy5xQCAQifLAMDFm8XMydX_Y
            'Upgrade-Insecure-Requests': 1,
            'Sec-Fetch-Dest': 'document',
            'Sec-Fetch-Mode': 'navigate',
            'Sec-Fetch-Site': 'none',
            'Sec-Fetch-User': '?1',
            'TE': 'trailers'
        }

        proxy = 'http://haritsproxy:M1tsut4n1_streaming-1@geo.iproyal.com:12321'

        with httpx.Client(proxies=proxy) as client:
            response = client.get(url)
        return response.text

    def parser(self, html):
        tree = HTMLParser(html)
        parent = tree.css_first('script:nth-of-type(7)').text().split('')
        # parent = tree.css('script')
        # print(len(parent))
        # for i, item in enumerate(parent):
        #     print(f'================script{i}====================')
        #     print(item.html)
        return parent


if __name__ == '__main__':
    url = 'https://www.google.com/maps/search/Restaurants/@37.7914119,-122.4132047,14z/data=!3m1!4b1'
    scraper = GmapsScraper()
    html = scraper.fetch(url)
    result = scraper.parser(html)
    for i, item in enumerate(result):
        print(f'============================{i}===============================')
        print(item)

