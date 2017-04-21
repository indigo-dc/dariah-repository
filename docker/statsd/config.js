{
  graphiteHost: "",
  backends: [ 'statsd-elasticsearch-backend'],
  port: 8125,
  deleteCounters: true,
  flushInterval: 10 * 1000,
  elasticsearch: {
    port:          ES_PORT,
    host:          "ES_HOST",
    path:          "/",
    indexPrefix:   "statsd",
    //indexTimestamp: "year",  //for index statsd-2015
    //indexTimestamp: "month", //for index statsd-2015.01
    indexTimestamp: "day",     //for index statsd-2015.01.01
    countType:     "counter",
    timerType:     "timer",
    timerDataType: "timer_data",
    gaugeDataType: "gauge",
    formatter:     "default_format"
  }
}
