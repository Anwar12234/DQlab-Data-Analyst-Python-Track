SELECT
    *
FROM
    ms_item_warna
    INNER JOIN ms_item_kategori ON ms_item_warna.nama_barang = ms_item_kategori.nama_item;
