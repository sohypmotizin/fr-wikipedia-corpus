# -*- coding: utf-8 -*-

### @authors: Anastasiia

# ===================================
# Bases Programmation - Mini Projet
# ===================================

# =========================
# 3 - Partie introductive
# =========================

import csv
import pandas as pd

# lire le fichier .conll
wikip_small = open("wikip_small.conll")
wikip_small = csv.reader(wikip_small, delimiter="\t")

wikip_small = pd.DataFrame(wikip_small) # en faire une dataframe

### 1. Le nombre de phrases du corpus

wikip_small_id = list(wikip_small.iloc[:,0]) # faire une liste à partir de la colonne 0 contenant les id des mots

nb_phrases = 0 # compter le nombre de 1 dans cette liste car chaque phrase commence par un id 1
for i in wikip_small_id:
    if i == "1":
        nb_phrases += 1
print(nb_phrases) # il y a 300000 phrases

### 2. Le nombre de mots du corpus 

wikip_small_mot = list(wikip_small.iloc[:,1]) # faire une liste à partir de la colonne 1
nb_mots = len(wikip_small_mot)
print(nb_mots) # il y a 7535392 mots

### 3. La taille du vocabulaire

wikip_small_voc = set(wikip_small.iloc[:,1]) # créer un set à partir de la colonne 1
taille_voc = len(wikip_small_voc)
print(taille_voc) # la taille du vocabulaire est 308153

### 4. Le nombre de PoS

wikip_small_pos = set(wikip_small.iloc[:,3]) # créer un set à partir de la colonne 3

nb_pos = 0 
for i in wikip_small_pos:
    nb_pos += 1

print(nb_pos) # il y a 52 parties du discours

### 5. La longueur moyenne des phrases

longueur_phrases = nb_mots / nb_phrases # diviser le nombre de mots par le nombre de phrases
print(longueur_phrases) # la longueur moyenne des phrases est 25.11797333333333

### 6. Ecriture d'un fichier

corpus_count = open("corpus_count.txt", "w")
corpus_count.write("nombre_de_phrases=")
corpus_count.write(str(nb_phrases) + "\n")
corpus_count.write("nombre_de_mots=")
corpus_count.write(str(nb_mots) + "\n")
corpus_count.write("taille_du_vocabulaire=")
corpus_count.write(str(taille_voc) + "\n")
corpus_count.write("nombre_de_pos=")
corpus_count.write(str(nb_pos) + "\n")
corpus_count.write("longueur_mn_phrases=")
corpus_count.write(str(longueur_phrases))
corpus_count.close()

# ==============================
# 4 - Partie avancée
# ==============================
# 4.1. Fréquence du vocabulaire
# ==============================

### 1. Fonction word_freq

import csv
import pandas as pd

wikip_small = open("wikip_small.conll")
wikip_small = csv.reader(wikip_small, delimiter="\t")
wikip_small = pd.DataFrame(wikip_small)

### 1. Ecrire la fonction word_freq

def word_freq(file):
    """ 
    Retourne un dictionnaire qui contient la fréquence des mots dans le corpus 
    
    :param file: fichier au format conll
    :type file: df
    :return: dictionnaire de la fréquence des mots
    :rtype: dict

    """
    wikip_small_mot = list(file.iloc[:,1])

    freq = {}

    for mot in wikip_small_mot:
        if mot not in freq:
            freq[mot] = 1
        else:
            freq[mot] += 1
    
    return freq

### 2. Stocker la fréquence des mots dans une DataFrame

dict_mot_freq = word_freq(wikip_small) 

df_mot_freq = pd.DataFrame(dict_mot_freq, index=[0])
df_mot_freq = df_mot_freq.T

### 3. Sauvegarder la DataFrame dans un fichier .csv

df_mot_freq.to_csv("word_freq.csv")

### 4. Trier les mots par leur fréquence (ordre décroissant), sauvegarder le résultat dans un fichier txt

sorted_word_freq = open("sorted_word_freq.txt", "w")
sorted_word_freq.write(str(df_mot_freq.sort_values(by=[0], ascending=False)))
sorted_word_freq.close()

### 5. Les cinq mots les plus fréquents

print(df_mot_freq.sort_values(by=[0], ascending=False).head(5))

# 1: "," = 55224
# 2: "de" = 54091
# 3: "NaN" = 45330
# 4: "." = 44775
# 5: "la" = 26116

# =======================
# 4.2 Fréquence des PoS
# =======================

### 1. Écrire la fonction pos_freq

def pos_freq(file):
    """ 
    Retourne un dictionnaire qui contient la fréquence des PoS dans le corpus 
    
    :param file: fichier au format conll
    :type file: df
    :return: dictionnaire de la fréquence des PoS
    :rtype: dict

    """
    wikip_small_pos = list(file.iloc[:,3])

    freq = {}

    for pos in wikip_small_pos:
        if pos not in freq:
            freq[pos] = 1
        else:
            freq[pos] += 1

    return freq

dict_pos_freq = pos_freq(wikip_small)

### 2. Stocker la fréquence des PoS dans une DataFrame

df_pos_freq = pd.DataFrame(dict_pos_freq, index=[0])
df_pos_freq = df_pos_freq.T

### 3. Sauvegarder la DataFrame dans un fichier .csv

df_pos_freq.to_csv("pos_freq.csv")

### 4. Trier les PoS par leur fréquence (ordre décroissant) et sauvegarder le résultat dans un fichier .txt

sorted_pos_freq = open("sorted_pos_freq.txt", "w")
sorted_pos_freq.write(str(df_pos_freq.sort_values(by=[0], ascending=False)))
sorted_pos_freq.close()

### 5. PoS la plus fréquente

print(df_pos_freq.sort_values(by=[0], ascending=False).head(1))


# ============================
# 4.3 - Longueurs des phrases
# ============================

### 1. Écrire une fonction length_freq

def length_freq(file):
    """ 
    Retourne un dictionnaire qui contient la fréquence des longueurs des phrases dans le corpus
    
    :param file: fichier au format conll
    :type file: df
    :return: dictionnaire de la fréquence des longueurs des phrases
    :rtype: dict

    """
    wikip_small_id = list(file.iloc[:,0])

    taille_phrase = []

    for i in range(len(wikip_small_id)):
        if wikip_small_id[i] == None:
            taille_phrase.append(wikip_small_id[i-1])

    freq_taille_phrase = {}

    for i in taille_phrase:
        if i not in freq_taille_phrase:
            freq_taille_phrase[i] = 1
        else:
            freq_taille_phrase[i] += 1
  
    return freq_taille_phrase

### 2. Stocker la fréquence des longueurs des phrases obtenues dans une DataFrame

dict_taille_phrase = length_freq(wikip_small)

df_taille_phrase = pd.DataFrame(dict_taille_phrase, index=[0])
df_taille_phrase = df_taille_phrase.T

### 3. Sauvegarder la DataFrame dans un fichier .csv

df_taille_phrase.to_csv("length_freq.csv")

### 4. Calculer la moyenne, la médianne et l’écart-type des longueurs des phrases

wikip_small_id = list(wikip_small.iloc[:,0])

taille_phrase = []

for i in range(len(wikip_small_id)):
    if wikip_small_id[i] == None:
        taille_phrase.append(wikip_small_id[i-1])
            
taille_phrase_int = []
for i in taille_phrase:
    taille_phrase_int.append(int(i))

df_taille_phrase_int = pd.DataFrame(taille_phrase_int)

### 5. Sauvegarder ces résultats dans un fichier txt

x = open("length_info.txt", "w")
x.write("moyenne des longueurs des phrases : ")
x.write(str(df_taille_phrase_int.mean()[0]) + "\n")
x.write("médiane des longueurs des phrases : ")
x.write(str(df_taille_phrase_int.median()[0]) + "\n")
x.write("écart-type des longueurs des phrases : ")
x.write(str(df_taille_phrase_int.std()[0]) + "\n")
x.close()
