import csv
import json
import sys
from io import StringIO
from typing import List

from cli.client import Client


def load_input(input_: str, json_: bool) -> tuple[List[str], List[str]]:
    dest = open(input_, "r") if input_ != "-" else sys.stdin

    file_data = dest.read()

    if input_ != "-":
        dest.close()

    file_json = {}
    if json_:
        file_json = json.loads(file_data)
    else:
        parsed_file = [line for line in csv.reader(StringIO(file_data))]
        file_json["line_1"] = parsed_file[0]
        file_json["line_2"] = parsed_file[1]
    return file_json["line_1"], file_json["line_2"]


def write_output(output: str, transformed: List[str]):
    dest = sys.stdout if output == "-" else open(output, "w")
    csv.writer(dest).writerow(transformed)
    if output != "-":
        dest.close()


def run_test(host: str, repeat: int, input_: str, json_: bool, output: str) -> None:
    client = Client(host)

    list_1, list_2 = load_input(input_, json_)

    for _ in range(repeat):
        print(f"Running iteration: {_}")
        create_response = client.create_payload(list_1, list_2).model_dump()
        get_response = client.get_payload(create_response["id"]).model_dump()

    write_output(output, get_response["payload"])
