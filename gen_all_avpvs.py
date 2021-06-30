#!/usr/bin/env python3
import os
import glob
import argparse
import sys
import itertools
from multiprocessing import Pool
import multiprocessing

import pandas as pd

from gen_avpvs import avpvs_gen


def main(_):
    parser = argparse.ArgumentParser(description='convert for all tests the avpvs',
                                     epilog="stg7 2021",
                                     formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument('--cpu_count', type=int, default=multiprocessing.cpu_count() // 2, help='thread/cpu count')

    a = vars(parser.parse_args())

    # get metadata files for all tests
    meta = list(glob.glob("test*/metadata.csv"))

    video_segment_src_pairs = []
    for m in meta:
        dm = pd.read_csv(m)
        for _, r in dm[["src", "video_name"]].iterrows():
            segment_file = os.path.join(
                os.path.dirname(m),
                "segments",
                r["video_name"]
            )

            # check if segment_file exists
            if not os.path.isfile(segment_file):
                continue

            # check if src video exists
            src = list(glob.glob("src_videos/" + r["src"] + ".mkv"))
            if len(src) == 0:
                continue

            # all is fine, collect the data
            db = os.path.dirname(m)
            j = {
                "src": src[0],
                "video_name": segment_file,
                "db": db,
                "avpvs_folder": db + "_avpvs"
            }
            video_segment_src_pairs.append(j)


    params = [(v['video_name'], v['src'], v["avpvs_folder"]) for v in video_segment_src_pairs]

    if a["cpu_count"] > 1:
        pool = Pool(processes=a["cpu_count"])
        result = pool.starmap(avpvs_gen, params)
    else:
        result = list(itertools.starmap(avpvs_gen, params))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

