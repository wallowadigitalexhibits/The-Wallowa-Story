# The Wallowa Story

This short film, restored from a narrated slide presentation from 1987, tells the history of Wallowa County.

<img src="https://github.com/wallowadigitalexhibits/the-wallowa-story/blob/main/site/img/wallowastory001.jpg" width="300">

## Introduction

The Wallowa Story was originally created in honor of Wallowa County's first centennial birthday in 1987. Working with both contemporary and historical photographs, a group of local historians developed 279 slides, wrote a 47-minute narrative, and commissioned local KWVR radio announcer Dave Nelson to record an audio cassette.

The presentation premiered to standing room only at the OK Theater in the Wallowa County seat of Enterprise, Oregon. Partially funded by the Oregon Council for the Humanities, volunteers then took the presentation on the road to schools and state parks in neighboring counties.

To restore the film, the audio was recorded from an original cassette tape and the slides were individually scanned. The resulting video was shown to a full house at the Wallowa History Center on July 4, 2022, thirty-five years after its creation. The Wallowa Story remains an excellent, near-comprehensive introduction to local history.

This restoration was completed with the support of surviving members of the The Wallowa Story Working Committee. You may arrange showings and provide copies of these materials so long as the intent is to educate and no money is being made.

The website is live at <a href="https://thewallowastory.com">https://thewallowastory.com</a>.

For more information, contact <a href="mailto:info@wallowadigitalexhibits.org">info@wallowadigitalexhibits.org</a>.

## Technical Details

We scanned the 279 slides in batches using an Epson v800 Perfection scanner at the Wallowa Public Library in 2021. We recovered an audio cassette but were unable to sync the original slide carousel timing to the audio tape in a way that seemed accurate, and at the time we had no other sources of the original video. Of course, a VHS tape materialized as soon as work was completed. So it goes.

Instead, we recorded the audio cassette to the computer and saved it as an mp3. 

The audio was uploaded to <a href="https://otter.ai">Otter.ai</a>, which gave us a fairly good transcription.

Armed with the mp3 audio, the text transcription, and a set of jpg images, we turned to the task of syncing up the slides with the audio to create an mp4 video.

### Building the Video with FFMPEG

We constructed the following ffmpeg command and created a video out of the first ten slides, each appearing on the screen for six seconds each. All preparation work was done on a laptop running Linux Mint 18. 

```
ffmpeg -y \
  -loop 1 -t 6 -i wallowastory-001.jpg \
  -loop 1 -t 6 -i wallowastory-002.jpg \
  -loop 1 -t 6 -i wallowastory-003.jpg \
  -loop 1 -t 6 -i wallowastory-004.jpg \
  -loop 1 -t 6 -i wallowastory-005.jpg \
  -loop 1 -t 6 -i wallowastory-006.jpg \
  -loop 1 -t 6 -i wallowastory-007.jpg \
  -loop 1 -t 6 -i wallowastory-008.jpg \
  -loop 1 -t 6 -i wallowastory-009.jpg \
  -loop 1 -i wallowastory-010.jpg \
  -i wallowastory_v2_denoised.mp3 \
  -filter_complex "[0]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i0];
 [1]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i1];
 [2]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i2];
 [3]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i3];
 [4]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i4];
 [5]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i5];
 [6]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i6];
 [7]scale=720:460:force_original_aspect_ratio=decrease,pad=720:460:(ow-iw)/2:(oh-ih)/2,setsar=1[i7];
 [i0][i1][i2][i3][i4][i5][i6][i7]concat=n=8" \
 -shortest \
  -c:v libx264 -pix_fmt yuv420p -c:a aac wallowastory.mp4
```

Writing this command by hand for 279 slides, each of which are on screen for varying lengths of time, was clearly a non-starter. We therefore turned to Python and, in the proud tradition of the Wallowa History Center, started with a spreadsheet.

First, we created a `slides.csv` file that contained one row per slide image, with the following columns:

- photoId
- durationSecs
- photographer
- annotation

Next, we listened to the audio and noted where each slide should be placed, and fixed up the transcription at the same time. Once we had the timing right, we wrote a Python file to construct the ffmpeg command.

&raquo; <a href="genffmpeg.py">genffmpeg.py</a>

The resulting mp4 video was uploaded to YouTube.

### Building the Website

The website uses the Carnivale Freakshow and EduSABeginner fonts, both of which are licensed for use without conditions. 

The intent of the website was to make a resource that could be cited by scholars. To that end, we provided the video, the audio mp3, the transcript, and a table of the annotated slides.

### Generating an Annotated Table

Again, we turned to Python to generate the HTML table of annotated slides, and again we started with a spreadsheet to collect annotations as we talked with oldtimers and historians. 

For each slide, we tried to determine the subject, the photographer, and the broader historical significance of each photo. We also looked for the personal significance---why was this photo chosen in particular? 

Once we felt we'd captured that information, we imported that spreadsheet using the same technique as we did with the `genffmpeg.py`. The resulting HTML was hand-pasted onto the page. 

&raquo; <a href="genannotatedtable.py">genannotatedtable.py</a>

### Preparing Images for the Annotated Table

We wanted all 279 slides to be searchable with Ctrl+F in the browser on one page, so we shrunk the slide images down using ImageMagick and added the `loading="lazy"` attribute to the HTML page. The total image load still ends up being 55MB, but the captions slow down the reader's scrolling and the page is very usable. 

```
<img loading="lazy"
     src="img/wallowastory099.jpg"
     alt="Caption reads, “Passing Joseph Sept [?] Enroute to the Tenderfoot Mining Camp, loaded with machinery for the [20?] stamp mill.“ The Tenderfoot Mine was “salted with gold“ to fool investors." />
```
