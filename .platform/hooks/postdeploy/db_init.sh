#! /bin/bash
python -c "from application.database import AWSPostgreSQL; AWSPostgreSQL()"
flask db upgrade