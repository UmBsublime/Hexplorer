# generated by datamodel-codegen:
#   filename:  http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.yml
#   timestamp: 2022-01-07T16:18:58+00:00

from __future__ import annotations

from typing import Optional

from pydantic import BaseModel, Field


class AccountDto(BaseModel):
    puuid: str
    gameName: Optional[str] = Field(
        None,
        description="This field may be excluded from the response if the account doesn't have a gameName.",
    )
    tagLine: Optional[str] = Field(
        None,
        description="This field may be excluded from the response if the account doesn't have a tagLine.",
    )


class ActiveShardDto(BaseModel):
    puuid: str
    game: str
    activeShard: str