#!/bin/bash
if [ $# -eq 0 ]; then
	date=2015-10-11
else
	date=$1
fi
curl http://0.0.0.0:5000/v1/apod/?date=$date
