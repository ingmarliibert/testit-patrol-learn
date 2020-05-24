#!/bin/bash -e

echo "Building testit_patrol_sut container..."
cd $(rospack find testit_patrol)/docker/sut
docker build --no-cache -t ingmarliibert/testit_patrol_sut:latest .
echo "Building testit_patrol_testit container..."
cd $(rospack find testit_patrol)/docker/testit
docker build --no-cache -t ingmarliibert/testit_patrol_testit:latest .
