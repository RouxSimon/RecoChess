import cv2
import os

def detect_contours(image_path):
    # Charger l'image en niveau de gris
    image = cv2.imread(image_path, 0)

    # Appliquer le filtre de Canny pour détecter les contours
    edges = cv2.Canny(image, 50, 150)

    # Trouver les contours dans l'image
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Dessiner les contours sur une copie de l'image originale (optionnel)
    image_with_contours = image.copy()
    cv2.drawContours(image_with_contours, contours, -1, (0, 255, 0), 2)

    # Afficher l'image originale et l'image avec les contours (optionnel)
    cv2.imshow("Original Image", image)
    cv2.imshow("Image with Contours", image_with_contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()  # Fermer la fenêtre après avoir affiché les contours

def main():
    images_dir = "images"
    for image_file in os.listdir(images_dir):
        image_path = os.path.join(images_dir, image_file)
        detect_contours(image_path)

if __name__ == "__main__":
    main()
