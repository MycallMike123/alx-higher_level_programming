#!/bin/bash
#takes in a URL as an argument and sends a GET
curl -sH "X-School-User-Id: 98" "$1"
