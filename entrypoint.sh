#!/bin/bash
set -e
if [ "$MODE" == 'UNIT' ]; then
        echo "running unit tests"
        exec python "/app/unit_test.py"
else
        echo "Running production"
        exec python "/app/get_stolen_bikes.py"
fi