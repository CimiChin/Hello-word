import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Membuat kanvas
fig, ax = plt.subplots(figsize=(8, 6))
ax.set_xlim(0, 100)
ax.set_ylim(0, 100)

# Langit
ax.add_patch(patches.Rectangle((0, 50), 100, 50, color='skyblue'))

# Tanah
ax.add_patch(patches.Rectangle((0, 0), 100, 50, color='lightgreen'))

# Matahari
sun = patches.Circle((80, 85), 8, color='yellow')
ax.add_patch(sun)

# Gunung
ax.add_patch(patches.Polygon([[10, 50], [30, 80], [50, 50]], color='dimgray'))
ax.add_patch(patches.Polygon([[40, 50], [60, 75], [80, 50]], color='gray'))

# Sungai
ax.add_patch(patches.Polygon([[20, 0], [30, 25], [40, 20], [50, 40], [60, 30], [70, 50], [75, 0]], color='blue', alpha=0.6))

# Pohon
def gambar_pohon(x, y):
    ax.add_patch(patches.Rectangle((x, y), 1.5, 5, color='saddlebrown'))  # batang
    ax.add_patch(patches.Circle((x+0.75, y+6), 3, color='forestgreen'))   # daun

gambar_pohon(15, 50)
gambar_pohon(25, 52)
gambar_pohon(65, 48)

# Matikan axis
ax.axis('off')

# Tampilkan
plt.title("Lukisan Pemandangan Sederhana")
plt.show()
