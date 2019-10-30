# AVT-VQDB-UHD-1
This is a repository with data related to the 4K databases that are published at IEEE-ISM 2019.

If you use any of the data please cite the following paper

```
@inproceedings{rao2019Db,
    author = {Rakesh Rao Ramachandra Rao and Steve G\"oring and Werner Robitza and Bernhard Feiten and Alexander Raake},
    title = {AVT-VQDB-UHD-1: A Large Scale Video Quality Database for UHD-1},
    booktitle={2019 IEEE ISM},
    year = {2019},
    pages={1-8},
    volume={},
    month={Dec}
}
```
## Download of Source videos and segments
TBD

## AVPVS Generation
To run, e.g., full reference models, it is required to perform a conversion to match the same resolution and framerate of the distorted video to the corresponding source video.
For this you can use the scripte `gen_avpvs.py`.
As a requirement you need Python >=3.6 installed.

For the usage, run `./gen_avpvs.py --help`:

```
usage: gen_avpvs.py [-h] [--avpvs_folder AVPVS_FOLDER] videosegment src

convert video segment to avpvs

positional arguments:
  videosegment          video segment
  src                   source video

optional arguments:
  -h, --help            show this help message and exit
  --avpvs_folder AVPVS_FOLDER
                        folder for storing the avpvs file (default: ./avpvs)

rrao 2019
```

If you run the avpvs script, please be carefully with the arguments videosegment and src.

## Structure
TBD


## Licence
GNU General Public License v3. See LICENSE file in this repository.

