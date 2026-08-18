import base64
import hashlib
import os

from fastapi import FastAPI, HTTPException, Request
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field

DEFAULT_MAX_TEXT_LENGTH = 10_000


def get_max_text_length() -> int:
    try:
        value = int(os.getenv("CHECKSUM_MAX_TEXT_LENGTH", DEFAULT_MAX_TEXT_LENGTH))
    except ValueError:
        return DEFAULT_MAX_TEXT_LENGTH
    return value if value > 0 else DEFAULT_MAX_TEXT_LENGTH

app = FastAPI(title="mytest API")


@app.exception_handler(RequestValidationError)
async def handle_validation_error(
    request: Request, error: RequestValidationError
) -> JSONResponse:
    del request
    details = [
        {key: value for key, value in detail.items() if key != "input"}
        for detail in error.errors()
    ]
    return JSONResponse(status_code=422, content={"detail": details})


class Text(BaseModel):
    text: str = Field(max_length=get_max_text_length())


@app.get("/")
async def read_root() -> dict[str, str]:
    return {"message": "Hello, World!"}


@app.post("/checksum")
async def create_checksum(payload: Text) -> dict[str, str]:
    try:
        digest = hashlib.sha256(payload.text.encode("utf-8")).digest()
    except UnicodeEncodeError as error:
        raise HTTPException(status_code=422, detail="Text must be valid Unicode") from error

    checksum = base64.b16encode(digest).decode("ascii").lower()
    return {"checksum": checksum}
