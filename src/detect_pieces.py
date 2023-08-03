# detect_pieces.py

import cv2
import os
import identify_pieces

def detect_pieces(image_path):
    # Charger l'image en couleur
    image = cv2.imread(image_path)

    # Convertir l'image en niveau de gris
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Appliquer un flou gaussien pour réduire le bruit
    blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

    # Appliquer la détection de cercles avec la méthode de HoughCircles
    circles = cv2.HoughCircles(
        blurred_image,
        cv2.HOUGH_GRADIENT,
        dp=1,
        minDist=20,
        param1=50,
        param2=30,
        minRadius=10,
        maxRadius=50
    )

    if circles is not None:
        circles = circles[0, :].astype(int)
        for (x, y, radius) in circles:
            # Dessiner les cercles détectés sur l'image originale (optionnel)
            cv2.circle(image, (x, y), radius, (0, 255, 0), 2)
        # Afficher l'image originale avec les cercles détectés (optionnel)
        cv2.imshow("Image with Detected Circles", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

def main():
    images_dir = "images"
    for image_file in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_file)
        detected_pieces = identify_pieces(image_path)
        print(f"Pièces détectées dans l'image {image_file}:")
        for piece_name, num_matches in detected_pieces.items():
            print(f"{piece_name}: {num_matches} correspondances")

if __name__ == "__main__":
    main()