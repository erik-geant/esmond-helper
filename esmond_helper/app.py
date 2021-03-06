"""
testing entry point that can be invoked as:

    FLASK_APP=esmond_helper.app flask run

or just by running the module directly
"""

import logging
import sys
import esmond_helper

logging.basicConfig(
    stream=sys.stderr,
    level=logging.DEBUG)

app = esmond_helper.create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8234")
