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
def get_sections():
    pass

url = "https://www.imdb.com/list/ls006266261/?sort=list_order,asc&st_dt=&mode=detail&page=1"
scraper = requests.get(url)
response = scraper.text

soup = BeautifulSoup(response, 'html.parser')
info = soup.find_all("div", class_ ="lister-item-content")

store = []
for each in info:
    title = each.find("h3", class_ ="lister-item-header").find("a").text
    release_year = each.find("h3", class_ ="lister-item-header").find("span", class_ ="lister-item-year text-muted unbold").text
    runtime = each.find("span", class_ = "runtime").text
    genre = each.find("span", class_ = "genre").text
    certificate = each.find("span", class_ = "certificate").text
    directors = each.find_all("p", class_ = "text-muted text-small")[1]
    # for each_other_details in other_details: 
        # runtime = each_other_details.find("span", class_ = "runtime").text
        # genre = each_other_details.find("span", class_ = "genre").text
        # certificate = each_other_details.find("span", class_ = "certificate").text
        # directors = other_details.a.text
        # print(directors)
    # print(runtime)
    print(directors)








# SELENIUM







