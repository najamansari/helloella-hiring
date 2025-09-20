import json
import sys

from pydantic import Field
from pydantic_settings import BaseSettings, CliImplicitFlag, SettingsConfigDict

from cli.logic import run_test


class Settings(BaseSettings):
    host: str = Field(
        default="http://localhost:8000",
        description="points to the server",
    )
    repeat: int = Field(
        default=1,
        gt=0,
        description="indicates number of iterations",
    )
    input_: str = Field(
        default="-",
        alias="input",
        description="indicates the input file (\"-\" for stdin)",
    )
    json_: CliImplicitFlag[bool] = Field(
        default=False,
        alias="json",
        description="indicates an input argument in json from (properly escaped)",
    )
    output: str = Field(
        default="-",
        description="indicates the output file (\"-\" for stdout)",
    )

    model_config = SettingsConfigDict(
        env_prefix="CACHE_CLI_",
        case_sensitive=True,
        cli_parse_args=True,
        cli_prog_name="cache-cli",
        cli_shortcuts={
            "host": "H",
            "repeat": "r",
            "input": "i",
            "json": "j",
            "output": "o",
        }
    )

    def cli_cmd(self) -> None:
        print("Starting cache test...")
        print(f"Host: {self.host}")
        print(f"Iterations: {self.repeat}")
        print(f"Input source: {self.input_}")
        print(f"JSON input: {self.json_}")
        print(f"Output destination: {self.output}")
        try:
            run_test(self.host, self.repeat, self.input_, self.json_, self.output)
        except RuntimeError:
            print(f"Error! Unable to reach host: {self.host}")
        except json.JSONDecodeError:
            print(f"Error parsing given JSON")
        print("Cache test completed!")
