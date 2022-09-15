#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from book import Book
import csv

French_Literature_Books = list()

# Email and Password to fill in
EMAIL = None
PASSWORD = None

# Step 1: Init web driver and get the url
browser = webdriver.Firefox()
browser.get("https://www.goodreads.com/user/sign_in")
print("Step 1: Init web driver and get the url ... Done")

# Step 2a: Locate the Signin button
signin = browser.find_element(By.CLASS_NAME, "third_party_sign_in")
signin_button = signin.find_element(By.CLASS_NAME, "authPortalSignInButton")
signin_button.click()
print("Step 2a: Locate the Signin button ... Done")

# Step 2b: Window switch
window_after = browser.window_handles[0]
browser.switch_to.window(window_after)
print("Step 2b: Switching to Signin page ... Done")

# Step 3: Find email and password input and signin button
email_input = browser.find_element(By.ID, "ap_email").send_keys(EMAIL)
password_input = browser.find_element(By.ID, "ap_password").send_keys(PASSWORD)
submit_signin = browser.find_element(By.ID, "signInSubmit")
submit_signin.click()
print("Step 3: Fill in the Signin form with credentials ... Done")

# Step 4: Switching to French Literature
browser.get("https://www.goodreads.com/list/show/67.Best_French_Literature")
print("Step 4: Switching to French Literature page ... Done")

# Step 5: Fetch all titles and authors
books_title = browser.find_elements(By.CLASS_NAME, "bookTitle")
books_author = browser.find_elements(By.CLASS_NAME, "authorName")
print("Step 5: Fetching book title and author name ... Done")

# Step 5b: Cleaning title data
books_title = [title for title in books_title[::2]]

# Step 6: Store each book in a list
for title, author in zip(books_title, books_author):
    new_book = Book(title.text, author.text)
    # print(new_book)
    French_Literature_Books.append(new_book)

# Step 7: Export data to CSV 
with open("french_literature.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "author", "description", "illustration"]
    writer = csv.writer(csvfile, delimiter=",", quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["title", "author", "description", "illustration"])

    for book in French_Literature_Books:
        title = book.title
        author = book.author
        description = book.description
        illustration = book.illustration
        writer.writerow([title, author, description, illustration])
print("Final Step: Writing the books to CSV ... Done")


