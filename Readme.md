QDPB code
=========

Data encoding algorithm.

Designed to encode key fingerprints, tripcodes, cryptocurrency wallet addresses and other pseudorandom idetifiers.

Examples
--------

```
qdbdpqpbqpqpbdqpbpbqdpdqpqbdpdqdbpbqbpdbpqdpb
```

Contains about 64 bits of information. Another identifier produces a completely different output:

```
qdbqdbqpdpdbqbqpbqdbpqpdqbpqdbpdqdpqdpbqbdbpb
```

Features
--------

- Encoded strings start and end with fixed patterns.

- No sequences of duplicate letters.

- Very unlikely to contain real language words.

Specification
-------------

The code is reversible and is a bijection from a range of integers to strings of the letters `qdpb` with the following properties:
- the string starts with the pair `qd` and ends with `pb`;
- it doesn't contain doubled letters;
- its length is constant for each particular range of encoded numbers.

The numbers range from 0 to the upper boundary (not including it), which can be determined from the string length with this recursive function:

```
n(4) = 1
n(5) = 2
n(length) = 2 * n(length - 1) + 3 * n(length - 2)
```

To decode a string:
- cut the first two and the last two letters;
- set the resulting number to 0;
- for each letter of the remaining string:
	- if it's one of `qdb`:
		- double the resulting number;
		- find the letter in the array `qdb` and increase the number by its index;
		- decrease the number by 1 if the index of the previous letter in the string (if exists, otherwise `d`) is less than the current;
	- otherwise it's `p`:
		- triple the number;
		- consume another letter and increase the number by its index in the array `qdb`;
		- increase the number by `2 * n(number of consumed letters + 3)`.

The encoding process is obvious from this description.

Links
-----

* [Source code](https://github.com/Kleshni/QDPB/archive/master.zip).
* [Git repository](https://github.com/Kleshni/QDPB.git).
* [Issue tracker](https://github.com/Kleshni/QDPB/issues).
* Bitmessage: BM-2cT5WWccBgLsHTw5ADLcodTz4dbqdtrwrQ.
* Mail: [kleshni@protonmail.ch](mailto:kleshni@protonmail.ch).
