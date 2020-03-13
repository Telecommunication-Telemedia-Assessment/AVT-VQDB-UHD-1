#!/usr/bin/env python3
import glob
import os
import sys
import logging
import argparse


def get_thumbnail_name(video, thumbfolder):
    """ create a unified thumbnail name """
    thumb_name = os.path.splitext(os.path.basename(video))[0] + ".jpg"
    dirname = os.path.dirname(video)
    d = dirname.replace("/", "_").replace("_segments", "")
    return os.path.join(thumbfolder, d + "_" + thumb_name)


def extract_thumb(video, thumbnailname):
    """ run ffmpeg to extract one frame """
    ret = os.system(f"""ffmpeg -y -ss 00:00:02 -i "{video}" -vframes 1 {thumbnailname}""")
    if ret != 0:
        sys.exit(0)


def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='create thumbnails for src_videos and segments',
                                     epilog="stg7 2020",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--only_sources", action="store_true", help="only extract for src_videos")
    parser.add_argument("--thumb_folder", type=str, default="thumbs", help="output folder for thumbs")

    a = vars(parser.parse_args())

    videos = list(glob.glob("src_videos/*"))
    if not a["only_sources"]:
        videos += list(glob.glob("test*/segments/*"))

    logging.info(f"extract thumbnails for {len(videos)} videos")

    if len(videos) == 0:
        logging.error("please first download all src_videos and segments")
        sys.exit(0)

    os.makedirs("thumbs", exist_ok=True)
    for video in videos:
        thumb_name = get_thumbname(video, thumbfolder=a["thumb_folder"])
        extract_thumb(video, thumb_name)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
