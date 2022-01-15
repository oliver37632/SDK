from sqlalchemy import Column, Integer, VARCHAR, ForeignKey, text, DATETIME

from server.model import Base


class Post(Base):
    __tablename__ = 'post'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(VARCHAR(50), nullable=True)
    content = Column(VARCHAR(2000), nullable=True)
    image = Column(VARCHAR(255), nullable=True)
    category = Column(VARCHAR(45), nullable=True)
    create_at = Column(DATETIME, nullable=False, server_default=text("CURRENT_TIMESTAMP"))
    userId = Column(VARCHAR(16), ForeignKey('user.id'))


