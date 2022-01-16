# generated by datamodel-codegen:
#   filename:  http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.yml
#   timestamp: 2022-01-07T16:18:58+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class MiniSeriesDTO(BaseModel):
    losses: int
    progress: str
    target: int
    wins: int


class RatedTier(Enum):
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    BLUE = "BLUE"
    GREEN = "GREEN"
    GRAY = "GRAY"


class LeagueEntryDTO(BaseModel):
    leagueId: Optional[str] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    summonerId: str = Field(..., description="Player's encrypted summonerId.")
    summonerName: str
    queueType: str
    ratedTier: Optional[RatedTier] = Field(
        None,
        description="Only included for the RANKED_TFT_TURBO queueType.\n             (Legal values:  ORANGE,  PURPLE,  BLUE,  GREEN,  GRAY)",
    )
    ratedRating: Optional[int] = Field(None, description="Only included for the RANKED_TFT_TURBO queueType.")
    tier: Optional[str] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    rank: Optional[str] = Field(
        None,
        description="A player's division within a tier. Not included for the RANKED_TFT_TURBO queueType.",
    )
    leaguePoints: Optional[int] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    wins: int = Field(..., description="First placement.")
    losses: int = Field(..., description="Second through eighth placement.")
    hotStreak: Optional[bool] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    veteran: Optional[bool] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    freshBlood: Optional[bool] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    inactive: Optional[bool] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")
    miniSeries: Optional[MiniSeriesDTO] = Field(None, description="Not included for the RANKED_TFT_TURBO queueType.")


class RatedTierModel(Enum):
    ORANGE = "ORANGE"
    PURPLE = "PURPLE"
    BLUE = "BLUE"
    GREEN = "GREEN"
    GRAY = "GRAY"


class TopRatedLadderEntryDto(BaseModel):
    summonerId: str
    summonerName: str
    ratedTier: RatedTierModel = Field(..., description="(Legal values:  ORANGE,  PURPLE,  BLUE,  GREEN,  GRAY)")
    ratedRating: int
    wins: int = Field(..., description="First placement.")
    previousUpdateLadderPosition: int


class LeagueItemDTO(BaseModel):
    freshBlood: bool
    wins: int = Field(..., description="First placement.")
    summonerName: str
    miniSeries: Optional[MiniSeriesDTO] = None
    inactive: bool
    veteran: bool
    hotStreak: bool
    rank: str
    leaguePoints: int
    losses: int = Field(..., description="Second through eighth placement.")
    summonerId: str = Field(..., description="Player's encrypted summonerId.")


class LeagueListDTO(BaseModel):
    leagueId: str
    entries: List[LeagueItemDTO]
    tier: str
    name: str
    queue: str