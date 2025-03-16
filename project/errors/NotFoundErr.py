from http import HTTPStatus


class NotFoundError(Exception):
    """Exception raised for HTTP 404 Not Found errors."""

    def __init__(self, message):
        self.message = message
        self.code = HTTPStatus.NOT_FOUND
        super().__init__(self.message)

    def __str__(self):
        return f"NotFoundError: {self.message}"
