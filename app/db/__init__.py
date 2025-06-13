from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    DeclarativeBase,
    sessionmaker
)
from sqlalchemy import create_engine


ENGINE = create_engine('sqlite:///database.db')
Session = sessionmaker(bind=ENGINE)


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)



def up():
    Base.metadata.create_all(ENGINE)


def down():
    Base.metadata.drop_all(ENGINE)



from .models import Item

# down()
up()