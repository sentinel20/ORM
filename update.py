from itertools import product
from models import Product


# products = Product.select()
# print(list(products))

# p = Product.get(product_id=1)
# print(dir(p))

# query = Product.update(price=1).where(Product.product_id==1)
# query.execute()
# print(Product.get(product_id=1).price)

# query = Product.update(price=(Product.price / 2))
# query.execute()
# for i in Product.select():
#     print(f'{i}\t{i.title}\t{i.price}')