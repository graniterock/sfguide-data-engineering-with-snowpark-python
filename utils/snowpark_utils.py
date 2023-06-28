from snowflake.snowpark import Session
import os
from typing import Optional

# Class to store a singleton connection option


class SnowflakeConnection(object):
    _connection = None

    @property
    def connection(self) -> Optional[Session]:
        return type(self)._connection

    @connection.setter
    def connection(self, val):
        type(self)._connection = val

# Function to return a configured Snowpark session


def get_snowpark_session() -> Session:
    # if running in snowflake
    # if SnowflakeConnection().connection:
    #     # Not sure what this does?
    #     session = SnowflakeConnection().connection
    # # if running locally with a config file
    # # TODO: Look for a creds.json style file. This should be the way all snowpark
    # # related tools work IMO
    # # if using snowsql config, like snowcli does
    # elif os.path.exists(os.path.expanduser("~/.snowsql/config")):
    #     snowpark_config = get_snowsql_config()
    #     session = Session.builder.configs(snowpark_config).create()
    # otherwise configure from environment variables
    # if "SNOWSQL_ACCOUNT" in os.environ:
    snowpark_config = {
        "account": "HMB58153",
        "user": "SUMMITUSER",
        "password": "WildSnarf4!",
        "role": "HOL_ROLE",
        "warehouse": "HOL_WH",
        "database": "HOL_DB"
    }
    session = Session.builder.configs(snowpark_config).create()

        # return session

    # if SnowflakeConnection().connection:
    #     return SnowflakeConnection().connection  # type: ignore
    # else:
    #     raise Exception("Unable to create a Snowpark session")

    return session


