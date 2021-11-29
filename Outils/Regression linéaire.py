import matplotlib.pyplot as plt
import numpy as np # Bibliothèque scientifique

plt.clf()
X = np.array([0, 0.021, 0.039, 0.063])
Y = np.array([0, 0.84, 1.45, 2.4])

plt.plot(X, Y, 'x', color='blue')  # On trace

plt.xlabel("Légende des abscisses")
plt.ylabel("Légende des ordonnées")
plt.title("Titre du graphique")

plt.grid()

# Demande à Numpy de trouver les coefficients a et b pour y = a x + b
fit = np.polyfit(X, Y, 1)


coefficient_directeur = fit[0] #a dans y = ax + b
print("coefficient directeur :", coefficient_directeur)

ordonnee_origine = fit[1] #b dans y = ax + b
print("ordonnée à l'origine:", ordonnee_origine)

print("Equation : y = " + str(coefficient_directeur) + ' x + ' + str(ordonnee_origine) )
Modelisation = coefficient_directeur * X + ordonnee_origine
plt.plot(X, Modelisation, color='red')


plt.show()
