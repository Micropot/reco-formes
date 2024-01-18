import os
import random

def supprimer_elements_aleatoires(dossier_images, dossier_labels, nombre_elements_a_supprimer):
    # Récupérer la liste des fichiers dans les deux dossiers
    fichiers_images = os.listdir(dossier_images)
    fichiers_labels = os.listdir(dossier_labels)

    # Assurer que les listes sont triées pour avoir les mêmes éléments dans le même ordre
    fichiers_images.sort()
    fichiers_labels.sort()

    # Vérifier que les deux dossiers ont le même nombre de fichiers
    if len(fichiers_images) != len(fichiers_labels):
        print("Erreur: Les dossiers n'ont pas le même nombre de fichiers.")
        return

    # Sélectionner aléatoirement les indices des fichiers à supprimer
    indices_a_supprimer = random.sample(range(len(fichiers_images)), nombre_elements_a_supprimer)

    # Supprimer les fichiers correspondants dans les deux dossiers
    for indice in indices_a_supprimer:
        fichier_image = os.path.join(dossier_images, fichiers_images[indice])
        fichier_label = os.path.join(dossier_labels, fichiers_labels[indice])

        try:
            os.remove(fichier_image)
            os.remove(fichier_label)
            print(f"Fichiers supprimés: {fichier_image}, {fichier_label}")
        except Exception as e:
            print(f"Erreur lors de la suppression des fichiers: {e}")

# Utilisation de la fonction avec vos dossiers
dossier_images = "/Users/arthurlamard/Documents/ISEN5/reco_formes/Buildings_Instance_Segmentation/test/images"
dossier_labels = "/Users/arthurlamard/Documents/ISEN5/reco_formes/Buildings_Instance_Segmentation/test/labels"
nombre_elements_a_supprimer = 500  # Remplacez par le nombre d'éléments que vous souhaitez supprimer

supprimer_elements_aleatoires(dossier_images, dossier_labels, nombre_elements_a_supprimer)
