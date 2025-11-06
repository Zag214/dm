import os , configparser

from sys import argv
from pathlib import Path

config = configparser.ConfigParser()

try :
    config.read(Path(__file__).res.parent/'config.ini')
except :
    config['prefix'] = {
    'music': '-x --audio-format mp3 --embed-thumbnail --embed-metadata',
    'video': '--embed-thumbnail --embed-metadata'
    }
    with open(Path(__file__).resolve().parent/'config.ini', 'w') as configfile :
        config.write(configfile)

if 'm' in argv :
    url = argv[1]
    os.system(f"yt-dlp {config['prefix']['music']} {url}")
if 'v' in argv :
    url = argv[1]
    os.system(f"yt-dlp {config['prefix']['video']} {url}")
else :
    print ('\tm = use music download prefix\n' +
        '\tv = use video download prefix')