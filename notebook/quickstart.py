# -*- coding: utf-8 -*-

from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import pandas as pd
import csv

app = ClarifaiApp(api_key='211d6ec030764627b5b07984b4881cda')
#paintings = pd.read_csv('../dados/paintings.csv') #read data and name columns
paintings = pd.read_csv('../dados/treino.csv',sep = ';', encoding='latin-1')

all_concepts = []
todos_autores = []
todas_escolas = []
todas_tecnicas = []
i = 0
for index, row in paintings.iterrows():
    if i < 1000:
        tecnica = row['TECHNIQUE'].split(',')[0]
        autor = row['AUTHOR']
        escola = row['SCHOOL']
        all_concepts = all_concepts + [tecnica, autor, escola]
        todos_autores.append(autor)
        todas_escolas.append(escola)
        todas_tecnicas.append(tecnica)
        
        i = i+1
    
all_concepts = list(set(all_concepts))
todas_escolas = list(set(todas_escolas))
todos_autores = list(set(todos_autores))
todas_tecnicas = list(set(todas_tecnicas))

print(len(all_concepts), len(todas_escolas), len(todas_tecnicas),len(todos_autores))

app.inputs.delete_all()

i = 0
for index, row in paintings.iterrows():
    if i < 1001:
        print(i)
        tecnica = row['TECHNIQUE'].split(',')[0]
        autor = row['AUTHOR']
        url = row['URL']
        escola = row['SCHOOL']
        concepts_list = [tecnica, escola, autor]
        not_concepts_list = [i for i in all_concepts if i not in concepts_list]
        app.inputs.create_image_from_url(url, concepts=concepts_list, not_concepts=not_concepts_list)
        i = i +1
    else:
        break

model = app.models.create('Paintings-rec', concepts=all_concepts)

model = app.models.get('Paintings-rec')

model.train()

def getInfo(prediction):
    output = prediction['outputs'][0]
    concepts = output['data']['concepts']

image = ClImage(url='https://www.wga.hu/detail/a/aachen/allegory.jpg')
image2 = ClImage(url='https://www.wga.hu/detail/a/ademollo/ark.jpg')
image3 = ClImage(url='https://www.wga.hu/detail/a/albani/1/4winter.jpg')
image4 = ClImage(url='https://upload.wikimedia.org/wikipedia/commons/f/f4/Aachen_Saint_Sebastian.jpg')
image5 = ClImage(url='https://www.wga.hu/detail/a/aelst/hunting2.jpg')
image6 = ClImage(url='https://www.wga.hu/detail/a/aertsen/christ.jpg')

columns = ['AUTHOR_EXPECTED', 'AUTHOR_PREDICTED', 'TECHNIQUE_EXPECTED', 'TECHNIQUE_PREDICTED','SCHOOL_EXPECTED', 'SCHOOL_PREDICTED', "MATCHES"]
df = pd.DataFrame(columns=columns)

i = 0
teste = pd.read_csv('../dados/teste.csv',sep = ';', encoding='latin-1')
for index, row in teste.iterrows():
    tecnica = row['TECHNIQUE'].split(',')[0]
    autor = row['AUTHOR']
    url = row['URL']
    escola = row['SCHOOL']
    image = ClImage(url=url)
    result = model.predict([image])['outputs'][0]['data']['concepts']
    pred_autor = False
    pred_tecnica = False
    pred_escola = False
    total = 0
    for concept in result:
        conceito = concept['name']
        if ((not pred_autor) and conceito in todos_autores):
            pred_autor = conceito
            if pred_autor == autor:
                total += 1
        if ((not pred_escola) and conceito in todas_escolas):
            pred_escola = conceito
            if pred_escola == escola:
                total += 1
        if ((not pred_tecnica) and conceito in todas_tecnicas):
            pred_tecnica = conceito
            if pred_tecnica == tecnica:
                total +=1
    df_data = [autor, pred_autor, tecnica, pred_tecnica, escola, pred_escola]
    df_data.append(total)
    print(df_data)
    line = pd.DataFrame([df_data],columns=columns)    
    if i == 0:
        df = line
    else:
        df = df.append(line)
    i = i+1

df.to_csv('test_results.csv', sep=',')
img1 = ClImage(url="https://samples.clarifai.com/puppy.jpeg", concepts=['boscoe'], not_concepts=['our_wedding'])
img2 = ClImage(url="https://samples.clarifai.com/wedding.jpg", concepts=['our_wedding'], not_concepts=['cat','boscoe'])

app.inputs.bulk_create_images([img1, img2])
