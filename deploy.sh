#!/bin/bash

docker build -t steemdata-webapi .
docker tag steemdata-webapi furion/steemdata-webapi
docker push furion/steemdata-webapi
