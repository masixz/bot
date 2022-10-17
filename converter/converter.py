from operator import index
import pandas as pd
import json
import os

datapath = os.path.join(os.path.dirname(__file__), 'Materials.xlsx')
fn = os.path.join(os.path.dirname(__file__), 'Materials.json')

excel_data_df=pd.read_excel(datapath)
json_str=excel_data_df.to_json(fn, orient="records")



# data = pd.read_excel(datapath)
# id = data.OBJ_ID_MAT
# name = data.Object_Name
# dim = data.Dimensions
# uom = data.Unit_Of_Measure
# strd = data.International_Standard
# bm = data.Basic_Material2
# remark = data.Remarks
# mass = data.Mass
# density = data.Density
# price = data.eur_kg
# container = { }
# lista=[]
# x = 0

# for i in data.index:
    
#     container [id[x]] = [
#         {"Name: ":name[x],},
#         {"Dimensions: ":dim[x],},
#         {"Unit of measure: ":uom[x],},
#         {"International standard: ":strd[x],},
#         {"Basic material: ":bm[x],},
#         {"Remarks: ":remark[x],},
#         {"Mass: ":mass[x],},
#         {"Density: ":density[x],},
#         {"Price: ":price[x],},]

#     x=x+1
    # lista.append(container)
    

#         ]
# while x<len(id):

#     container [id[x]] = [
#         {"Name: ":name[x],},
#         {"Dimensions: ":dim[x],},
#         {"Unit of measure: ":uom[x],},
#         {"International standard: ":strd[x],},
#         {"Basic material: ":bm[x],},
#         {"Remarks: ":remark[x],},
#         {"Mass: ":mass[x],},
#         {"Density: ":density[x],},
#         {"Price: ":price[x],},
       

#         ]
#     x = x+1

# df=pd.DataFrame(container)
# df.reset_index().to_json(fn,orient="records")



