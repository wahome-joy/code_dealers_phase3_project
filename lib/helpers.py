import bcrypt
from sqlalchemy import String, Integer, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    password = Column(String)  # Change to store hashed password

    def set_password(self, password):
        """Hashes the password before storing it."""
        self.password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    def check_password(self, password):
        """Verifies that the entered password matches the stored hash."""
        return bcrypt.checkpw(password.encode('utf-8'), self.password.encode('utf-8'))
