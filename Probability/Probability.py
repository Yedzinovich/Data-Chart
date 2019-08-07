import random
import math
from matplotlib import pyplot as plt

def random_kid():
  return random.choice(["boy", "girl"])

both_girls = 0
older_girl = 0
either_girl = 0

random.seed(0)

for _ in range(10000):
  younger = random_kid()
  older = random_kid()
  if older == "girl":
    older_girl +=1
  if  older == "girl" and younger == "girl":
    both_girls +=1
  if older == "girl" or younger == "girl":
    either_girl += 1

print("P(both | older): ", both_girls / older_girl)      
print("P(both | either): ", both_girls / either_girl)

def unform_pdf(x):
  return 1 if x >= 0 and x < 1 else 0

def uniform_cdf(x):
  if x < 0: 
    return 0
  elif x < 1:
    return x
  else:
    return 1

def normal_pdf(x, mu = 0, sigma = 1):
  sqrt_two_pi = math.sqrt(2 * math.pi)
  return (math.exp(-(x-mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))

xs = [x / 10.0 for x in range(-50, 50)]
plt.plot(xs,[normal_pdf(x,sigma=1) for x in xs],'-',label='mu=0,sigma=1')
plt.plot(xs,[normal_pdf(x,sigma=2) for x in xs],'--',label='mu=0,sigma=2')
plt.plot(xs,[normal_pdf(x,sigma=0.5) for x in xs],':',label='mu=0,sigma=0.5')
plt.plot(xs,[normal_pdf(x,mu=-1) for x in xs],'-.',label='mu=-1,sigma=1')
plt.legend()
plt.title("Various Normal pdfs")
plt.show()

