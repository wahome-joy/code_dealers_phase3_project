#!/usr/bin/env python3
from helpers import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import time
from logic import *
import bcrypt
import getpass  # for password masking

def save_user_name(user_name):
    with open("current_user.txt", "w") as file:
        file.write(user_name)

if __name__ == "__main__":
    
    user_name = input("Welcome to Blackjack! \nWhat is your name? ")
    current_user = user_name
    save_user_name(user_name)
    
    engine = create_engine("sqlite:///blackjack.db")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    user_name_query = session.query(User).filter(User.name == user_name).first()
    
    if user_name_query:
        # Prompt for password using getpass (it will be masked)
        password = getpass.getpass(f"Good to see you again, {user_name}! Enter your password: ")
        
        # Check if the password is correct
        if not bcrypt.checkpw(password.encode('utf-8'), user_name_query.password.encode('utf-8')):
            print("Wrong password")
            exit()
        print(f"Welcome {user_name}!")
        
    else:
        print("Hey there! Welcome!!")
        
        # Prompt for password to create a new user (password will be masked)
        password = getpass.getpass("Create a password: ")
        
        # Check if the password is valid
        if isinstance(password, str) and (len(password) >= 4 and len(password) <= 20):
            # Hash the password before storing it
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
            
            user = User(name=user_name, password=hashed_password)
            session.add(user)
            session.commit()
            
            with open("logs.txt", "a") as file:
                file.write(f"{user_name} signed up at {datetime.now()}\n")
        else:
            print("Password must be between 4 and 20 characters long")
    

    with open("logs.txt", mode="a") as file:
        file.write(f"{user_name} has logged in at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    main(user_name)
