# this script creates a table for annotations that can be embedded in a static html webpage.

import os, csv

csvFile = open('slides.csv', 'r', encoding='utf8')

fieldNames = (
    "id",
    "strCaption",
    "strLocation",
    "strMedium",
    "relCreatedBy",
    "relTimestamp",
    "relRelatedTopicNodes",
    "relRelatedNodes")

reader = csv.DictReader(csvFile, fieldnames=fieldNames)
next(reader)

for row in reader:
  idstr   = row['id']
  number  = row['id'][-3:]

  caption = row['strCaption']

  if row['relCreatedBy'] != '':
    caption = caption + f" Taken by {row['relCreatedBy']}."

  #if row['relCreatedBy'] == 'Janie Tippett':
  #  caption = caption + " Taken iby Janie Tippett."

  str =       f'          <figure>\n'
  str = str + f'            <span>{number}</span>\n'
  str = str + f'            <img src="img/{idstr}.jpg"\n'
  str = str + f'                 alt="{caption}" />\n'
  str = str + f'            <figcaption>\n'
  str = str + f'              {caption}\n'
  str = str + f'            </figcaption>\n'
  str = str + f'          </figure>'

  print(str)
