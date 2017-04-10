#!/usr/local/bin/python

import os
import sys
from time import sleep
import subprocess
import psycopg2

def main():

	filename = "init.output"
	f = open(filename, "w")

	""" Read environment variables """
	postgres_user = os.environ['DB_ENV_POSTGRES_USER']
	postgres_db = os.environ['DB_ENV_POSTGRES_DB']
	postgres_pass = os.environ['DB_ENV_POSTGRES_PASSWORD']
	postgres_host = "db_1" 


	""" Wait for other services to start """
	f.write("[web] Sleeping for 30 secs...\n")
#	os.system('sleep 30')
	sleep(20)

	print("[web] checking if db exists...")
	f.write("[web] checking if db exists...\n")
	"""Check if the database zenodo is empty"""
	db_num_tables = check_db(postgres_db, postgres_user, postgres_host, postgres_pass)

	"""If database zenodo is empty then start tables init"""
	if db_num_tables == 0:
#		print("[web] db does not exist. Creating tables...")
		f.write("[web] db does not exist. Creating tables...\n")
		run_init()
		f.write("[web] db created!\n")
	else:
		"""Else (f database is not empty), finish. Do not perform initialization"""
#		print("[web] db exists. Skipping further actions (creating tables).")
		f.write("[web] db exists. Skipping further actions (creating tables).\n")


	""" Start server - uwsgi"""
#	print("[web] Starting uwsgi...")
	f.write("[web] Starting uwsgi...\n")
#	command = 'uwsgi /code/zenodo/docker/uwsgi/uwsgi.ini'
	command = "uwsgi"
	path = "/code/zenodo/docker/uwsgi/uwsgi.ini"
	subprocess.call([command, path])
#	os.system(command)	
	f.write("[web] uwsgi finished!\n")

	return

def check_db(db, user, host, password):
	"""Check if the database zenodo is empty
	   The function returns the number of tables in the database 'zenodo'"""

	connect_info = "dbname=" + db + " user=" + user + " host=" + host + " password=" + password
	conn = psycopg2.connect(connect_info) 
	cur = conn.cursor() 
	cur.execute("select count(*) from information_schema.tables where table_schema='public'")

	return cur.fetchone()[0]

def run_init():
	"""Start initialization of the tables in the database zenodo"""
	
	command = '/code/zenodo/scripts/init.sh'
#	os.system(command)
	subprocess.call([command])
	
	return

if __name__ == '__main__':
	sys.exit(main())
