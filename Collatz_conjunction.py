""" Collatz Conjecture: (3x + 1) """

from matplotlib import pyplot as plt
plt.style.use("ggplot")

""" This mathematical equation will ALWAYS end up with 1 """
count = 0
evens = 0
odds = 0
numbers = []
counts = []

number = int(input("Enter integer: "))
first = number

while number != 1:
	if number % 2 == 0:
		evens += 1
		number = int(number / 2)
	else:
		odds += 1
		number = int(number * 3 + 1)
	count += 1
	counts.append(count)
	numbers.append(number)
	
plt.plot(counts, numbers, color="k", linestyle="--", marker="o", label="Numbers")

plt.xlabel(f"Numbers\nSteps: {count}")
plt.ylabel(f"Results\nEvens: {evens} | Odds: {odds}")
plt.title(f"3x + 1 Illustration: Given number: {first}")
plt.grid(True)
plt.legend()
plt.show()
