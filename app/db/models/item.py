from sqlalchemy.orm import Mapped

from .. import Base


class Item(Base):
    __tablename__ = 'items'

    name: Mapped[str]
    price: Mapped[int]
    amount: Mapped[int]