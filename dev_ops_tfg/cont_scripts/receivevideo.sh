#!/bin/bash

for i in {1..100}
	do
	ffmpeg -y -reconnect 1 -reconnect_at_eof 1 -reconnect_streamed 1 -reconnect_delay_max 1 -i "http://VideoSrv:8000/Video.mp4" -codec copy  ~/Video.mp4
	done
