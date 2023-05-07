contoh_tuple = ('Januari', 'Februari', 'Maret', 'April')
print(contoh_tuple[0])

contoh_list = list(contoh_tuple)  # mengubah tuple ke list
contoh_list[0] = 'Desember'
contoh_tuple = tuple(contoh_list)  # mengubah kembali list ke tuple

print(contoh_tuple)
