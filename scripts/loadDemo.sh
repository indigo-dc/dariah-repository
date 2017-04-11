#!/bin/bash

# Load demo records and index them

./loadlicenses.sh
./loadgrants.sh

zenodo fixtures loaddemorecords
zenodo migration recordsrun
zenodo migration reindex -t recid
zenodo index run -d
