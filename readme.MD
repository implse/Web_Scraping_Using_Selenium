# Web Scraping Using Selenium

![Book Shelves](./images/alfons-morales-YLSwjSy7stw-unsplash.jpg)

## Introduction

In this short project, we are going to fetch the first 100 French literature books from the site `www.goodreads.com`. The goal of this project is to scrape data using `selenium` and export the collected data in `CSV` format.

- Create a virtual environmrent
- Install `Selenium` using `PIP`


## Drivers

- Chrome: `ChromeDriver`
- Firefox: `geckodriver`

## Data Structure

- A class with properties and methods.
- A Python list to store the collected books.

### Book Properties
- Author name
- Book title
- Book description
- Book illustration (cover)

(Extra parameters)
+ Published date
+ Original Title

```
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.description = None
        self.illustration = None

    def __str__(self):
        return f"{title} by {author}"
```

### A collection of Book Objects
```
    French_Literature_Books = [

        Book(
            author_name: "Jules Verne"
            book_title: "Twenty Thousand Leagues Under the Sea"
            book_description: "When an unidentified “monster” threatens ..."
            book_illustration: link to illustration (local storage)
        ),

        ...

    ]
```

## Phase 1 : Selenium

- Step 1: Init web driver and get the url
- Step 2a: Locate the Signin button
- Step 2b: Window switch
- Step 3: Find email and password input and signin button
- Switch to French Literature page
- Step 5 : Fetch all titles and authors



## Phase 2 : Export data to `csv`

Write the collected data to a CSV file using `utf-8` as encoding.






