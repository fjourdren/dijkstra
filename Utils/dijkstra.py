# coding: utf-8

from __future__ import print_function

# Fonction pour générer la matrice de dijkstra à partir d'un sommet de départ vers tous les autres sommets
def dijkstra(graph, sommetDep):
    sommets = graph.sommets[:] # On COPIE l'ensemble des sommets du graphe pour avoir une liste dans laquelle on pourra retirer les sommets déjà analysés

    chemin = {}
    visites = {sommetDep: 0} # On ajoute le sommet de départ avec une distance de 0

    while sommets: # Tant qu'il reste des sommets non explorés

        # On cherche le successeur suivant à calculer en cherchant celui qui a l'arc avec la valeur minimale
        min_sommet = None

        for sommet in sommets: # boucle dans les sommets non traités
            if sommet in visites:
                if min_sommet is None or visites[sommet] < visites[min_sommet]:
                    min_sommet = sommet

        # Si il n'y a plus de successeur, on force l'arret de la boucle.
        if min_sommet is None:
            break

        
        # On retire le prochain sommet à être calculer et on récupère la valeur de l'arc
        sommets.remove(min_sommet)
        current_poid = visites[min_sommet]


        # On analyse les arcs suivants pour calculer les valeurs à mettre dans la matrice de dijkstra
        if min_sommet not in graph.arcs:
            break

        for arc in graph.arcs[min_sommet]:

            # Calcul de la valeur de ce chemin en prenant la valeur précédente et en y additionnant la valeur de l'arc
            try:
                poid = current_poid + graph.valeurs[(min_sommet, arc)]
            except:
                continue


            # On sauvegarde la valeur du chemin et le sommet suivant si le chemin est considéré comme meilleur
            if arc not in visites or poid < visites[arc]:
                visites[arc] = poid # On garde en mémoire la valeur du chemin quand on arrive à cet arc
                chemin[arc] = min_sommet # On indique que pour atteindre arc il faut se diriger vers min_sommet


    return visites, chemin


def calculCheminCourt(graph, sommetDep, sommetArr):

    # Valeurs par défaut, valeur du chemin = inifini et chemin = []. Si ces valeurs ne changent pas au cours de la fonction, cela signifie qu'il n'y a pas de chemin possible
    sortieCheminValeur = float('inf')
    sortieChemin = []

    if sommetDep == sommetArr: # Si le noeud de départ et d'arrivé sont les mêmes, alors on est arrivé
        sortieCheminValeur = 0
        sortieChemin = [sommetDep]
    else:
        visites, chemins = dijkstra(graph, sommetDep) # Calcul de la matrice de dijkstra qui permet de connaitre la façon la plus courte d'arriver à l'arrivé et connaitre la longueur du chemin

        # Si le sommet d'arrivé est dans la matrice de dijkstra, on calcul la longueur du chemin et le trajet
        if sommetArr in chemins:
            sortieChemin = []
            sommetEnCalcul = chemins[sommetArr]

            sortieCheminValeur = visites[sommetArr] # Valeur du chemin minimum du sommet de départ au sommet d'arrivé

            # On met le sommet de départ dans le tableau du chemin
            sortieChemin.insert(0, sommetDep)

            # On parcours la matrice de dijkstra jusqu'au sommet d'arrivé et on ajoute les sommets au fûr et à mesure au tableau du chemin
            while sommetEnCalcul != sommetDep:
                sortieChemin.insert(1, sommetEnCalcul)
                sommetEnCalcul = chemins[sommetEnCalcul]

            # Ajout du sommet d'arrivé au tableau du chemin
            sortieChemin.append(sommetArr)

    return sortieCheminValeur, sortieChemin


# Affichage d'un chemin pour le debug
def afficherChemin(valeurChemin, chemin):
    if valeurChemin == float('inf'):
        print("Aucun chemin possible.")
    elif len(chemin) == 1 and valeurChemin == 0:
        print("Le point de départ est aussi le point d'arriver.")
    else:
        print("Chemin de valeur total: " + str(valeurChemin))
        print("Chemin: ", end="")
        indexAAfficher = 0
        while indexAAfficher != len(chemin):
            if indexAAfficher != len(chemin) - 1:
                print(chemin[indexAAfficher] + " => ", end="")
            else:
                print(chemin[indexAAfficher])
            indexAAfficher += 1