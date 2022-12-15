def counter(start=1):
    while True:
        yield start
        start += 1


print(counter(3))
