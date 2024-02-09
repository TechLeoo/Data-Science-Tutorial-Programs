import numpy as np
import pandas as pd
import requests
import time
from bs4 import BeautifulSoup



# COURSE WORK



# # 1. Title
# # 2. Rating
# # 3. Price
# # 4. Stock availability (Boolean)
# # 5. UPC
# # 6. Quantity available 
# # 7. Category

# def get_info_internal_links(address: str, tag: str, class_: str = None):
#     scraper = requests.get(address)
#     response = scraper.text
    
#     soup = BeautifulSoup(response, "lxml")
#     info = soup.find(tag, class_ = class_)
#     return info

# def get_books_into_dataset(container_books, books):
#     store = []
#     for each_book in books:
#         book_title = each_book.h3.a["title"]
#         book_rating = each_book.p.attrs["class"][1]
#         book_price = each_book.find("p", class_ ="price_color").text.replace("Â£", '')
        
#         info_address = each_book.find("h3").a["href"].replace("../../../", "https://books.toscrape.com/catalogue/")
#         get_upc = get_info_internal_links(address = info_address, tag = "table", class_ ="table table-striped")
        
#         book_upc = get_upc.find("td").text
        
#         book_in_stock = each_book.find("p", class_ ="instock availability").text.strip()

#         get_quantity_available = get_info_internal_links(address = info_address, tag = "p", class_ ="instock availability")
#         book_quantity_available = get_quantity_available.text.strip().replace("In stock (", "").split()[0]
        
#         book_category = container_books.find("h1").text
#         book_more_info = each_book.find("h3").a["href"].replace("../../../", "https://books.toscrape.com/catalogue/")
#         store.append([book_title, 
#                       book_rating, 
#                       book_price, 
#                       book_upc, 
#                       book_in_stock,
#                       book_quantity_available,
#                       book_category, 
#                       book_more_info])
#     return store

# def iterate_through_pages():
#     # Get the dataset
#     dataset = pd.DataFrame(columns = ["Title", "Rating", "Price", "UPC", "Availability", "Quantity_Available", "Category", "More_Info"])
    
#     url = "https://books.toscrape.com/catalogue/category/books_1/index.html"
#     box = get_info_internal_links(address = url, tag = "ul", class_ = "nav nav-list").li
#     column_box = box.find_all("li")
    
#     columns = [column.text.lower().strip().replace(" ", '-') for column in column_box]
#     index = [num for num in range(2, len(columns) + 2)]
    
#     for category, index in zip(columns, index):
#         url1 = f"https://books.toscrape.com/catalogue/category/books/{category}_{index}/index.html"
        
#         container_books = get_info_internal_links(address = url1, tag = "div", class_ = "col-sm-8 col-md-9")
#         books = container_books.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")
        
#         print(f"{category}{index} -->", container_books.find("li", class_ = "current") == None)
        
        
#         if container_books.find("li", class_ = "current") == None:
#             store = get_books_into_dataset(container_books, books)
#             data = pd.DataFrame(store, columns = ["Title", "Rating","Price", "UPC", "Availability", "Quantity_Available", "Category", "More_Info"])
#             dataset = pd.concat([dataset, data])
            
#         elif container_books.find("li", class_ = "current") != None:
#             page_number = container_books.find("li", class_ = "current").text.split()[-1]
#             page_number = int(page_number)
#             for page in range(1, (page_number + 1)):
#                 url2 = f"https://books.toscrape.com/catalogue/category/books/{category}_{index}/page-{page}.html"
#                 container_books = get_info_internal_links(address = url2, tag = "div", class_ = "col-sm-8 col-md-9")
#                 books = container_books.find_all("li", class_ ="col-xs-6 col-sm-4 col-md-3 col-lg-3")
                
#                 store = get_books_into_dataset(container_books, books)
#                 data = pd.DataFrame(store, columns = ["Title", "Rating","Price", "UPC", "Availability", "Quantity_Available", "Category", "More_Info"])
#                 dataset = pd.concat([dataset, data])
                
#     return dataset

# # print(book_title)


# # NOTES
# # i) .find() can be replaced with (.then the tag you are looking for)
# # ii) to get attributes from tags, use .get or (square brackets [])

# data = iterate_through_pages()





# CLASS ASSESSMENT





# define functions
def scrape_info():
    movies_info = []
    store = []
    all_store = []
    store_directors = []
    store_stars = []
    store_votes = []
    store_gross = []
    for each in info:
        if each.find("h3", class_ ="lister-item-header").find("a") != None:
            title = each.find("h3", class_ ="lister-item-header").find("a").text
            store.append(title)
        else:
            store.append(np.nan)
        if each.find("h3", class_ ="lister-item-header").find("span", class_ ="lister-item-year text-muted unbold") != None:
            release_year = each.find("h3", class_ ="lister-item-header").find("span", class_ ="lister-item-year text-muted unbold").text.replace("(", "").replace(")", "")
            store.append(release_year)
        else:
            store.append(np.nan)
        if each.find("span", class_ = "runtime") != None:
            runtime = each.find("span", class_ = "runtime").text.replace("min", "").strip()
            store.append(runtime)
        else:
            store.append(np.nan)
        if each.find("span", class_ = "genre") != None:
            genre = each.find("span", class_ = "genre").text.strip()
            store.append(genre)
        else:
            store.append(np.nan)
        if each.find("span", class_ = "certificate") != None:
            certificate = each.find("span", class_ = "certificate").text
            store.append(certificate)
        else:
            store.append(np.nan)
        
        movies_info.append(store)
        store = []
        
        other_details = each.find_all("p", class_ = "text-muted text-small")[1:]
        for each_other_details in other_details: 
            if each_other_details.text != None:
                all_ = each_other_details.text.strip().replace("Votes", "|Votes").replace("Director", "|Director").replace("\nStars ", "|Stars").split("|")
                all_store.append(all_)
        
    for index, item in enumerate(all_store):
        if index == 0 or index % 2 == 0:
            if any(["Director" in sublist for sublist in item]):
                director = item[1].replace("Director:", "").replace("Directors:", "").strip()
                store_directors.append(director)
            else:
                store_directors.append(np.nan)
            if any(["Stars" in sublist for sublist in item]):
                stars = item[2].replace("Stars:", "").strip()
                store_stars.append(stars)
            else:
                store_stars.append(np.nan)
        else:
            if any(["Votes" in sublist for sublist in item]):
                votes = item[1].replace(",", "").replace("Votes:", "").strip()
                store_votes.append(votes)
            else:
                store_votes.append(np.nan)
            if any(["Gross" in sublist for sublist in item]):
                gross = item[2].replace("$", "").replace("Gross:", "").replace("M", "").strip()
                store_gross.append(gross)
            else:
                store_gross.append(np.nan)

def get_pages(url, parser, tag, class_ = None):
    scraper = requests.get(url)
    response = scraper.text

    soup = BeautifulSoup(response, parser)
    info = soup.find_all(tag, class_ = class_)
    return (soup, info)


url = f"https://www.imdb.com/list/ls006266261/?st_dt=&mode=detail&page=1&sort=list_order,asc"
pages = int(soup.find("span", class_="pagination-range").text.replace(",", "").split()[-1])




# scraper = requests.get(url)
# response = scraper.text

# soup = BeautifulSoup(response, 'html.parser')
# info = soup.find_all("div", class_ ="lister-item-content")



# SELENIUM







