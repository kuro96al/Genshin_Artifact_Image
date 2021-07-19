import csv
import pprint
import requests

with open('artifact.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        img_data = requests.get("https://upload-os-bbs.mihoyo.com/game_record/genshin/equip/"+row[1]+".png").content
        with open(row[0]+'.png', 'wb') as handler:
            handler.write(img_data)