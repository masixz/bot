import pandas as pd
import json

datapath = r"C:\Users\TomiK\OneDrive\Desktop\Koulutehtävät\bot\Materials.xlsx"
outpath = r"C:\Users\TomiK\OneDrive\Desktop\Koulutehtävät\bot\Materials.json"

data = pd.read_excel(datapath)

id = data.OBJ_ID_MAT
name = data.Object_Name
dim = data.Dimensions
uom = data.Unit_Of_Measure
strd = data.International_Standard
bm = data.Basic_Material2
remark = data.Remarks
mass = data.Mass
density = data.Density
price = data.eur_kg

container = { }

x = 0

while x<len(id):

    container [id[x]] = [
        {"Name: ":name[x],},
        {"Dimensions: ":dim[x],},
        {"Unit of measure: ":uom[x],},
        {"International standard: ":strd[x],},
        {"Basic material: ":bm[x],},
        {"Remarks: ":remark[x],},
        {"Mass: ":mass[x],},
        {"Density: ":density[x],},
        {"Price: ":price[x],},
       

        ]
    x = x+1

df=pd.DataFrame(container)
df.to_json(outpath, indent=4)



