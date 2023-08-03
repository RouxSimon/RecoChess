# identify_pieces.py

import cv2
import os

def identify_pieces(image_path):
    # Charger l'image en niveau de gris
    image = cv2.imread(image_path, 0)

    # Appliquer la détection des coins avec la méthode ORB
    orb = cv2.ORB_create()
    key_points, descriptors = orb.detectAndCompute(image, None)

    # Charger les descripteurs de pièces connues (à remplacer avec vos propres descripteurs)
    known_descriptors = {
        "king": known_descriptor_for_king,
        "queen": known_descriptor_for_queen,
        # Ajoutez les descripteurs pour les autres pièces connues ici
    }

    # Initialiser le dictionnaire pour stocker les correspondances détectées
    detected_pieces = {}

    # Comparer les descripteurs avec les descripteurs de pièces connues
    for piece_name, piece_descriptor in known_descriptors.items():
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = bf.match(piece_descriptor, descriptors)
        matches = sorted(matches, key=lambda x: x.distance)
        good_matches = matches[:10]  # Sélectionner les 10 meilleures correspondances

        # Si le nombre de bonnes correspondances est suffisant, considérez que la pièce est identifiée
        if len(good_matches) >= 5:
            detected_pieces[piece_name] = len(good_matches)

    return detected_pieces

if __name__ == "__main__":
    images_dir = "images"
    for image_file in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_file)
        detected_pieces = identify_pieces(image_path)
        print(f"Pièces détectées dans l'image {image_file}:")
        for piece_name, num_matches in detected_pieces.items():
            print(f"{piece_name}: {num_matches} correspondances")
