import threading


def increment_score():
    global score
    for x in range(1000000):
        score += 1


def decrement_score():
    global score
    for x in range(1000000):
        score -= 1


score = 0
first_thread = threading.Thread(target=increment_score)
second_thread = threading.Thread(target=decrement_score)

first_thread.start()
second_thread.start()

print(f"Le score est égal à {score}")
