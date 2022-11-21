from typing import TypedDict
import pandas as pd
import json
import os


class Data_Temp(TypedDict):
    tag: str
    patterns: list
    responses: list


datapath = os.path.join(os.path.dirname(__file__), "Materials.xlsx")
fn = os.path.join(os.path.dirname(__file__), "Materials.json")
fn2 = os.path.join(os.path.dirname(__file__), "intents.json")

excel_data_df = pd.read_excel(datapath)
excel_data_df.to_json(fn, orient="records")
with open(fn) as json_file:
    data = json.load(json_file)

data321 = {"intents": []}
for i, key in enumerate(data):

    sdy1 = data[i]["OBJ_ID_MAT"]
    sdy2 = data[i]["Object_Name"]
    sdy3 = data[i]["Dimensions"]
    sdy4 = data[i]["Unit_Of_Measure"]
    sdy5 = data[i]["International_Standard"]
    sdy6 = data[i]["Basic_Material2"]
    sdy7 = data[i]["Remarks"]
    sdy8 = data[i]["Mass"]
    sdy9 = data[i]["Density"]
    sdy10 = data[i]["eur_kg"]

    m = Data_Temp(tag=sdy1, patterns=[sdy1], responses=[
                  sdy1, sdy2, sdy3, sdy4, sdy5, sdy6, sdy7, sdy8, sdy9, sdy10])

    data321["intents"].append(m)

with open(fn2, "w") as newjson:
    json.dump(data321, newjson)

# print(lopullinen_data)
# with open("intents.json",fn2) as outfile:
#     outfile.write(lopullinen_data)