#!/bin/bash
# mix.sh video.mp4 track.mp3 out.mp4 : fit the track to the video length (no stretch, no loop), as _fit_track in make_media.py
v=$1; t=$2; o=$3
d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$v"); tl=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$t")
if python3 -c "import sys;sys.exit(0 if $tl<=$d+0.3 else 1)"; then
  fc="[1:a]apad,atrim=0:$d[a]"
else
  read body keep <<<$(python3 -c "e=min(3.0,$tl/3);print(f'{$tl-e:.3f} {$d-e+1.0:.3f}')")
  fc="[1:a]atrim=0:$keep,asetpts=N/SR/TB[m];[2:a]atrim=start=$body,asetpts=N/SR/TB[e];[m][e]acrossfade=d=1.0:c1=tri:c2=tri,atrim=0:$d[a]"
fi
ffmpeg -v error -y -i "$v" -i "$t" -i "$t" -filter_complex "$fc" -map 0:v -map "[a]" -c:v copy -c:a aac -b:a 192k -t $d -movflags +faststart "$o"
