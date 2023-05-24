import matplotlib.pyplot as plt

plt.figure(1)
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.title("Wykres 1")
plt.xlabel('X')
plt.ylabel('Y')

plt.figure(2)
plt.plot([1, 2, 3, 4], [1, 8, 27, 64])
plt.title("Wykres 2")
plt.xlabel('X')
plt.ylabel('Y')

plt.show()

