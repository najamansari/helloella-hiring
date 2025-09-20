from typing import List

import requests

from app.schemas import CreatePayload, CreateResponse, GetResponse


class Client:
    def __init__(self, base_url: str):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()

    def create_payload(self, list_1: List[str], list_2: List[str]) -> CreateResponse:
        url = f"{self.base_url}/payload"
        payload = CreatePayload(list_1=list_1, list_2=list_2)
        try:
            response = self.session.post(url, json=payload.model_dump())
            if response.status_code != 200:
                response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to create payload: {e}")
        return CreateResponse.model_validate(response.json())

    def get_payload(self, payload_id: str) -> GetResponse:
        """Retrieve a payload by ID."""
        url = f"{self.base_url}/payload/{payload_id}"
        try:
            response = self.session.get(url)
            if response.status_code != 200:
                response.raise_for_status()
        except requests.RequestException as e:
            raise RuntimeError(f"Failed to get payload: {e}")
        return GetResponse.model_validate(response.json())
