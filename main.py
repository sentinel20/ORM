# ORM (Object-Relational Mapping, Объектно-реляционное отображение) - технология программирования
# благодаря которой разработчики могут использовать язык программирования для взаимодействия с реляционной базой данных(Postgres, MySQL и др)
# вместо написания операторов SQL. Это очень сильно ускоряет разработку приложения и БД, особенно на начальных этапах разработки.


from peewee import PostgresqlDatabase

db = PostgresqlDatabase(
    'orm_db',
    user = 'emilbegaliev',
    password = '1316',
    host = 'localhost',
    port = 5432
)






