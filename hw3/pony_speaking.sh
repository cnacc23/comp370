#!/bin/bash

# Check if the pony name is provided
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <pony_name> <file.csv>"
    exit 1
fi

PONY_NAME="$1"
FILE="$2"

# Count the number of times the pony speaks
COUNT=$(grep -iE "\"$PONY_NAME\"" "$FILE" | wc -l)

echo "$PONY_NAME speaks $COUNT times."

