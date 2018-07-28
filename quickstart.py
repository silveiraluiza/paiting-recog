# -*- coding: utf-8 -*-

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage


app = ClarifaiApp(api_key='692a9ce7cbc846f19facd68123c1f0a5')

# Criando um modelo utilizando conceitos
# model = app.models.create('impressionism', concepts=['monet'])

# Utilizando um modelo já existente
model = app.models.get('impressionism')

# Adicionando imagens com conceitos via url
winterVethuil1 = ClImage(url='https://www.wga.hu/detail/m/monet/05/1vethe2.jpg', concepts=['monet'])
winterVethuil2 = ClImage(url='https://www.wga.hu/detail/m/monet/05/1vethe3.jpg', concepts=['monet'])

# Adicionando imagens criadas ao app
# app.inputs.bulk_create_images([winterVethuil1, winterVethuil2])

# Treinando o modelo com imagens adicionadas
# model.train()

#Fazendo predição
model.predict([winterVethuil1])
