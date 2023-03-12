import pandas as pd
import numpy as np
from graphes import *

if __name__ == "__main__":
    # Ouverture du fichier
    file = "./files/table 1.txt"
    f = open(file, 'r')

    graph = Graphe()  # Initialisation du graphe
    l = f.readline()  # Lecture du fichier

    while l:
        l = l.strip()  # Supprimer les espaces et retours à la ligne au début et à la fin
        c = l.split(' ')  # Découper la ligne en tableau à chaque espace

        # On vérifie si la tâche a déjà été ajoutée au graphe
        task_exists = False
        for tache in graph.taches:
            if tache.nom == c[0]:
                task_exists = True
                t = tache  # On récupère la tâche pour la modifier
                break  # On quitte la boucle
        if not task_exists:
            # La tâche n'a pas été ajoutée, donc on la crée :
            t = Tache()
            t.nom = c[0]
            # graph.taches = np.append(graph.taches, [t])  # On ajoute la tâche au graphe

        # On modifie la tâche en fonction de ce qu'on lit dans le fichier .txt :
        t.duree = c[1]

        # S'il existe des contraintes (prédécesseurs), on les ajoute :
        if len(c) > 2:
            for pre in c[2:]:  # Pour chaque contrainte...
                # On vérifie si elle a déjà été ajoutée au graphe
                pred_exists = False
                for tache in graph.taches:
                    if tache.nom == pre:
                        # Elle existe, donc on la récupère
                        predecesseur = tache
                        pred_exists = True
                        break
                if not pred_exists:  # Si elle n'a pas été ajoutée, on la crée :
                    predecesseur = Tache()
                    predecesseur.nom = pre
                    graph.taches = np.append(graph.taches, [predecesseur])  # On l'ajoute au graphe

                # On ajoute la contrainte à la liste des contraintes :
                t.predecesseurs = np.append(t.predecesseurs, [predecesseur])

        if not task_exists:
            graph.taches = np.append(graph.taches, [t])
        l = f.readline()
