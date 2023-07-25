

import os 
import json
import argparse
import pandas as pd
from pathlib import Path
from PIL import Image, ImageOps
from collections import OrderedDict


def makesense_single_csv_to_coco_json(
        result_csv_path, 
         image_path, 
         categories_csv_path, 
         coco_result_save_path):
    '''
    Modify the result of single csv in makesense and change it to coco format.
    Results from makesense do not include category information.
    A csv file with category information is required.
        
    Args:
        result_csv_path : makeense single csv result path
        image_path : images path
        categories_csv_path :  Path to the csv file where additional categories information
        coco_result_save_path : coco format json save path
    '''
    df = pd.read_csv(result_csv_path)
    categories_df = pd.read_csv(categories_csv_path,index_col=0)

    images_info = []
    pog_categories = []
    annotations_info = []

    unique_images = df.image_name.unique()
    id_dict = {name_ : num_ for num_, name_ in enumerate(unique_images)}

    # categories setup
    for num, category_ in categories_df.iterrows():
        pog_categories.append({key_ : info_ for key_, info_ in category_.items()})

    categories_dict = { category['name'] : category  for _, category in categories_df.iterrows()}

    # images setup
    for image_name in unique_images:
        file_path = Path(os.path.join(image_path , image_name))
        imag = Image.open(file_path)
        imag = ImageOps.exif_transpose(imag)
        w, h = imag.size

        images_dict = OrderedDict()
        images_dict['id'] = id_dict[image_name]
        images_dict["width"] = w
        images_dict["height"] = h
        images_dict["file_name"] = image_name
        images_info.append(images_dict)

    # annotations setup
    for num, anno_ in df.iterrows():
        annotations_dict = OrderedDict()
        x1, y1 = anno_['bbox_x'], anno_['bbox_y']
        w, h = anno_['bbox_width'], anno_['bbox_height']

        annotations_dict["id"] = num
        annotations_dict["category_id"] = categories_dict[anno_['label_name']]['id']
        annotations_dict["image_id"] = id_dict[anno_['image_name']]
        annotations_dict["area"] = int(w*h)
        annotations_dict["iscrowd"] = 0
        annotations_dict["bbox"] = [int(x1), int(y1), int(w), int(h)]

        annotations_info.append(annotations_dict)


    # result json setup
    coco_format = OrderedDict()
    coco_format['images'] = images_info
    coco_format['categories'] = pog_categories
    coco_format['annotations'] = annotations_info

    with open(coco_result_save_path,'w') as js:
        json.dump(coco_format,js)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    
    parser.add_argument("--result_csv_path", type=str, default='coco_sample/annotations/labels_my-project-name_2023-07-25-03-19-19.csv', help="makeense single csv result path")
    parser.add_argument("--image_path", type=str, default='coco_sample/images/', help="Base images folder")
    parser.add_argument("--categories_csv_path", type=str, default= 'coco_sample/annotations/categories.csv', help="Path to the csv file where additional categories information")
    parser.add_argument("--coco_result_save_path", type=str, default='coco_sample/annotations/annotation.json', help="coco format json save path")

    args = parser.parse_args()
    
    result_csv_path = args.result_csv_path
    image_path = args.image_path
    categories_csv_path = args.categories_csv_path
    coco_result_save_path = args.coco_result_save_path

    makesense_single_csv_to_coco_json(
        result_csv_path, 
        image_path, 
        categories_csv_path, 
        coco_result_save_path)