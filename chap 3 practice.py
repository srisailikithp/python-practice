# Q1.write a python program to display a user enterd name followed by good Afternoon using input() function .
a = input("enter your name :")
print(f"good Afternoon {a}")

# Q2.write a program to fill in a letter template give below with name and date . 
letter = '''Dear <|name|> ,
you are selected!
<|Date|>
'''
print(letter.replace("<|name|>" , "sslp") . replace("<|Date|>" , "23-feb-2030" )) 

# Q3.write a program to dettect double space in a string .
sslp = "is a  macho  "
print(sslp.find("  "))

# Q4.write a program to format the following letter using escape sequence characters .letter = "E What myan ! , life full jolly becomingg!"
letter = "E What myan ! , \n\tlife fulll \n jolly becomingg!"
print(letter)

