#!/bin/bash

docker build -t steemdata-api .
docker tag steemdata-api furion/steemdata-api
docker push furion/steemdata-api
