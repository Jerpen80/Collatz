# To run this, you need to install matplotlib
# Do this by running: 'pip install matplotlib' in your shell

print("\nWelcome to my app to display Collatz Conjecture sequences in graphs")

# What is Collatz conjecture?
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
    
    # Creating lists for the graph with starting position
    x = [step]
    y = [n]
    
    # Loop to do the Collatz sequence until n is equal to 1 
    # If menu choice was 1 you get more detailed information
    while n != 1:
        if n % 2 == 0:
            n /= 2
            if menu == '1':
                print(int(n))
            step += 1
            x.append(int(step))
            y.append(int(n))

        else:
            n = 3 * n + 1
            if menu == '1':
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
    n = 0
    while n < 1:
        try:
            # Taking starting number from input
            n = int(input("\nGive an integer number above 0: "))
            while n < 1:
                print("number above 0 only!")
                n = int(input("\nGive an integer number above 0: "))
        except ValueError:
            print("Please enter a number!")

    step, x, y = seq(n)
    # Size of graph
    plt.figure(figsize=(14,10))

    # Drawing points(scatter) and lines(plot)
    #plt.scatter(x, y)
    plt.plot(x, y)

    # To make 0 on x and y axes
    plt.xlim(xmin = 0)
    plt.ylim(ymin = 1)

    # Naming x and y axes
    plt.xlabel('step count \n \n The highest point is: '+str(max(y)))
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
            end = int(input("Give last number of the range: "))
            while end <= start:
                print("number has to be above your starting number")
                end = int(input("Give last number of the range: "))
        except ValueError:
            print("Numbers only")
    
    steps = []
    iterations = []
    
    # For loop to do the sequence on a range of numbers
    for i in range(start,end+1): # ,2 after end+1 for only odd numbers(important that you start with an odd number) that will make it faster
        if i % 1000 == 0:
            print("Current number:",i)
        step, x, y = seq(i)
        iterations.append(i)
        steps.append(x[-1])

    # Determining which iteration had highest number of steps to reach 1    
    moststeps = max(steps)
    msnr = steps.index(moststeps)
    msnr2 = iterations[msnr]
    print("Highest number of steps is:",moststeps,"from number:",msnr2)
    
    # Size of graph
    plt.figure(figsize=(14,10))

    # Drawing points(scatter) and lines(plot)
    #plt.scatter(iterations, steps)
    plt.plot(iterations, steps)

    # To make 0 on x and y axes
    plt.ylim(ymin = 0)
    plt.xlim(xmin = start)

    # Naming x and y axes
    plt.xlabel('input number\n \nHighest number of steps is: '+str(moststeps)+' from number: '+str(msnr2))
    plt.ylabel('number of steps to reach 1')

    # Naming title of graph
    plt.title('Collatz conjecture: number of steps to reach 1 from starting numbers: '+str(iterations[0])+' to '+str(iterations[-1]))

    # Launching graph window
    plt.show()

print("\nThank you for using my tool! \n \nJeroen Penders\n")
    








