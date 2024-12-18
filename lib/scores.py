from sqlalchemy import String, Integer, Column, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base(

)
class Win_points(Base):
    __tablename__ = "points"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    score = Column(Integer)



    def __init__(self, name, score):
        self.name = name
        self.score = score

engine = create_engine("sqlite:///blackjack.db")
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
def register_win(name):
    win = session.query(Win_points).filter_by(name=name).first()
    if win is None:
        win = Win_points(
            name=name,
            score=10
        ) 
    else:
        win.score += 10
    session.add(win)
    session.commit()

def register_loss(name):
    win = session.query(Win_points).filter_by(name=name).first()
    if win is None:
        win = Win_points(
            name=name,
            score=0
        ) 
        
    else:
        win.score -= 5
    session.add(win)
    session.commit()    
def check_score(name):
    win = session.query(Win_points).filter_by(name=name).first()
    if win is None:
        return 0
    else:
        return win.score



