from pathlib import Path

class FileStorage:
    def save(self, directory: str, filename: str, data: bytes) -> None:
        path = Path(directory)

        path.mkdir(parents=True, exist_ok=True)

        file_path = path / filename

        with file_path.open("wb") as file: # wb write binary pois o downloader returns bytes
            file.write(data)