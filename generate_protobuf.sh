#!/usr/bin/env bash

DIR=$(dirname "$0")
cd "$DIR"

python3 -m grpc_tools.protoc -I . --python_out=. --grpc_python_out=. soniox/speech_service.proto
