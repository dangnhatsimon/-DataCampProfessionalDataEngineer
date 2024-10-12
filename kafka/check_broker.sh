#!/bin/bash
echo "Broker count: $(bin/kafka-broker-api-versions.sh --bootstrap-server localhost:9092 | grep 9092 | wc -l)"$