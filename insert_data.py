import peewee 

from models import Category, Product

def add_category(name):
    try:
        row = Category(name=name.lower().strip())
        row.save()
        print(f'Сохранили категорию {name.strip()}!')
    except (peewee.IntegrityError, peewee.InternalError):
        print('Такие категории уже существуют!!')

# add_category('Платья')
# add_category('Джинсы')
# add_category(' Худи ')
# add_category('Футболки')
# add_category('Обувь')


def add_product(title, price, category_name):
    try:
        category = Category.select().where(Category.name==category_name.lower().strip()).get()
        category_exists = True
    except peewee.DoesNotExist:
        category_exists = False

    if category_exists:
        row = Product(
            title = title.lower().strip(),
            price = price,
            category = category
        )
        row.save()
        print(f'Сохранили товар {title.strip()}')
    else:
        print(f'Категории {category_name} не существует!')

# add_product('ZARA Платье Лен', 15000.50, 'платья')
# add_product('DG Платье Атлас', 20000.00, 'платья')
# add_product('Supreme 15 лето', 70000.00, 'футболки')
# add_product('Aygen Super', 10000.00, 'джинсы')
# add_product('Lacoste NY', 100000.00, 'худи')
# add_product('Adidas', 8000.00, 'обувь')