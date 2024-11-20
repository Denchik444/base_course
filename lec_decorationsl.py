import matplotlib.pyplot as plt

x = [3, 8, 5]
y = [7, 4, 9]

plt.plot(x, y, color='g', label='Graf 1', marker='>', ms=5)
plt.plot(y, x, color='r', label='Graf 2', marker='o', ms=3) 

# --- украшательства ---

plt.xlabel('Coord: x') # подпись на оси Х
plt.ylabel('Coord: y') # подпись на оси У
plt.legend() # Вызов 'легенды'
plt.title('Base') # Общая подпись графика
plt.grid() # сетка
# plt.clear() # забыть всё

plt.savefig('fig_2.png') 