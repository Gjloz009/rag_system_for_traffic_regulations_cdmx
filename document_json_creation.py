import pdfplumber
import pandas as pd
import json 

def parrafo(text,i,j,df=None):
    parrafo = text.split(" \n \n")
    new_parrafo = ' \n \n'.join(parrafo[i:j])
    if df is None:
        return new_parrafo
    else :
        return new_parrafo + " \n \n" + df.to_string()

def replace_spaces(num_1):
    for i, outer_list in enumerate(beta[num_1][1]):
        for j, inner_list in enumerate(outer_list):
            beta[num_1][1][i][j] = inner_list.replace("\n", " ")



url = "./Reglamento-de-Transito-CDMX.pdf"

table_settings = {
    "vertical_strategy": "lines",
    "horizontal_strategy": "lines",
    "snap_x_tolerance": 10
}

beta = {}


with pdfplumber.open(url) as pdf:
    alpha = [page.extract_text(keep_blank_chars=True) for page in pdf.pages]
    for page in pdf.pages:
        table = page.find_table()
        if table is not None:
            beta[page.page_number] = (page.crop(table.bbox),page.extract_table(table_settings),page.to_image())

replace_spaces(10)
replace_spaces(11)
replace_spaces(67)
replace_spaces(132)

df = pd.DataFrame(beta[10][1][1:],columns=beta[10][1][0])
df_2 = pd.DataFrame(beta[11][1][0:],columns=beta[10][1][0])
df_3 = pd.DataFrame(beta[67][1][1:],columns=beta[67][1][0])
df_4 = pd.DataFrame(beta[68][1][0:],columns=beta[67][1][0])
df_5 = pd.DataFrame(beta[132][1][1:],columns=beta[132][1][0])

df_12 = pd.concat([df,df_2],axis=0,ignore_index=True)
df_34 = pd.concat([df_3,df_4],axis=0,ignore_index=True)

alpha[9] = parrafo(alpha[9],0,-2,df_12)
alpha[10] = parrafo(alpha[10],2,14)
alpha[66] = parrafo(alpha[66],0,-2,df_34)
alpha[67] = parrafo(alpha[67],2,15)
alpha[131] = parrafo(alpha[131],0,-7,df_5)

# hasta la 74 (75 documento)
sample = alpha[:74]

joined_sample = " \n \n".join(sample)
splitted_sample = joined_sample.split("TÍTULO")

corrected_sample = []
for i,celda in enumerate(splitted_sample):
    for articulo in celda.split("Artículo"):
        a = {}
        a["Título"] = f"Título {i}"
        a["Artículo"] = "Artículo"+articulo
        a["Artículo"] = a["Artículo"].replace("\n \n \n \n  \n \n \n"," \n \n")
        a["Artículo"] = a["Artículo"].replace("\n \n \n  \n \n \n"," \n")
        
        corrected_sample.append(a)

c = corrected_sample[2::]

lista_quitar = [c[4],c[29],c[38],c[46],c[66],c[67],c[70]]

almost_final = [x for x in c if x not in lista_quitar]

for indice in [5,12,18,20,23,32,38,49,52,58,68]:
    almost_final[indice]['Artículo'] = parrafo(almost_final[indice]['Artículo'],0,-2)

for indice in [44,60,69]:
    almost_final[indice]['Artículo'] = almost_final[indice]['Artículo'] + almost_final[indice + 1]['Artículo']

final = [x for x in almost_final if x not in [almost_final[45],almost_final[61],almost_final[70]]]


with open('documents.json', 'wt') as f_out:
    json.dump(final, f_out, indent=2, ensure_ascii=False)


'''
Borrar lo de abajo:
f[5]['Artículo']
f[12]['Artículo']
(f[18]['Artículo']
f[20]['Artículo'])
f[23]['Artículo']
f[32]['Artículo']
f[38]['Artículo']
f[49]['Artículo']
f[52]['Artículo']
f[58]['Artículo']
f[68]['Artículo']

Juntar :
f[44]['Artículo'] - f[45]['Artículo']
f[60]['Artículo'] - f[61]['Artículo']
f[69]['Artículo'] - f[70]['Artículo']
'''
'''
for i, outer_list in enumerate(beta[10][1]):
    for j, inner_list in enumerate(outer_list):
        beta[10][1][i][j] = inner_list.replace("\n", " ")
        
for i, outer_list in enumerate(beta[11][1]):
    for j, inner_list in enumerate(outer_list):
        beta[11][1][i][j] = inner_list.replace("\n", " ")
        
for i, outer_list in enumerate(beta[67][1]):ñ
    for j, inner_list in enumerate(outer_list):
        beta[67][1][i][j] = inner_list.replace("\n", " ")

for i, outer_list in enumerate(beta[68][1]):
    for j, inner_list in enumerate(outer_list):
        beta[68][1][i][j] = inner_list.replace("\n", " ")

for i, outer_list in enumerate(beta[132][1]):
    for j, inner_list in enumerate(outer_list):
        beta[132][1][i][j] = inner_list.replace("\n", " ")

#alpha[10] = " \n \n".join(alpha[10].split(" \n \n")[2:])
#alpha[67] = " \n \n".join(alpha[67].split(" \n \n")[2:])
'''
