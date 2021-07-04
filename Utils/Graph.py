# coding: utf-8

class Graph(object):
    def __init__(self):
        self.sommets = []
        self.arcs = {}
        self.valeurs = {}

    # Ajouter un sommet au graph
    def ajouterSommet(self, valeur):
        self.sommets.append(valeur)

    # Créer un arc entre deux sommets
    def ajouterArc(self, deSommet, versSommet, valeur):
        if deSommet not in self.arcs:
            self.arcs[deSommet] = [versSommet]
        else:
            self.arcs[deSommet].append(versSommet)

        self.valeurs[(deSommet, versSommet)] = valeur

    # Liste des successeurs d'un sommet et la valeur de l'arc
    def successeurs(self, sommet):
        valeurs = []

        for arc in self.arcs[sommet]:
            valeurs.append(self.valeurs[(sommet, arc)])

        return self.arcs[sommet], valeurs

    # Liste des prédécesseur d'un sommet et la valeur de l'arc
    def predecesseur(self, sommet):
        predecesseurs = []
        valeurs = []

        for s in self.sommets:
            if sommet in self.arcs[s]:
                predecesseurs.append(s)
                valeurs.append(self.valeurs[(s, sommet)])

        return predecesseurs, valeurs