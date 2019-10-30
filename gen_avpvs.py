#!/usr/bin/env python3

import os
import sys
import argparse
import glob
import pandas as pd
import subprocess as sp
import shlex
import pprint
import json

import yaml

def get_fps(src_video):
    ffprobe_cmd = "ffprobe -v quiet -print_format json -show_streams"
    args = shlex.split(ffprobe_cmd)
    args.append(src_video)
    ffprobeOutput = sp.check_output(args).decode('utf-8')
    ffprobeOutput = json.loads(ffprobeOutput)

    fps = ffprobeOutput["streams"][0]["avg_frame_rate"]
    nr = int(fps.split("/")[0])
    dr = int(fps.split("/")[1])
    framerate = round((nr/dr),2)
    return framerate

def avpvs_gen(input_file, src_video, avpvs_folder):
    avpvs_width = 3840
    avpvs_height = 2160
    output_file = os.path.join(avpvs_folder, os.path.splitext(os.path.basename(input_file))[0] + "_avpvs.mkv")
    print(output_file)
    target_pix_fmt = "yuv422p10le"

    # ffprobe_cmd = """ffprobe -v 0 -of csv=p=0 -select_streams v:0 -show_entries stream=r_frame_rate {src_video}""".format(**locals())
    # ffprobe_cmd = """ffprobe {src_video} 2>&1| grep ",* fps" | cut -d "," -f 5 | cut -d " " -f 2 """.format(**locals())

    src_framerate = get_fps(src_video)
    print(src_framerate)

    cmd = """ffmpeg -nostdin -i {input_file} -filter:v scale={avpvs_width}:{avpvs_height}:flags=bicubic,fps={src_framerate},setsar=1/1 -c:v ffvhuff -threads 4 -level 3 -coder 1 -context 1 -slicecrc 1 -pix_fmt {target_pix_fmt} -an {output_file}""".format(**locals())

    ret = os.system(cmd)
    if ret != 0:
        sys.exit(-1)
    return output_file

def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='convert video segment to avpvs',
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--videosegment", type=str, help="video segment")
    parser.add_argument("--src", type=str, help="source video")
    parser.add_argument("--avpvs_folder", type=str, default="./avpvs", help="folder for storing the avpvs file")

    args = vars(parser.parse_args())
    avpvs_gen(args["videosegment"], args["src"], args["avpvs_folder"])

    return 0

if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
