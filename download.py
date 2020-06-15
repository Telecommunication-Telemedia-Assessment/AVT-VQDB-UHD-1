#!/usr/bin/env python3
import argparse
import os
import sys
import urllib.request
import json


def read_local_json(filename):
    with open(os.path.join(os.path.dirname(__file__), filename)) as fp:
        return json.load(fp)


base_url = 'https://avtshare01.rz.tu-ilmenau.de/avt-vqdb-uhd-1/'

SRC_VIDEOS = read_local_json("src_videos.json")

VIDEO_SEGMENTS = {
    "test_1": read_local_json("test_1.json"),
    "test_2": read_local_json("test_2.json"),
    "test_3": read_local_json("test_3.json"),
    "test_4": read_local_json("test_4.json"),
}


def _get_file(url, target_filename_and_path):
    """
    downloads a file from `url` to `target_filename_and_path`
    """
    try:
        urllib.request.urlretrieve(url, target_filename_and_path)
    except urllib.error.URLError as e:
        return False
    return True


def download_files(files):
    """
    downloads a list of `files`
    """
    for file in files:
        print(f"""download {file}""")
        os.makedirs(os.path.dirname(file), exist_ok=True)
        _get_file(base_url + file, file.replace(base_url, "./"))
    return True


def main(_):
    # argument parsing
    parser = argparse.ArgumentParser(description='download video segments and source videos',
                                     epilog="stg7 2019",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--no_sources", action="store_true", help="download no sources")

    a = vars(parser.parse_args())
    for test in VIDEO_SEGMENTS:
        download_files(VIDEO_SEGMENTS[test])

    if not a["no_sources"]:
        download_files(SRC_VIDEOS)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
