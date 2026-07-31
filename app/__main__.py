from app.application import Applicaton
from app.log_config import configure_logging

def main() -> None:
    configure_logging()
    
    app = Applicaton()
    app.run()


if __name__ == "__main__":
    main()