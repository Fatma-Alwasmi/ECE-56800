birthday = {"Albert Einstein": "3/14/1879",
            "Benjamin Franklin": "1/17/1706",
            "Ada Lovelace": "12/10/1815",
            "Charles Babbage": "12/26/1791",
            "Grace Hopper": "12/9/1906"}

name = input("Welcome to the birthdays of:\n Albert Einstein\n Benjamin Franklin\n Ada lovelace\n Charles Babbagr\n Grace Hopper\n whose birthay would you like to lookup? \n")

print(name + "'s birthday is " + birthday[name])
