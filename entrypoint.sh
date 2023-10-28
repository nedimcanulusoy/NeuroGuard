#!/bin/sh

if [ "$APP_TYPE" = "api" ]; then
    python main.py api
elif [ "$APP_TYPE" = "interface" ]; then
    python main.py interface
else
    echo "Please specify APP_TYPE environment variable as 'api' or 'interface'"
fi
