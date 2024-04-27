import httpx
from httpx import Response


class HttpClient:
    def __init__(self):
        self.status_code: int | None = None
        self.client = self.__init_client()

    def get(self, url: str) -> Response:
        result = self.client.get(url)
        self.status_code = result.status_code
        return result

    def is_error(self) -> bool:
        return httpx.codes.is_error(self.status_code)

    def __init_client(self) -> httpx.Client:
        return httpx.Client(follow_redirects=True)
