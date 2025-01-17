from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from database.database import Base
from utils.generateUUID import generateUUID
import datetime

class Cart(Base):
    __tablename__ = "cart"

    id = Column(String(36), primary_key=True, index=True, default=generateUUID)
    user_id = Column(String(36), ForeignKey("users.id"), unique=False) 
    state = Column(String(20), nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now)
    updated_at = Column(DateTime, default=datetime.datetime.now)

    products = relationship(
        "Products",
        secondary="cart_product_association",
        back_populates="carts"
    )
    user = relationship("Users", back_populates="cart")
