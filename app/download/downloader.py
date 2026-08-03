import logging
import time
from urllib.request import urlopen

logger = logging.getLogger(__name__)

class Downloader:
    def download(self, url: str) -> bytes:
        attempts = 3

        for attempt in range(1, attempts + 1):
            try:
                logger.info("Dowloading %s (attempt %d)", url, attempt)

                with urlopen(url) as response: # urlopen opens a tcp connection, send and http request, waits for response
                    return response.read()

            except Exception:
                logger.exception("Download failed")

                if attempt == attempts:
                    raise

                time.sleep(2)