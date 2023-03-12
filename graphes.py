import numpy as np


class Graphe:
    taches: np.ndarray
    taches = np.array([])


class Tache:
    duree: int
    duree = None

    nom: int
    nom = None

    predecesseurs: np.ndarray
    predecesseurs = None

    successeurs: np.ndarray
    successeurs = None
