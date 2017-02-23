#! /usr/bin/env python3
import codecs
import os
import sqlite3
import csv


def main(db_file, output_dir):
    """
    This script dumps data from a SQLite database into CSV tables
    """
    con = sqlite3.connect(db_file)
    cur = con.cursor()
    # get the names of each of the tables in the database
    cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tabs = cur.fetchall()
    for tab in tabs:
        tab = tab[0]
        cols = []
        try:
            # get the column names for the current table
            cols = cur.execute("PRAGMA table_info('%s')" % tab).fetchall()
        except:
            cols = []
        if len(cols) > 0:
            # we have columns for the table, so OK to dump it
            fname = tab + '.csv'
            print('Output: ' + fname)
            path_fname = os.path.join(output_dir, fname)
            f = codecs.open(path_fname, 'w', encoding='utf-8')
            writer = csv.writer(f, dialect=csv.excel, quoting=csv.QUOTE_ALL)
            field_name_row = []
            for col in cols:
                col_name = col[1]
                field_name_row.append(col_name)
            writer.writerow(field_name_row)  # write the field labels in first row
            # now get the data
            cur.execute("SELECT * FROM " + tab + ";")
            rows = cur.fetchall()
            for row in rows:
               writer.writerow(row)  # write data row
            f.closed
    print("Done! " + output_dir)

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description="""
This script dumps SQLite database data into a set of CSV files. The first row of each
file has the column names.

Example Usage: python3 sqlite_dump.py --db sqlite.db --output ../data/

""")
    parser.add_argument('--db', required=True, help='database file')
    parser.add_argument('--output', required=True, help='output directory')
    args = parser.parse_args()
    main(args.db, args.output)



