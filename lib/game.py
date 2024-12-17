#!/usr/bin/env python3

from helpers import User, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from datetime import datetime
from logic import *

import time
if __name__ == "__main__":
    user_name = input("Welcome to Blackjack! \nWhat is your name? ")
    
    engine = create_engine("sqlite:///blackjack.db")
    Base.metadata.create_all(engine)
    session = sessionmaker(bind=engine)
    session = session()

    user_name_query = session.query(User).filter(User.name == user_name).first()
    if user_name_query:
        password = input(f"Good to see you again, {user_name}! Enter your password: ")
        
        query_password = session.query(User.password).filter(User.name == user_name).first()
        if query_password[0] != password:
            print("Wrong password")
            exit()
        print(f"Welcome {user_name}!")
        with open("logs.txt", "a") as file:
            file.write(f"{user_name} logged in at {datetime.now()}\n")
        
    else:
        print("Hey there! Welcome!!")
        password = input("Create a password: ")
        if isinstance(password, str) and (len(password) >= 4 and len(password) <= 20): 
                   
            user = User(
                name = user_name,
                password = password
            )

            session.add(user)
            session.commit()
            with open("logs.txt", "a") as file:
                file.write(f"{user_name} signed up at {datetime.now()}\n")
        else:
            print("Password must be between 4 and 20 characters long")
    

    with open("logs.txt", mode="a") as file:
        file.write(f"{user_name} has logged in at {time.strftime('%Y-%m-%d %H:%M:%S')}\n")

    main(user_name)