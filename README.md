# makesense_csv_to_coco

Modify a single csv result created with [makeense.ai](https://github.com/SkalskiP/make-sense) to coco format.
Results from makesense do not include category information.  
A csv file with category information is required.  

```bash
python main.py
```


## sample data
The data used as an example is the COCO2017 Val 000000000139.jpg and the modified JSON

### [categories csv sample](coco_sample/annotations/categories.csv)

|  | supercategory | id | name |
|---|---|---|---|
| 0 | person | 1 | person |
| 1 | furniture | 62 | chair |
| 2 | furniture | 64 | potted plant |
| 3 | furniture | 67 | dining table |
| 4 | electronic | 72 | tv |
| 5 | appliance | 78 | microwave |
| 6 | appliance | 82 | refrigerator |
| 7 | indoor | 84 | book |
| 8 | indoor | 85 | clock |
| 9 | indoor | 86 | vase |

### [sample makesense result single csv](coco_sample/annotations/labels_my-project-name_2023-07-25-03-19-19.csv)

| label_name | bbox_x | bbox_y | bbox_width | bbox_height | image_name | image_width | image_height |
|---|---|---|---|---|---|---|---|
| potted plant | 237 | 143 | 25 | 70 | 000000000139.jpg | 640 | 426 |
| tv | 7 | 168 | 149 | 95 | 000000000139.jpg | 640 | 426 |
| tv | 557 | 209 | 81 | 79 | 000000000139.jpg | 640 | 426 |
| chair | 359 | 218 | 56 | 103 | 000000000139.jpg | 640 | 426 |
| chair | 291 | 218 | 62 | 98 | 000000000139.jpg | 640 | 426 |
| chair | 413 | 223 | 30 | 81 | 000000000139.jpg | 640 | 426 |
| chair | 317 | 219 | 22 | 12 | 000000000139.jpg | 640 | 426 |
| person | 413 | 158 | 53 | 138 | 000000000139.jpg | 640 | 426 |
| person | 384 | 172 | 15 | 36 | 000000000139.jpg | 640 | 426 |
| microwave | 512 | 206 | 15 | 16 | 000000000139.jpg | 640 | 426 |
| refrigerator | 493 | 174 | 20 | 108 | 000000000139.jpg | 640 | 426 |
| book | 605 | 306 | 14 | 46 | 000000000139.jpg | 640 | 426 |
| book | 613 | 308 | 13 | 46 | 000000000139.jpg | 640 | 426 |
| clock | 448 | 121 | 14 | 22 | 000000000139.jpg | 640 | 426 |
| vase | 549 | 309 | 37 | 90 | 000000000139.jpg | 640 | 426 |
| vase | 351 | 209 | 11 | 23 | 000000000139.jpg | 640 | 426 |
| chair | 412 | 219 | 10 | 13 | 000000000139.jpg | 640 | 426 |
| vase | 241 | 195 | 14 | 18 | 000000000139.jpg | 640 | 426 |
| vase | 337 | 200 | 10 | 17 | 000000000139.jpg | 640 | 426 |
| dining table | 321 | 231 | 126 | 89 | 000000000139.jpg | 640 | 426 |

## Result coco format json
[Result coco format json](coco_sample/annotations/annotation.json)