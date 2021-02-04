# [AVT-VQDB-UHD-1](https://telecommunication-telemedia-assessment.github.io/AVT-VQDB-UHD-1/)
This is a repository with data related to the 4K databases that are published at IEEE-ISM 2019.

If you use any of the data or code please cite the following paper

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
## Download of source videos and segments
To download all video segments and source videos (in total around 55GB) use the provided download tool, e.g. a `./download.py --help` call will show you the following help:

```
usage: download.py [-h] [--no_sources] [--output OUTPUT]

download video segments and source videos

optional arguments:
  -h, --help       show this help message and exit
  --no_sources     download no sources (default: False)
  --output OUTPUT  specify a different output directory (default: working directory)


stg7 2019
```

You can also use your favourite download tool, check the base_url defined in `download.py`.

## AVPVS generation
To run, e.g., full reference models, it is required to perform a conversion to match the same resolution and framerate of the distorted video to the corresponding source video.
For this you can use the script `gen_avpvs.py`.
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

If you run the avpvs script, please be careful with the arguments videosegment and src.

## Structure
We shortly describe the folder structure used in this repository and after downloading of all additional files.

```
src_videos --> source vidoes for all tests

# for each test
test_X/mos_ci.csv --> subjective ratings with CI values
test_X/metadata.csv --> video meta-data for all video segments
test_X/objective_scores.csv --> calculated objective video quality scores
test_X/segments --> all encoded videos used in the test

test_X/brisque_reports --> extracted features for brisque model
test_X/niqe_reports --> extracted features for niqe model
test_X/vmaf_reports --> all per frame vmaf and other full ref scores

# siti
siti/*.csv --> SI/TI scores for each SRC video, according to ITU-T Rec. P.910
```


## License for the code
GNU General Public License v3. See LICENSE file in this repository.

## Licence for the shared videos
This database consists of short term videos based on several short movies, that are either public available or created by TU Ilmenau.
The tools provided in this repository can be used to download the shared videos that are used in the described video quality tests.
In the following we specify the common filename prefix, to identify the source and corresponding licence of the video.
This applies to encoded and source videos that are shared within this database.
For example all files that can be downloaded with the prefix `bigbuck_bunny` are based on the Big Bucks Bunny content and follow the corresponding licence.

We are happy that it was possible to access and use all the external video sources.
  * `bigbuck_bunny`: a short 8-10s cut from [Big Bucks Bunny](https://peach.blender.org/about/): [Creative Commons Attribution 3.0](http://creativecommons.org/licenses/by/3.0/)
  * `Sparks`: two short 8-10s cuts from [Netflix Sparks movie](http://download.opencontent.netflix.com/?prefix=TechblogAssets/Sparks/): [license](http://download.opencontent.netflix.com.s3.amazonaws.com/TechblogAssets/Sparks/sparks_license.txt)
  * `water_netflix`: two short 8-10s cuts from Netflix El Fuente: [license](http://download.opencontent.netflix.com.s3.amazonaws.com/TechblogAssets/Sparks/sparks_license.txt)


Our own contents follows the [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](https://creativecommons.org/licenses/by-nc/4.0/) licence.
  * `Dancers_8s`
  * `cutting_orange_tuil`
  * `fr-041_debris`
  * `Daydreamer`
  * `vegetables`
  * `Giftmord`
