import unittest

import Utils

class Dijkstra(unittest.TestCase):

    def test_graph1(self):
        print("===== test_graph1 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 10)
        G.ajouterArc('A', 'C', 20)
        G.ajouterArc('B', 'D', 30)
        G.ajouterArc('C', 'D', 30)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'D')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (40, ['A', 'B', 'D']))



    def test_graph2(self):
        print("===== test_graph2 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 10)
        G.ajouterArc('B', 'C', 10)
        G.ajouterArc('C', 'D', 30)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'D')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (50, ['A', 'B', 'C', 'D']))



    def test_graph3(self):
        print("===== test_graph3 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D', 'E']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 10)
        G.ajouterArc('B', 'C', 20)
        G.ajouterArc('C', 'D', 20)
        G.ajouterArc('B', 'E', 2)
        G.ajouterArc('E', 'C', 1)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'D')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (33, ['A', 'B', 'E', 'C', 'D']))



    def test_graph4(self):
        print("===== test_graph4 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 20)
        G.ajouterArc('B', 'C', 15)
        G.ajouterArc('C', 'A', 10)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'A')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (0, ['A']))



    def test_graph5(self):
        print("===== test_graph5 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 10)
        G.ajouterArc('C', 'B', 20)
        G.ajouterArc('D', 'B', 30)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'D')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (float('inf'), []))



    def test_graph6(self):
        print("===== test_graph6 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'C', 20)
        G.ajouterArc('D', 'C', 10)
        G.ajouterArc('B', 'D', 20)
        G.ajouterArc('B', 'A', 30)
        G.ajouterArc('F', 'B', 10)
        G.ajouterArc('E', 'B', 10)
        G.ajouterArc('G', 'F', 20)
        G.ajouterArc('G', 'E', 10)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'G', 'C')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (50, ['G', 'E', 'B', 'D', 'C']))



    def test_graph7(self):
        print("===== test_graph7 =====")
        G = Utils.Graph()

        for sommet in ['A', 'B', 'C', 'D']:
            G.ajouterSommet(sommet)

        G.ajouterArc('A', 'B', 20)
        G.ajouterArc('A', 'A', 60)
        G.ajouterArc('B', 'C', 10)
        G.ajouterArc('C', 'D', 15)

        valeurChemin, chemin = Utils.calculCheminCourt(G, 'A', 'A')
        Utils.afficherChemin(valeurChemin, chemin)

        self.assertEqual((valeurChemin, chemin), (0, ['A']))


unittest.main()