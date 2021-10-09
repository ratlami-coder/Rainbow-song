import random

def sumkrandom(k):
  sum=0
  for i in range(k):
    sum+=random.random()
  return sum

print(sumkrandom(int(input())))
