# -*- coding: utf-8 -*-

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import csv

app = ClarifaiApp(api_key='##putkey')


def addImages(link, concept_list):
    app.inputs.create_image_from_url(link, concepts=concept_list)

def catchImages(data):
    link = ""
    concept_list = []
    f = open("output.txt","w")
    with open(data, 'rb') as csvfile:
        datapainting = csv.reader(csvfile, delimiter=',')
        n=0
        for row in datapainting:
            n += 1
            if (n<=100 and n>1):
                link = row[6]
                concept_list.append(row[0])
                concept_list.append(row[7])
                addImages(link,concept_list)
                concept_list = []


data = "dados/paintings.csv"
#catchImages(data)
#model = app.models.create(model_id="puppy", concepts=["my puppy"]) modify to our context
model = app.models.get('impressionism')

#winterVethuil1 = ClImage(url='https://www.wga.hu/detail/m/monet/05/1vethe2.jpg', concepts=['monet']) put another

#addImages(winterVethuil1) 

# search by image url
#print app.inputs.search_by_image(url="https://www.wga.hu/detail/m/monet/05/1vethe2.jpg")

#model.train()

#print(model.predict([winterVethuil1]))
