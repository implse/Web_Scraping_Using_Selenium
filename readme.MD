# Web Scraping Using Selenium

- Create a virtual environmrent
- Install `Selenium` using `PIP`


## Drivers

- Chrome: ChromeDriver
- Firefox: geckodriver

## Data Structure

### Book object 
- Author name
- Book title
- Book description
- Book illustration

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

### A collection of Book objects
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






