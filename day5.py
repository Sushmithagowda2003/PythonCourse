#creating a strong password
import random
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers=['0','1','2','3','4','5','6','7','8','9']
symbols=['!','#','@','$','%','^','&','*','(',')','+']

#giving inputs
nr_letters=int(input("How many letters would u like in ur password:"))
nr_symbols=int(input("how many symbols would u like to have in ur password:"))
nr_numbers=int(input("how many numbers:"))

#generating in sequence which is easy
password=" "
for char in range (1,nr_letters+1):
    password+=random.choice(letters)
for char in range (1,nr_numbers+1):
    password+=random.choice(numbers)
for char in range (1,nr_symbols+1):
    password+=random.choice(symbols)
print(f"Your password is {password}")

#hard level is generating randomly after one letter one number then again letter then symbol etc
password_list=[]
for char in range (1,nr_letters+1):
    password_list+=random.choice(letters)
for char in range (1,nr_numbers+1):
    password_list+=random.choice(numbers)
for char in range (1,nr_symbols+1):
    password_list+=random.choice(symbols)
print(password_list)
random.shuffle(password_list)
print(f"your reoredred list is:{password_list}")
password_2=" "
for char in password_list:
    password_2+=char
print(f"Your password is:{password_2}")

