# -*- coding: utf-8 -*-

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='692a9ce7cbc846f19facd68123c1f0a5')

model = app.models.create('impressionism', concepts=['monet'])

winterVethuil1 = ClImage(url='https://www.wga.hu/detail/m/monet/05/1vethe2.jpg', concepts=['monet'])
winterVethuil2 = ClImage(url='https://www.wga.hu/detail/m/monet/05/1vethe3.jpg', concepts=['monet'])

app.inputs.bulk_create_images([winterVethuil1, winterVethuil2])

# search by image url
print app.inputs.search_by_image(url="https://www.wga.hu/detail/m/monet/05/1vethe2.jpg")

model.train()

model.predict([winterVethuil1])
