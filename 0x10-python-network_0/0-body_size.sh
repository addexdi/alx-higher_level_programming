#!/bin/bash
# count the bytes of a response request
curl -s "$1" | wc -c
