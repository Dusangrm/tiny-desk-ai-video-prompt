"""Local-only AAC alignment helper. Requires ffmpeg and ffprobe on PATH."""
import argparse,json,subprocess
from pathlib import Path
p=argparse.ArgumentParser();p.add_argument('video',type=Path);p.add_argument('audio',type=Path);p.add_argument('output',type=Path);p.add_argument('--offset',type=float,default=0);a=p.parse_args()
if a.output.exists():p.error('Output exists; choose a new path.')
if not 0<=a.offset<=60:p.error('Offset must be between 0 and 60 seconds.')
def probe(path):
 return json.loads(subprocess.check_output(['ffprobe','-v','error','-show_streams','-show_format','-of','json',str(path.resolve())]))
v=probe(a.video);m=probe(a.audio)
if not any(x['codec_type']=='video' for x in v['streams']):p.error('Missing video stream.')
if not any(x['codec_type']=='audio' for x in m['streams']):p.error('Missing audio stream.')
duration=float(v['format']['duration'])
subprocess.run(['ffmpeg','-v','error','-n','-i',str(a.video.resolve()),'-i',str(a.audio.resolve()),'-map','0:v:0','-map','1:a:0','-c:v','copy','-af',f'adelay={round(a.offset*1000)}:all=1,apad=whole_dur={duration}','-c:a','aac','-b:a','160k','-t',str(duration),'-movflags','+faststart',str(a.output.resolve())],check=True)
