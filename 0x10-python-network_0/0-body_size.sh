#!/bin/bash
# Display number of bytes in location
curl -s "$1" | wc -c
