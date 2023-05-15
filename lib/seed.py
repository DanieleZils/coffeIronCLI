#!/usr/bin/env python3
from datetime import datetime
# from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from models import *

if __name__ == '__main__':
    engine = create_engine('sqlite:///coffeeiron.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    
    d_1 = Drinks(name="Big Mama Latte", description="espresso with steamed milk & caramel + chocolate + marshmallow", price=8)
    d_2 = Drinks(name="Gentle Christmas Latte", description="espresso with steamed milk & lavendar + mint", price=7) 
    d_3 = Drinks(name="Matcha Latte", description="steamed milk & matcha", price=7)
    d_4 = Drinks(name="Cappuccino", description="espresso with foam", price=6)
    d_5 = Drinks(name="Americano", description="espresso with hot water", price=5)
    d_6 = Drinks(name="Spicy Pumpkin Latte", description="espresso with steamed milk & cayenne + pumpkin", price=7)
    d_7 = Drinks(name="Latte", description="espresso with steamed milk", price=6)
    d_8 = Drinks(name="Brewed Coffee", description="our daily brew", price=3)
    d_9 = Drinks(name="Mocha", description="espresso with steamed milk & chocolate", price=6)
    d_10 = Drinks(name="Summer Breeze", description="espresso with steamed milk & coconut + vanilla", price=6)



    # a_1 = Add_Drinks(drink_name = 1, size = "M", hot = True)

    # o_1 = Orders(total_price = 10)


    # session.query().delete()
    # session.add_all([d_8, d_7, d_4, d_5, d_9, d_3, d_10, d_6, d_2, d_1])
    session.commit()
    session.close()