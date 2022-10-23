#!/bin/bash
export FLASK_APP=routes.py
export FLASK_DEBUG=1
export FLASK_ENV=development
export FLASK_RUN_HOST=0.0.0.0
export FLASK_RUN_PORT=3000

flask run