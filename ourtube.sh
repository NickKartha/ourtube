#!/bin/bash
docker run --rm --network ourtube-net -p 4000:80 --mount type=bind,source="$(pwd)"/web,target=/web ourtube
