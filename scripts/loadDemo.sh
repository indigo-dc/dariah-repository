#!/bin/bash

# Load demo records and index them

zenodo fixtures loaddemorecords
zenodo migration recordsrun
zenodo migration reindex -t recid
zenodo index run -d -c 4
