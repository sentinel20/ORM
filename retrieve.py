import peewee

from models import Category, Product

def find_all_categories():
    return Category.select()

def find_all_products():
    return Product.select()

categories = find_all_categories()
# print(categories)
print('Категории в БД:')
for x in categories:
    # print(x)
    print(x.name)

choice = int(input('Введите категорию(1-платья, 2-джинсы, 3-футболки, 4-худи, 5-обувь): '))    

products = find_all_products()
for x in products:
    if x.category == categories[choice-1]:
        print(f'Title: {x.title}, price: {x.price}, category {x.category}')