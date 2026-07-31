from urllib.request import urlopen

class Downloader:
    def download(self, url: str) -> bytes:
        with urlopen(url) as response: # urlopen opens a tcp connection, send and http request, waits for response
            return response.read()