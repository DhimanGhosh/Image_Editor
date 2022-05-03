import pytesseract


def extract_text_from_image(image_path: str):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    return pytesseract.image_to_string(rf"{image_path}")
