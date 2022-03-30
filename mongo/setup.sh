#!/bin/bash

sleep 10 | echo "Waiting for the servers to start..."

mongo mongodb://mongo1:27017 replicaSet.js