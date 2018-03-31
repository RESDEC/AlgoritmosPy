from random import randint

'''Rutas de los archivos que lee el proyecto de RESDEC'''
FILE_PATH_ANDROID = "../data/android.data"
FILE_PATH_WORDPRESS = "../data/ratings_0221.csv"
FILE_PATH_WORDPRESS_CONTENT = "../data/plugin_tag_0221.csv"
FILE_PATH_ANDROID_KNN = "../data/product_features.item"
FILE_PATH_EXAMPLE_CONTENT = "../data/pubmed_oa_2013_2.csv"
FILE_PATH_WORDPRESS_CORREGIDA = "../generated/ratings_corregido.csv"


def file_path_formatted(file_name):
    return "../generated/" + file_name + "_" + str(randint(0, 1000)) + ".csv"
