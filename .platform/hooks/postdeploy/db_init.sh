#!/bin/bash
source $PYTHONPATH/activate
python -c "from application.database import AWSPostgreSQL; AWSPostgreSQL()"
flask db upgrade