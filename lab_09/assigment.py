import os
import pandas as pd


# Zad 1
def files_folder_count(base_path):

    folder_count = 0
    file_count = 0

    for root, _, files in os.walk(base_path):
        if root != base_path:
            folder_count +=1
        file_count += len(files)
    print(f"Liczba folderów: {folder_count}\nLiczba plików: {file_count} ")

# Zad 2
def file_stats(base_path, folder_name):
    for root, _, files in os.walk(base_path):
        if os.path.basename(root) == folder_name:
            file_size = 0
            file_count = 0

            for file in files:
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    file_count += 1
                    file_size += os.path.getsize(file_path)

            return file_count, file_size

    return 0, 0

# Zad 3
def fs_stats(base_path):
    feature_list = []

    for root, dirs, files in os.walk(base_path):
        for d in dirs:
            abs_path = os.path.join(root, d)
            rel_path = os.path.relpath(abs_path, base_path)
            feature_list.append({
                'name': d,
                'relative_path': rel_path,
                'absolute_path': abs_path,
                'is_dir': True,
                'is_file': False,
                'size_bytes': 0,
                'line_count': 0
            })

        for f in files:
            abs_path = os.path.join(root, f)
            rel_path = os.path.relpath(abs_path, base_path)
            size = os.path.getsize(abs_path)
            line_count = 0

            try:
                with open(abs_path, 'r', encoding='utf-8') as file:
                    line_count = sum(1 for _ in file)
            except:
                line_count = None

            feature_list.append({
                'name': f,
                'relative_path': rel_path,
                'absolute_path': abs_path,
                'is_dir': False,
                'is_file': True,
                'size_bytes': size,
                'line_count': line_count
            })

        return pd.DataFrame(feature_list)

def df_into_csv():
    df.to_csv("df_z_fs_stats.csv", index=False, encoding='utf-8')
    print("stworzona csvka z df'a")


# Zad 5
"""
Ponieważ lista w Pytonie przechowuje jedynie referencje do obiektów, a nie same obiekty. 
Dlatego rozmiar listy nie jest sumą rozmiarów jej elemtów. Podczas wstawiania elementów,Python dynamicznie reaokuje pamięć,
dlatego rozmiar rośnie.
https://stackoverflow.com/questions/65547276/how-allocation-of-memory-for-list-works-in-python-why-size-of-list-is-not-sam
"""
if __name__ == "__main__":
    # Zad 1
    files_folder_count(r"data/daily/pl")

    # Zad 2
    path_base = r"data/daily/pl"
    folder_name_base = "funds balanced"

    print(file_stats(path_base, folder_name_base))

    # Zad 3
    df = fs_stats(r"data/daily/pl/funds balanced")
    print(df)

    # Zad 4
    df_into_csv()
