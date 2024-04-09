# Notes Formatter

This Python script rotates images based on their detected orientation using Tesseract OCR and converts them into a PDF file. So this helps students to easily format the notes images recieved in whatsapp into a pdf with proper orientation.

## Installation

1. Clone the repository
2. Install the required Python libraries using pip

## Usage

1. Place the images you want to rotate and convert into pdf in a single directory.
2. Run the Python script, specifying the directory containing the images as the argument.

## Dependencies

- Tesseract OCR (`pytesseract`): For detecting text orientation.
- Pillow (`PIL`): For image manipulation.
- FPDF (`fpdf`): For creating PDF files.

## Notes

- The script will generate a PDF file named `notes.pdf` in the same directory as the input images.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
