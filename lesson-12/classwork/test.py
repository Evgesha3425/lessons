from sqlalchemy import create_engine, MetaData, Table, Integer, String, \
    Column, DateTime, ForeignKey, insert, Numeric, CheckConstraint
from datetime import datetime

DB_USER = "evgeniy"
DB_PASSWORD = "evgeniy"
DB_NAME = "evgeniy"


metadata = MetaData()


client = Table('client', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(100), nullable=False),
    Column('email', String(200), nullable=False),
)


product = Table('product', metadata,
    Column('id', Integer(), primary_key=True),
    Column('name', String(200), nullable=False),
    Column('price', Numeric(10, 2), nullable=False),
)


purchases = Table('purchases', metadata,
    Column('id', Integer(), primary_key=True),
    Column('price', Numeric(10, 2), nullable=False),
    Column('time', DateTime(), default=datetime.now),
    Column('client_id', ForeignKey('client.id')),
    Column('product_id', ForeignKey('product.id')),
)

if __name__ == "__main__":
    engine = create_engine(
        f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )

    metadata.create_all(engine)
    conn = engine.connect()

    ins_product = insert(product)
    r = conn.execute(ins_product, [
        {
            "name": "monitor",
            "price": "40.5"
        },
        {
            "name": "watch",
            "price": "70.3"
        },
    ])


    # Создание нового пользователя
    ins_client = insert(client)
    r = conn.execute(ins_client, [
        {
            "name": "Artem",
            "email": "weibak@gmail.com"
        },
        {
            "name": "Elena",
            "email": "asamoilenka@gmail.com"
        },
    ])


