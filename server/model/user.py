from sqlalchemy import Column, VARCHAR, Integer
from sqlalchemy.orm import relationship

from server.model import Base


class User(Base):
    __tablename__ = 'user'

    id = Column(VARCHAR(16), primary_key=True)
    name = Column(VARCHAR(4), nullable=True)
    school = Column(VARCHAR(16), nullable=True)
    password = Column(VARCHAR(60), nullable=True)
    post = relationship("Post", cascade="all,delete", backref="user")

