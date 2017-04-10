#!/usr/bin/env bash

statsd /opt/statsd/config.js &

echo "Sleeping for 15sec..."
sleep 15

echo "Initializing..."
sh /usr/local/lib/node_modules/statsd-elasticsearch-backend/es-index-template.sh

while [ 1 ]; do
  sleep 600 
done
