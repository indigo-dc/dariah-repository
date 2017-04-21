#!/usr/bin/env bash

sed -i "s/ES_PORT/$ES_PORT/" /opt/statsd/config.js 
sed -i "s/ES_HOST/$ES_HOST/" /opt/statsd/config.js

statsd /opt/statsd/config.js &

echo "Sleeping for 15sec..."
sleep 15

echo "Initializing..."
sh /usr/local/lib/node_modules/statsd-elasticsearch-backend/es-index-template.sh

while [ 1 ]; do
  sleep 600 
done
