# get all the sales data by product type
def book_sales(file):
    return load(file)

def game_sales(file):
    return load(file)

# calculate the total sales for each year
def total_sales(book_file, game_file):
    book_sales_year = book_sales(book_file)
    game_sales_year = game_sales(game_file)

    return sum_sales(book_sales_year, game_sales_year)
