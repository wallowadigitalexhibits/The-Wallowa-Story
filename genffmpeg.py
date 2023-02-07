# this script creates a custom ffmpeg statement for combining slides from The Wallowa Story
# with Dave Nelson's 1987 audio tape (mp3) recorded from the last remaining cassette tape.
#
# the default duration an image will stay on screen is 15 seconds
# add the three-digit ID number to the custom secsToDisplayLength arrays
# to set alternate durations for certain images

import os, csv

str = "ffmpeg -y \\\n"

inputAudioFileName = "wallowastory_v2_denoised.mp3"
outputVideoFileName = "wallowastory.mp4"

csvFile = open('slides.csv', 'r', encoding='utf8')

lastIdStr = 279 

fieldNames = (
    "photoId",
    "durationSecs",
    "photographer",
    "annotation")

reader = csv.DictReader(csvFile, fieldnames=fieldNames)

for row in reader:
  str = str + f" -loop 1 -t {row['durationSecs']} -i wallowastory{row['photoId']}.jpg \\\n"

# capture the last slide, which should remain on screen until the audio terminates

str = str + f" -loop 1 -i wallowastory{lastIdStr}.jpg \\\n"

# add the input file statement

str = str + f" -i {inputAudioFileName} \\\n"

# add the set of filter_complex statements for all the images

height = "460"
width = "720"

str = str + ' -filter_complex "'

for index in range(0, lastIdStr):
    str = str + f'[{index}]scale={width}:{height}:force_original_aspect_ratio=decrease,pad={width}:{height}:(ow-iw)/2:(oh-ih)/2,setsar=1[i{index}];\n'

for index in range(0, lastIdStr):
    str = str + f'[i{index}]'

str = str + f'concat=n={lastIdStr}" \\\n'

# print the output format commands

str = str + f' -shortest -c:v libx264 -pix_fmt yuv420p -c:a aac {outputVideoFileName}'

# swap the comments to fire off the resulting command on your system
# print the result

print(str)
#os.system(str)
