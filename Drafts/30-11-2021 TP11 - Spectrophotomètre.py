import matplotlib.pyplot as plt
import numpy as np  # Bibliothèque scientifique

plt.clf()
plt.grid()
X = np.array([0, 0.021, 0.039, 0.063])
Y = np.array([0, 0.84, 1.45, 2.4])

valeur_absorbance = 0.045

plt.plot(X, Y, 'x', color='blue', markersize=10, markeredgewidth=2)  # On trace

plt.xlabel("Concentration en masse $mg.L^{-1}$")
plt.ylabel("Absorbance")
plt.title("Dosage du bleu brillant dans un sirop de menthe")

fit = np.polyfit(X, Y, 1)

print("Equation : y = " + str(fit[0]) + ' x + ' + str(fit[1]))
f = lambda x: fit[0] * x + fit[1]
Y_mod = np.array(list(map(f, X)))

plt.plot(X, Y_mod, color='red', linestyle='--')
# plt.xticks(list(plt.xticks()[0]) + [0.035])

ax = plt.gca()
percent = 0.05
ax.set_xlim([X.min() - percent * X.max(), X.max() + percent * X.max()])
ax.set_ylim([Y.min() - percent * Y.max(), Y.max() + percent * Y.max()])

xmin, xmax, ymin, ymax = plt.axis()

plt.vlines(valeur_absorbance, ymin, f(valeur_absorbance))
plt.hlines(f(valeur_absorbance), xmin, valeur_absorbance)

plt.scatter(valeur_absorbance, f(valeur_absorbance), color='black')
plt.annotate(f"({valeur_absorbance:.3f} ; {f(valeur_absorbance):.3f})", (valeur_absorbance+percent * X.max(), f(valeur_absorbance)-percent * Y.max()),fontsize=15, weight='bold')

plt.show()
