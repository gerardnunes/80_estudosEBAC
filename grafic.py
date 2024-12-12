import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import os
import sys

def gerargrafic(base, value, index, func, ylabel, xlabel):
    tabela = pd.pivot_table(base, values=value, index=index, aggfunc=func)
    tabela.sort_values(by=value).plot(figsize=[18, 6])
    plt.ylabel(ylabel)
    plt.xlabel(xlabel)

mes1 = sys.argv[1]
mes2 = sys.argv[2] 
mes3 = sys.argv[3]
mes4 = sys.argv[4]
mes5 = sys.argv[5]

meses = [mes1, mes2, mes3, mes4, mes5]

for mes in meses:
    
    sinas = pd.read_csv(f"./bases/SINASC_RO_2019_{mes}.csv")
    max_data = sinas['DTNASC'].max()[:7]    
    output_dir = f'./output/figs_{max_data}'
    os.makedirs(output_dir, exist_ok=True)
    

    gerargrafic(sinas, "IDADEMAE", "DTNASC", 'mean', "Idade média da mãe", "Data de nascimento")
    plt.savefig(f'{output_dir}/media_idade_mae.png')
    
    gerargrafic(sinas, "IDADEMAE", "DTNASC", 'count', "Contagem de idades das mães", "Data de nascimento")
    plt.savefig(f'{output_dir}/contagem_idade_mae.png')
    
    gerargrafic(sinas, "IDADEMAE", ["DTNASC", 'SEXO'], 'count', "Contagem de idades das mães", "Sexo do bebê")
    plt.savefig(f'{output_dir}/contagem_sexo_bebe.png')
    
    gerargrafic(sinas, "IDADEMAE", ["DTNASC", 'SEXO'], 'mean', "Idade média da mãe", "Sexo do bebê")
    plt.savefig(f'{output_dir}/media_sexo_bebe.png')
    
    gerargrafic(sinas, "PESO", "ESCMAE", 'median', "Peso médio do bebê", "Escolaridade da mãe")
    plt.savefig(f'{output_dir}/media_escolaridade_mae.png')
    
    gerargrafic(sinas, "APGAR1", "GESTACAO", 'mean', "APGAR1 médio", "Gestação")
    plt.savefig(f'{output_dir}/media_apg1_gestacao.png')


plt.close('all')
