# generated by datamodel-codegen:
#   filename:  http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.yml
#   timestamp: 2022-01-07T16:18:58+00:00

from __future__ import annotations

from pydantic import BaseModel, Field


class SummonerDTO(BaseModel):
    accountId: str = Field(..., description="Encrypted account ID. Max length 56 characters.")
    profileIconId: int = Field(..., description="ID of the summoner icon associated with the summoner.")
    revisionDate: int = Field(
        ...,
        description="Date summoner was last modified specified as epoch milliseconds. The following events will update this timestamp: profile icon change, playing the tutorial or advanced tutorial, finishing a game, summoner name change",
    )
    name: str = Field(..., description="Summoner name.")
    id: str = Field(..., description="Encrypted summoner ID. Max length 63 characters.")
    puuid: str = Field(..., description="Encrypted PUUID. Exact length of 78 characters.")
    summonerLevel: int = Field(..., description="Summoner level associated with the summoner.")
