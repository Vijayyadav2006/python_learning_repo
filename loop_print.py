import time 
import concurrent.futures 
import random


product = ["lemon","tea","futta","gannna","channna"]

def producs(i):
    wait=random.randint(1,10)
    time.sleep(wait)
    print(f"i am {i} ordered at {wait}")

for i in product:
    producs(i)
