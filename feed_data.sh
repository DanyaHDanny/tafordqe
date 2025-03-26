#!/bin/bash

# Database connection details
DB_HOST="localhost"
DB_PORT="5433"  # Updated port
DB_USER="admin"
DB_PASSWORD="admin123"
DB_NAME="my_database"

# Feed data into PostgreSQL
PGPASSWORD=$DB_PASSWORD psql -h $DB_HOST -p $DB_PORT -U $DB_USER -d $DB_NAME -f data.sql