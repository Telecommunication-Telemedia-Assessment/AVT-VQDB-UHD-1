# Codec Retraining

This folder contains a data set that can be used for retraining the Pv component (P.1203.1) for different codecs.

It consists of HD-encoded video sequences using VP9, AV1 and HEVC as codecs.

As encoders, the following were used with ffmpeg:

- libaom-av1
- libvpx
- libx265

The data in the CSV file is structured as follows:

- `video`: The encoded video name
- `src`: Original source video name (part of the main AVT-VQDB-UHD1 databases)
- `codec`: The used codec (av1, hevc, vp9)
- `bitrate_kbits`: The encoded bitrate
- `fps`: The used fps
- `height`: The encoded video height
- `width`: The encoded video width
- `resolution`: The encoded video resolution
- `Q`: The quality as judged by VMAF v0.6.1
