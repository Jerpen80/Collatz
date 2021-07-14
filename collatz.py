# To run this, you need to install matplotlib
# Do this by running: 'pip install matplotlib' in your shell

# The Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows:
# Start with any positive integer n. Then each term is obtained from the previous term as follows: 
# If the previous term is even, the next term is one half of the previous term. 
# If the previous term is odd, the next term is 3 times the previous term plus 1. 
# The conjecture is that no matter what value of n, the sequence will always reach 1

from matplotlib import pyplot as plt

n = int(input("\nGive an integer number above 0: "))

step = 0

x = [step]
y = [n]

while n != 1:
    if n % 2 == 0:
        n = n / 2
        print(int(n))
        step += 1
        x.append(step)
        y.append(n)

    else:
        n = 3 * n + 1
        print(int(n))
        step += 1
        x.append(step)
        y.append(n)

plt.figure(figsize=(14,10))
plt.scatter(x, y)
plt.plot(x, y)

plt.xlabel('step count')
plt.ylabel('term')

plt.title('Collatz conjecture: '+str(y[0])+' reached 1 in '+str(step)+' steps')

plt.show()
