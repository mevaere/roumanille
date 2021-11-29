# matplotlib est la bibliothèque qui permet de tracer les graphiques
import matplotlib.pyplot as plt

plt.clf()

X = [0, 0.021, 0.039, 0.063]  # Valeur des x
Y = [0, 0.54, 1.08, 1.62]  # Valeur des y

plt.plot(X, Y, 'x', color='blue')  # On trace

plt.xlabel("Légende des abscisses")
plt.ylabel("Légende des ordonnées")
plt.title("Titre du graphique")

plt.grid()  # Si on veut afficher une grille

plt.show()  # Afficher l'image
