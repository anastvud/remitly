#!/bin/bash

export REPO_ROOT=$(git rev-parse --show-toplevel)

read -p "Do you want to run the main program or tests? (main/tests): " choice

if [ "$choice" = "main" ]; then
    python3 $REPO_ROOT/app.py
elif [ "$choice" = "tests" ]; then
    python3 $REPO_ROOT/test.py
else
    echo "Invalid choice. Exiting..."
    exit 1
fi
