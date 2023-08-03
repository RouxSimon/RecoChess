import os
import cv2
import detect_contours
import identify_pieces
import detect_pieces

def main():
    images_dir = "images"
    for image_file in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_file)

        # Étape 2 : Détection des contours
        detect_contours.detect_contours(image_path)

        # Fermer les fenêtres d'affichage des contours
        cv2.destroyAllWindows()

        # Étape 3 : Détection des pièces
        detect_pieces.detect_pieces(image_path)

        # Étape 4 : Identification des pièces
        detected_pieces = identify_pieces.identify_pieces(image_path)
        print(f"Pièces détectées dans l'image {image_file}:")
        for piece_name, num_matches in detected_pieces.items():
            print(f"{piece_name}: {num_matches} correspondances")

if __name__ == "__main__":
    main()
