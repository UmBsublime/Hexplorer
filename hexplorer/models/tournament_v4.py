# generated by datamodel-codegen:
#   filename:  http://www.mingweisamuel.com/riotapi-schema/openapi-3.0.0.yml
#   timestamp: 2022-01-07T16:18:58+00:00

from __future__ import annotations

from enum import Enum
from typing import List, Optional

from pydantic import BaseModel, Field


class PickType(Enum):
    BLIND_PICK = "BLIND_PICK"
    DRAFT_MODE = "DRAFT_MODE"
    ALL_RANDOM = "ALL_RANDOM"
    TOURNAMENT_DRAFT = "TOURNAMENT_DRAFT"


class MapType(Enum):
    SUMMONERS_RIFT = "SUMMONERS_RIFT"
    TWISTED_TREELINE = "TWISTED_TREELINE"
    HOWLING_ABYSS = "HOWLING_ABYSS"


class SpectatorType(Enum):
    NONE = "NONE"
    LOBBYONLY = "LOBBYONLY"
    ALL = "ALL"


class TournamentCodeParameters(BaseModel):
    allowedSummonerIds: Optional[List[str]] = Field(
        None,
        description="Optional list of encrypted summonerIds in order to validate the players eligible to join the lobby. NOTE: We currently do not enforce participants at the team level, but rather the aggregate of teamOne and teamTwo. We may add the ability to enforce at the team level in the future.",
    )
    metadata: Optional[str] = Field(
        None,
        description="Optional string that may contain any data in any format, if specified at all. Used to denote any custom information about the game.",
    )
    teamSize: int = Field(..., ge=1, le=5, description="The team size of the game. Valid values are 1-5.")
    pickType: PickType = Field(
        ...,
        description="The pick type of the game.\n             (Legal values:  BLIND_PICK,  DRAFT_MODE,  ALL_RANDOM,  TOURNAMENT_DRAFT)",
    )
    mapType: MapType = Field(
        ...,
        description="The map type of the game.\n             (Legal values:  SUMMONERS_RIFT,  TWISTED_TREELINE,  HOWLING_ABYSS)",
    )
    spectatorType: SpectatorType = Field(
        ...,
        description="The spectator type of the game.\n             (Legal values:  NONE,  LOBBYONLY,  ALL)",
    )


class Region(Enum):
    BR = "BR"
    EUNE = "EUNE"
    EUW = "EUW"
    JP = "JP"
    LAN = "LAN"
    LAS = "LAS"
    NA = "NA"
    OCE = "OCE"
    PBE = "PBE"
    RU = "RU"
    TR = "TR"


class TournamentCodeDTO(BaseModel):
    code: str = Field(..., description="The tournament code.")
    spectators: str = Field(..., description="The spectator mode for the tournament code game.")
    lobbyName: str = Field(..., description="The lobby name for the tournament code game.")
    metaData: str = Field(..., description="The metadata for tournament code.")
    password: str = Field(..., description="The password for the tournament code game.")
    teamSize: int = Field(..., description="The team size for the tournament code game.")
    providerId: int = Field(..., description="The provider's ID.")
    pickType: str = Field(..., description="The pick mode for tournament code game.")
    tournamentId: int = Field(..., description="The tournament's ID.")
    id: int = Field(..., description="The tournament code's ID.")
    region: Region = Field(
        ...,
        description="The tournament code's region.\n             (Legal values:  BR,  EUNE,  EUW,  JP,  LAN,  LAS,  NA,  OCE,  PBE,  RU,  TR)",
    )
    map: str = Field(..., description="The game map for the tournament code game")
    participants: List[str] = Field(..., description="The summonerIds of the participants (Encrypted)")


class PickTypeModel(Enum):
    BLIND_PICK = "BLIND_PICK"
    DRAFT_MODE = "DRAFT_MODE"
    ALL_RANDOM = "ALL_RANDOM"
    TOURNAMENT_DRAFT = "TOURNAMENT_DRAFT"


class MapTypeModel(Enum):
    SUMMONERS_RIFT = "SUMMONERS_RIFT"
    TWISTED_TREELINE = "TWISTED_TREELINE"
    HOWLING_ABYSS = "HOWLING_ABYSS"


class SpectatorTypeModel(Enum):
    NONE = "NONE"
    LOBBYONLY = "LOBBYONLY"
    ALL = "ALL"


class TournamentCodeUpdateParameters(BaseModel):
    allowedSummonerIds: Optional[List[str]] = Field(
        None,
        description="Optional list of encrypted summonerIds in order to validate the players eligible to join the lobby. NOTE: We currently do not enforce participants at the team level, but rather the aggregate of teamOne and teamTwo. We may add the ability to enforce at the team level in the future.",
    )
    pickType: PickTypeModel = Field(
        ...,
        description="The pick type\n             (Legal values:  BLIND_PICK,  DRAFT_MODE,  ALL_RANDOM,  TOURNAMENT_DRAFT)",
    )
    mapType: MapTypeModel = Field(
        ...,
        description="The map type\n             (Legal values:  SUMMONERS_RIFT,  TWISTED_TREELINE,  HOWLING_ABYSS)",
    )
    spectatorType: SpectatorTypeModel = Field(
        ...,
        description="The spectator type\n             (Legal values:  NONE,  LOBBYONLY,  ALL)",
    )


class LobbyEventDTO(BaseModel):
    timestamp: str = Field(..., description="Timestamp from the event")
    eventType: str = Field(..., description="The type of event that was triggered")
    summonerId: str = Field(..., description="The summonerId that triggered the event (Encrypted)")


class RegionModel(Enum):
    BR = "BR"
    EUNE = "EUNE"
    EUW = "EUW"
    JP = "JP"
    LAN = "LAN"
    LAS = "LAS"
    NA = "NA"
    OCE = "OCE"
    PBE = "PBE"
    RU = "RU"
    TR = "TR"


class ProviderRegistrationParameters(BaseModel):
    region: RegionModel = Field(
        ...,
        description="The region in which the provider will be running tournaments.\n             (Legal values:  BR,  EUNE,  EUW,  JP,  LAN,  LAS,  NA,  OCE,  PBE,  RU,  TR)",
    )
    url: str = Field(
        ...,
        description="The provider's callback URL to which tournament game results in this region should be posted. The URL must be well-formed, use the http or https protocol, and use the default port for the protocol (http URLs must use port 80, https URLs must use port 443).",
    )


class TournamentRegistrationParameters(BaseModel):
    providerId: int = Field(
        ...,
        description="The provider ID to specify the regional registered provider data to associate this tournament.",
    )
    name: Optional[str] = Field(None, description="The optional name of the tournament.")


class LobbyEventDTOWrapper(BaseModel):
    eventList: List[LobbyEventDTO]