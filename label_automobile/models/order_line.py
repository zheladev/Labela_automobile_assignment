from sqlalchemy import Column, String, Boolean, Integer, Numeric, ForeignKey
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.dialects.postgresql import UUID

from label_automobile.models.meta import Base, BaseModel


#probably should be defined just as a many-to-many relationship between Order and Part
class Order_line(BaseModel, Base):
    __tablename__ = 'order_line'

    #define columns
    order_id = Column(UUID(as_uuid=True), ForeignKey('order.id'))
    part_id = Column(UUID(as_uuid=True), ForeignKey('part.id'))
    quantity = Column(Integer, nullable=False)
    
    