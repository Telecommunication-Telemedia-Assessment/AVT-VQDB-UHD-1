#!/usr/bin/env python3
import argparse
import os
import sys
import urllib.request


base_url = 'https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/'

# TODO: maybe push to JSON?
SRC_VIDEOS = [
    base_url + "",
    base_url + "",
    base_url + ""
]

VIDEO_SEGMENTS = [
    base_url + "",
    base_url + "",
    base_url + ""
]


def _get_file(url, target_filename_and_path):
    """
    downloads a file stored as a given `url` to `target_filename_and_path`
    """
    try:
        urllib.request.urlretrieve(url, target_filename_and_path)
    except:
        return False
    return True


def download_files(files):
    """
    downloads a list of `files`

    TODO: maybe parallel?
    """
    for file in files:
        _get_file(file, file.replace("base_url", "./"))
    return True


def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='download video segments and source videos',
                                     epilog="stg7 2019",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--no_sources", action="store_true", help="download no sources")

    a = vars(parser.parse_args())
    download_files(VIDEO_SEGMENTS)

    if not a["no_sources"]:
        download_files(SRC_VIDEOS)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
