#!/usr/bin/python3

def get_ranges():
	"Yields the values of the recursive formula."

	d, t = 2, 1

	while True:
		yield t

		d, t = 2 * d + 3 * t, d

class Coder():
	def __init__(self, length):
		"Requires the length of the encoded strings."

		if length < 4:
			raise ValueError()

		ranges = get_ranges()

		self.length = length
		self._boundaries = [2 * next(ranges) for i in range(length - 4)]
		self.range = next(ranges)

	def encode(self, number):
		"Number must be in the range."

		symbols = []

		i = len(self._boundaries) - 1

		while i >= 0:
			if number < self._boundaries[i]:
				symbols.append(number % 2)
				number //= 2
				i -= 1
			else:
				number -= self._boundaries[i]
				symbols.append(number % 3 + 2)
				number //= 3
				i -= 2

		result = "qd"

		for i in reversed(symbols):
			if i < 2:
				result += "qdb".replace(result[-1], "")[i]
			else:
				result += ["pq", "pd", "pb"][i - 2]

		return result + "pb"

	def decode(self, string):
		"Checks the format, but not the length."

		if string[: 2] != "qd" or string[-2: ] != "pb":
			raise ValueError()

		result = 0

		i = 0

		while i < len(self._boundaries):
			if string[i + 2] == "p":
				result *= 3
				result += "qdb".index(string[i + 3]) + self._boundaries[i + 1]
				i += 2
			else:
				result *= 2
				result += "qdb".replace(string[i + 1], "").index(string[i + 2])
				i += 1

		return result

if __name__ == "__main__":
	import sys
	import math

	if len(sys.argv) == 1:
		# Prints string lengths and their capacities in bits

		ranges = get_ranges()

		for i in range(163):
			print(i + 4, math.log(next(ranges), 2))
	elif len(sys.argv) == 2:
		# Decodes a string

		string = sys.argv[1]
		coder = Coder(len(string))
		decoded = coder.decode(sys.argv[1])

		print("{1:0{0}x}".format((math.ceil(math.log(coder.range, 2)) + 3) // 4, decoded))
	elif len(sys.argv) == 3:
		# Encodes a number to a string of the specified length

		length = int(sys.argv[1])
		number = int(sys.argv[2], 16)
		coder = Coder(length)

		if number >= coder.range:
			raise ValueError()

		print(coder.encode(number))
	else:
		raise ValueError()
