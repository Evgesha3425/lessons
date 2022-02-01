from sqlalchemy import create_engine, Integer, String, Column, ForeignKey, DateTime
from sqlalchemy_utils import create_database, database_exists
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime

# Настройки доступа к БД
DB_USER = "evgeniy"
DB_PASSWORD = "evgeniy"
DB_NAME = "evgeniy"
DB_ECHO = True

# Базовый класс для работы с БД
Base = declarative_base()


class Client(Base):
    __tablename__ = "client"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)


class Product(Base):
    __tablename__ = "product"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    price = Column(Integer)


class Purchases(Base):
    __tablename__ = "purchases"
    id = Column(Integer, primary_key=True)
    count = Column(String)
    time = Column(DateTime, default=datetime.utcnow)

    client_id = Column(Integer, ForeignKey("client.id"), nullable=False)
    client = relationship("Client", backref="purchases")

    product_id = Column(Integer, ForeignKey("product.id"), nullable=False)
    product = relationship("Product", backref="purchases")


if __name__ == "__main__":
    # Создание подключения к БД
    engine = create_engine(
       f"postgresql://{DB_USER}:{DB_PASSWORD}@localhost/{DB_NAME}", echo=True,
    )
    # Проверка существования БД
    if not database_exists(engine.url):
        # Создание БД
        create_database(engine.url)

    # Создание таблиц в БД для всех классов/моделей
    Base.metadata.create_all(engine)

    # Создание новой сессии для добавления/удаления записей
    Session = sessionmaker(bind=engine)
    session = Session()

    # Создание нового пользователя
    client = Client(name="Alexandr", email="manti.by@gmail.com")
    session.add(client)

    # Создание нового товара
    product = Product(name="book", price=80)
    #product = Product(name="milk", price=10)
    session.add(product)

    # Отправка данных в БД
    session.commit()

    # Создание новой покупки
    product = Purchases(client_id=client.id, product_id=product.id, count=1)
    session.add(product)

    # Отправка данных в БД
    session.commit()





