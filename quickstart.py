# -*- coding: utf-8 -*-

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage

      
app = ClarifaiApp(api_key='692a9ce7cbc846f19facd68123c1f0a5')
      
      # get the general model
      
model = app.models.get('general-v1.3')
image = ClImage(url='https://samples.clarifai.com/metro-north.jpg')
print(model.predict([image]))
