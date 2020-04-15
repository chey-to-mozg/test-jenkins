import sys


def compare(num):
	num = int(num)
	if num > 0:
		print("GREATER")
	elif num < 0:
		print("LOWER")
	else:
		print("ZERO")


if __name__ == "__main__":
	actions = {'compare': compare}
	action = sys.argv[1]
	args = sys.argv[2:]
	actions[action](*args)
