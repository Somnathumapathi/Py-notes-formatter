# Py-Notes-Formatter

Py-Notes-Formatter is a Flask web application that allows users to format images contained within a ZIP folder into a single PDF document. It utilizes OCR (Optical Character Recognition) to automatically rotate images to the correct orientation before converting them to PDF.

## Features

- Upload a ZIP folder containing images (.png, .jpg, .jpeg).
- Automatically rotate images to the correct orientation based on text detection.
- Generate a PDF document with formatted images.
- Download the PDF document directly from the web interface.
So this helps students to easily format the notes images recieved in whatsapp into a pdf with proper orientation.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
