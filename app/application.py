from app.config.settings import Settings
from app.download.downloader import Downloader
from app.storage.filesystem import FileStorage
import logging
from app.utils.datetime import utc_timestamp

logger = logging.getLogger(__name__)

class Applicaton:

    def __init__(self) -> None:
        self.settings = Settings()
        self.downloader = Downloader()
        self.storage = FileStorage()

    def run(self) -> None:
        print(f"Starting - {self.settings.app_name}")
        print(f"Environment: {self.settings.environment.value}")
        logger.info("Starting application")

        # request API
        data = self.downloader.download(self.settings.source_url)
        filename = f"{utc_timestamp()}_{self.settings.output_file}"

        # parse JSON - Neste caso não é preciso pois o write 
        # data =  data.decode("utf-8")
        
        # save file
        # self.storage.save("users.json", data) # não é preciso data.decode("utf-8") pois os bytes vão ser escritos para json
        self.storage.save(
            self.settings.output_dir,
            filename, # self.settings.output_file,
            data,
        )
        logger.info("Download complete")