# GutenbergToPDF

Simple python program to convert Gutenberg web ebooks to PDFs.

How to use:

- Go to https://www.gutenberg.org/ and search for the book you want.
- Click "Read online (web)" and copy the link

### Install
- Make python virtual environment: `python -m venv venv`
- Activate virtual environment `.\venv\Scripts\activate` (may vary depending on your operating system)
- Install requirements: `pip install -r requirements.txt`
- Run the instruction in this format: python.exe .\GutenbergToPDF.py link-here "your-title-here"
- Example: python.exe .\GutenbergToPDF.py https://www.gutenberg.org/cache/epub/26/pg26-images.html "Paradise Lost"