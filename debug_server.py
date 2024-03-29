"""
    Required for run server with uvicorn
    It is used for debugging in IDE or if you want to run it with simple python command, not unvicorn
"""

import uvicorn
from config import config
# it has to be for run server
# noinspection PyUnresolvedReferences
# pylint: disable=unused-import
from main import app


if __name__ == "__main__":
    uvicorn.run("debug_server:app", host="0.0.0.0", port=config.port, reload=True)
