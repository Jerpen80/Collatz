# To run this, you need to install matplotlib
# Do this by running: 'pip install matplotlib' in your shell

print("\nWelcome to my app to display Collatz Conjecture sequences in graphs")

print("""\nThe Collatz conjecture is a conjecture in mathematics that concerns sequences defined as follows:
Start with any positive integer n. 
Then each term is obtained from the previous term as follows: 
If the previous term is even, the next term is one half of the previous term. 
If the previous term is odd, the next term is 3 times the previous term plus 1. 
The conjecture is that no matter what value of n, the sequence will always reach 1\n""")

from matplotlib import pyplot as plt

# Running formula on input, stops when n is 1 adding iterations in list for graph
def seq(n):
    # Counting the number of steps to reach 1
    step = 0
    
    # Creating lists for the graph
    x = [step]
    y = [n]
    
    while n != 1:
        if n % 2 == 0:
            n /= 2
            print(int(n))
            step += 1
            x.append(int(step))
            y.append(int(n))

        else:
            n = 3 * n + 1
            print(int(n))
            step += 1
            x.append(int(step))
            y.append(int(n))
    return step, x, y

menu = 0

print("""Enter 1 to do the sequence on 1 number and see a graph of every iteration in the sequence.\n
Enter 2 to do a range of numbers in 1 go and see the number of terms in a graph : """)

while menu not in ['1','2']:
    menu = input("\nType 1 or 2 and press Enter: ")

if menu == '1':
    # Taking starting number from input
    n = int(input("\nGive an integer number above 0: "))
    step, x, y = seq(n)
    # Size of graph
    plt.figure(figsize=(14,10))

    # Drawing points and lines
    plt.scatter(x, y)
    plt.plot(x, y)

    # To make 0 on x and y axes
    #plt.xlim(xmin = 0)
    plt.ylim(ymin = 1)

    # Naming x and y axes
    plt.xlabel('step count')
    plt.ylabel('term')

    # Naming title of graph
    plt.title('Collatz conjecture: '+str(y[0])+' reached 1 in '+str(step)+' steps')

    # Launching graph window
    plt.show()

elif menu == '2':
    start = 0
    end = 0

    while start < 1:
        try:
            start = int(input("Give first number of the range (has to be an integer above 0): "))
            while start < 1:
                print("number above 0 only!")
                start = int(input("Give first number of the range (has to be an integer above 0): "))
        except ValueError:
            print("Numbers only!")
    
    while end <= start:
        try:
            end = int(input("Give last number of the range "))
            while end <= start:
                print("number has to be above your starting number")
                end = int(input("Give last number of the range"))
        except ValueError:
            print("Numbers only")
    
    steps = []
    iterations = []
    for i in range(start,end):
        step, x, y = seq(i)
        iterations.append(i)
        steps.append(x[-1])

    
    # Size of graph
    plt.figure(figsize=(14,10))

    # Drawing points and lines
    plt.scatter(iterations, steps)
    plt.plot(iterations, steps)

    # To make 0 on x and y axes
    plt.xlim(xmin = 0)
    plt.ylim(ymin = 0)

    # Naming x and y axes
    plt.xlabel('input number')
    plt.ylabel('number of steps to reach 1')

    # Naming title of graph
    plt.title('Collatz conjecture: number of steps to reach 1 from starting numbers: '+str(iterations[0])+' to '+str(iterations[-1]))

    # Launching graph window
    plt.show()









