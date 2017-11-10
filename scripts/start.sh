#!/bin/bash

# Start zenodo
zenodo run -h 0.0.0.0 -p 5000 &

sleep 45

# Start initialization
bash /code/zenodo/scripts/init.sh
bash /code/zenodo/scripts/index.sh

# Load demo records and reindex
bash /code/zenodo/scripts/loadDemo.sh

