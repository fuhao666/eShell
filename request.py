import requests


class Request:
    def gets(self):
        res = requests.get(url=self['url'], params=self['myParams'])
        res.close()
        return res

    def posts(self):
        url = "http://httpbin.org/post"
        data = {"name": "plusroax", "age": 18}
        res = requests.post(url=url, data=data)
        return res
