# generated by datamodel-codegen:
#   filename:  http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.yml
#   timestamp: 2022-01-07T16:18:58+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel


class Status(BaseModel):
    status_code: Optional[int] = None
    message: Optional[str] = None


class Error(BaseModel):
    status: Optional[Status] = None