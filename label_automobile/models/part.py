from sqlalchemy import Column, String, Boolean, Integer, Numeric
from sqlalchemy.ext.hybrid import hybrid_property
from sqlalchemy.orm import relationship

from label_automobile.models.meta import Base, BaseModel



class Part(BaseModel, Base):
    __tablename__ = 'part'

    #define columns
    name = Column(String, nullable=False) #car part name
    vendor_id = Column(String, nullable=False) #vendor's own identification number because why not
    details = Column(String, nullable=True) #in reality, this would separate into several columns