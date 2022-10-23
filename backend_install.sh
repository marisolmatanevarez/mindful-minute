#!/bin/bash

python3 -m venv env
source env/bin/activate
pip install -r requirements.txt

cd backend && sqlite3 database.db ".read create.sql"