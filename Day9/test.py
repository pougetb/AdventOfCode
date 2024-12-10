import numpy as np

def find_sequence(array, sequence):
    array = np.array(array)  # Convertir le tableau en NumPy
    seq_len = len(sequence)
    sequence = np.array(sequence)  # Convertir la séquence en tableau NumPy
    
    # Parcourir le tableau avec des fenêtres glissantes
    for i in range(len(array) - seq_len + 1):
        # Comparer la sous-partie avec la séquence
        if np.array_equal(array[i:i+seq_len], sequence):
            return i  # Retourne le premier index trouvé
    
    return -1  # Si la séquence n'est pas trouvée

# Exemple
array = ['x', 'y', 'a', 'b', 'c', 'd', 'e', 'f']
sequence = ['a', 'b', 'c']
result = find_sequence(array, sequence)
print(result)  # Renvoie 2