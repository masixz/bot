import pandas as pd
import json
import os

datapath = os.path.join(os.path.dirname(__file__), 'Materials.xlsx')
fn = os.path.join(os.path.dirname(__file__), 'Materials.json')

excel_data_df=pd.read_excel(datapath)
excel_data_df.to_json(fn, orient="records")
with open(fn) as json_file:
    data = json.load(json_file)
    
sdy1=data[0]['OBJ_ID_MAT']
sdy2=data[0]['Object_Name']
sdy3=data[0]['Dimensions']
sdy4=data[0]['Unit_Of_Measure']
sdy5=data[0]['International_Standard']
sdy6=data[0]['Basic_Material2']
sdy7=data[0]['Remarks']
sdy8=data[0]['Mass']
sdy9=data[0]['Density']
sdy10=data[0]['eur_kg']



sdy=data[0]
names=[]
for jvg in sdy:
    names.append(jvg)

# lists=[]
# for i in data:
#     lists.append(i)
# print(data)

def datan_rakennus():
    data123 = {"intents": [
    {"tag": [],
      "patterns": [],
      "responses": []}]}
    # print(data123["intents"][0]["tag"])
    data123["intents"][0]["tag"] = sdy1
    data123["intents"][0]["patterns"] = sdy1
    data123["intents"][0]["responses"] = sdy1,sdy2,sdy3,sdy4,sdy5,sdy6,sdy7,sdy8,sdy9,sdy10
    lopullinen_data = json.dumps(data123)
    print(lopullinen_data)
datan_rakennus()