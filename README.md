# sqlite-dump-to-csv
Simple Python 3 script to dump a SQLite database to a set of CSV files.

This script dumps SQLite database data into a set of CSV files, one for each table in the database. The first row of each
CSV file has the table column names.

Example Usage: python3 sqlite_dump.py --db sqlite.db --output ../data/
