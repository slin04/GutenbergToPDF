from selenium import webdriver
from selenium.webdriver.common.by import By

import time
import markdownify
import shutil
import os
import sys

def downloadVolume():
    #print("Enter link of page to download: ")
    link = sys.argv[1]
    #print("Enter export name: ")
    bookName = sys.argv[2]
    driver.get(str(link))
    driver.maximize_window()
    print("Currently downloading...")
    initializeDocument()
    writeArticles()
    finishExport(bookName)
    print(bookName + " finished downloading!")
    
def initializeDocument():
    with open('temp.txt', 'w', encoding="utf-8") as f:
        f.write(settings)

def writeArticles():
    time.sleep(0.25)

    # find main article
    article = driver.find_element(By.TAG_NAME, 'body')

    # remove title from article, so it can be added back with different header size
    to_remove = article.find_element(By.ID, 'pg-header')
    driver.execute_script("arguments[0].remove();", to_remove)

    # write article to md
    article_html = article.get_attribute("outerHTML")
    markdown_string = markdownify.markdownify(article_html, heading_style='ATX')

    with open('temp.txt', 'a', encoding="utf-8") as f:
        f.write(markdown_string)


def finishExport(bookName):
    shutil.copyfile("temp.txt", bookName + ".md")
    os.remove("temp.txt")
    command = "pandoc -V geometry:\"top=3cm, bottom=3.5cm, left=2cm, right=2cm\" \"" + bookName + ".md\" -o \"" + bookName + ".pdf\""
    os.system(command)
    os.remove(bookName + ".md")

def runProgram():
    downloadVolume()
    driver.close()

settings = "---\ndocumentclass: scrartcl\nformat: pdf\nfontsize: 13pt\n---\n"
driver = webdriver.Firefox()
driver.minimize_window()

runProgram()