# Sutton Family Home Videos

Date: 2024-10-07

- Original camcorder RCA analog 8mm
- Last camcorder Sony digital 8mm with Firewire interface
- I think iMovie app on macOS
  - Imports analog video as a single large movie file
  - Imports digital video based on start/stop timestamps as individual mov file
- mov file is Apples Quicktime format
- mp4 is maybe 10x smaller than mov, but image quality may be less
- On mac, the path to iMovie library is a package ( a hidden folder ). Example:
    `/Users/sutton/Movies/iMovie Library.imovielibrary`
- This Seagate 2TB drive contains a backup from a drive removed from a iMac 27 Late 2012 model
- This copy is missing all large files > 4 GB because I could only format as FAT and 4GB file is the limit
- This copy is missing about 20 more video tapes that have not been imported

## Rsync Command Used to Create Backup

I had to set a max file limit of 4GB due to FAT. 

## Python Script to Convert a Folder of mov files to mp4

find_mov_files.py

1) Search all folder in iMovie Library.imovielibrary
2) Locate each folder named "Original Movie" containing *.mov file(s)
   1) Create a text file with each mov file with filename enclosed in quotes and prepended by "file ".  This file is named list.txt
   2) Use ffmpeg merge all *.mov files contained in list.txt into a single merged-movies.mov
   3) Use ffmpeg to convert merged-movies.mov to H.264 merged-movies.mp4. 


```
ffmpeg -f concat -i files_to_combine.txt merged.mov

# I don't think this worked, concatenating directly from mov to mp4
ffmpeg -f concat -i files_to_combine.txt -f mp4 merged.mp4


# I think this worked
ffmpeg -i {in-video}.mov -vcodec h264 -acodec aac {out-video}.mp4

ffmpeg -i merged.mov -vcodec h264 -acodec aac merged.mp4
```




