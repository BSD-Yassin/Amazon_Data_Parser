import csv 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import time

# importer les fichiers CSV et les merge en une grosse DataFrame
def get_dataframe():
    files_dict = iter([str(f'keywords_filter{i}.csv') for i in range(1,15)])

    sum_df = pd.concat(map(pd.read_csv, files_dict))
    return sum_df

# Nettoyer les data des colonnes non nécessaires
def clean_sortdf(df,drop):
    
    for i in drop:
        del df[i]
    return df

#retourner des rapports
def print_infos(groups,filename):
    with open(str(filename), 'a+') as file:
        for name, group in groups:
            file.writelines('\n')
            file.writelines(name)
            file.writelines('\n')
            
    file.close()

#laisser à la personne le choix de retirer les colonnes qu'elle souhaite via une fonction
def rm_columns(data):
    lst_columns = tuple(output_df.columns)
    print('Les données sont analysés avec ces colonnes :')
    dict_columns = dict()
    for i in lst_columns:
        dict_columns.update({lst_columns.index(i):i})
        print(f'{lst_columns.index(i)}:{i}')
        
    exclude_ipt= ''
    exclude_lst = []
    
    exclude_ipt = input("Veuillez écrire les index des critères à exclure de l'analyse, séparé par une virgule ou écrivez -fin pour ne pas mettre de filtre : ")
    if exclude_ipt == '-fin': 
        pass
    else:
        try:
            for i in exclude_ipt.split((',')):
                exclude_lst.append(i)
            for a,b in zip(range(len(exclude_lst)),exclude_lst):
                    exclude_lst[a] = dict_columns[int(b)]
            print(f'Les colonnes {exclude_lst} seront exclues.')
        except:
            print('Une erreur est survenue, avez-vous bien écrit les index correctement ? ')

    return exclude_lst, lst_columns

#création des filtres selon la colonne
def setting_filters(data):
    lst_columns = tuple(output_df.columns)
    print('Les données qui peuvent être modifiés :')
    dict_columns = dict()
    for i in lst_columns:
        dict_columns.update({lst_columns.index(i):i})
        print(f'{lst_columns.index(i)}:{i}')

output_df = get_dataframe()
exclude_df = ['Fulfillment', 'Size Tier', 'Variation Count', 'Last Year Sales', 'Sales Year Over Year', 'Sales Trend (90 days)', 'Price Trend (90 days)', 'Best Sales Period', 'Sales to Reviews']
clean_sortdf(output_df,exclude_df)

#filtres
output_df = output_df[(output_df['Sellers'] >= 1) & (output_df['Price'] > 5 ) &
                      (output_df['Number of competing products'] <  1000) &
                      (output_df['Monthly Sales'] > 5)]

#divise la dataframe par catégorie de vente
columns = tuple(output_df.columns)
key = (i for i in output_df.Category.unique())
grouped = output_df.groupby(output_df['Category'])
group_names = tuple(grouped.indices.keys())

#Créer des tableaux séparés
for i in group_names:
    (f'category_df_{i}') = pd.DataFrame(grouped.get_group(i))
    category_df = category_df.sort_values(by=['Number of competing products','Monthly Revenue','Sellers','Monthly Sales'],ascending=[True,False,True,False])
    