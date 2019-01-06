from sqlalchemy import Column, String, Boolean, Integer, Numeric, ForeignKey, DateTime
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel



class Order(BaseModel, Base):
    __tablename__ = 'order'

    #define columns
    user_id = Column(UUID(as_uuid=True), ForeignKey('user.id'))
    delivery_date = Column(DateTime, nullable=False)
    lines = relationship("Order_line", cascade="all,delete")
    