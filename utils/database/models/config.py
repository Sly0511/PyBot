from pydantic import BaseModel


class BotConfig(BaseModel):
    token: str
    prefix: str
    server: int
    server_name: str
    owners: list[int]
    admins: list[int]
    blacklist: list[int]


class DatabaseConfig(BaseModel):
    name: str


class Config(BaseModel):
    bot: BotConfig
    database: DatabaseConfig
