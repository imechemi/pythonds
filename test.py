
import random
import string

def generate():
	return ''.join([random.choice(string.ascii_lowercase + ' ') for _ in range(28)])

def score(word):
	target = "methinks it is like a weasel"
	score = 0
	for i, v in enumerate(word):
		if v == target[i]:
			score += 1

	return (score/28 * 100)

prev = ""
sc = 0
counter = 1
while counter < 1000:
	word = generate()
	sc = score(word)

	if sc == 100:
		print("Found: ", word)
		break

	if sc > score(prev):
		prev = word
	counter = counter + 1


print("Best match: ", prev)
print("Score: ", sc)