import requests

"""Список http методов"""
class Http_mothods:
    headers = {'Content-Type' : 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result = requests.get(url, headers=Http_mothods.headers, cookies=Http_mothods.cookie)
        return result

    @staticmethod
    def post(url, body):
        result = requests.post(url, json=body, headers=Http_mothods.headers, cookies=Http_mothods.cookie)
        return result

    @staticmethod
    def put(url, body):
        result = requests.put(url, json=body, headers=Http_mothods.headers, cookies=Http_mothods.cookie)
        return result

    @staticmethod
    def delete(url, body):
        result = requests.delete(url, json=body, headers=Http_mothods.headers, cookies=Http_mothods.cookie)
        return result
    