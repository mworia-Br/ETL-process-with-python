from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, Float

from sqlalchemy.orm import Session

engine = create_engine("postgresql+psycopg2://postgres:bigsecret@localhost:5432/campdata-prod")
session = Session(engine)

Base = declarative_base()

# summary on classes
class Parent():
    parent_attr = 'I am the parent'

class Child(Parent):
    child_attr = 'I am the child'

child = Child()
print(child.parent_attr, "and", child.child_attr)

# continue
class TableName(Base):
    __tablename__ = 'table_name'
    id = Column(Integer, primary_key=True)
    column_name = Column(String(255))
    another_column = Column(Integer)

    def __repr__(self):
        return "<TableName(id='%s', column_name='%s', another_column='%s')>" % (
            self.id, self.column_name, self.another_column)

#example
class Movies(Base):
    __tablename__ = 'movies'
    id = Column(Integer, primary_key=True)
    title = Column(String(55))
    description = Column(String(255))
    year = Column(Integer)
    rating = Column(Float)
    votes = Column(Integer)

    def __repr__(self):
        return "<Movies(id='%s', title='%s', year='%s', rating='%s', votes='%s')>" % (
            self.id, self.title, self.year, self.rating, self.votes)