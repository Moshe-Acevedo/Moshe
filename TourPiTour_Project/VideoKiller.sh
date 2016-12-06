#!/bin/bash

kill $(ps -al | grep omxplayer | awk $'{print $4}')
