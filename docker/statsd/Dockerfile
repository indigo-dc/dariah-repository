FROM node:6
RUN npm install -g statsd git://github.com/markkimsal/statsd-elasticsearch-backend.git
COPY config.js /opt/statsd/config.js
COPY init.sh /init.sh
EXPOSE 8125/udp
#CMD statsd /opt/statsd/config.js
ENV ES_HOST es
ENV ES_PORT 9200
CMD bash /init.sh
