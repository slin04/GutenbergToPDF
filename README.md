# GutenbergToPDF

Simple python program to convert Gutenberg web ebooks to PDFs.

How to use:

- Go to https://www.gutenberg.org/ and search for the book you want.
- Click "Read online (web)" and copy the link

### Windows
- If packages aren't installed:
    - pip install selenium
    - pip install markdownify
- Run the instruction in this format: python.exe .\GutenbergToPDF.py link-here "your-title-here"
- Example: python.exe .\GutenbergToPDF.py https://www.gutenberg.org/cache/epub/26/pg26-images.html "Paradise Lost"

### Linux
- Make a virtual python environment
    - python -m venv path/to/venv
- Activate environment and install packages in it
    - source /venv/bin/activate
    - pip install selenium
    - pip install markdownify
    - deactivate # at this point you don't need to have it active
- Now you can run the program following this syntax:
    - Example: /home/user/Documents/simon/Coding/PythonVirtualEnvironment/myenv/bin/python ./GutenbergToPDF.py https://www.gutenberg.org/cache/epub/8578/pg8578-images.html "The Grand Inquisitor"
    - Basically you call python from the environment and tell it to run this file with the two arguments [link] and [title]