import requests


def main():
    pass


if __name__ == "__main__":
    web_url = 'https://maker.ifttt.com/trigger/price_greater_10000/with/key/nusE8EAkgRapaH9qk9TnJnsHf8-5ta9eaOie9h5DUZi'
    returned = requests.get(web_url)
    print(returned)
