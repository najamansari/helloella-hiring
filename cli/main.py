import json

import requests
from pydantic_settings import CliApp

from cli.settings import Settings


def main() -> None:
    CliApp.run(Settings)

if __name__ == "__main__":
    main()
