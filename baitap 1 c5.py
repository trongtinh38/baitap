numbers = []

while True:
    inp = input("Enter a number: ")

    if inp == "done":
        break

    try:
        num = float(inp)
        numbers.append(num)
    except:
        print("Invalid input")
        continue

if len(numbers) > 0:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No valid numbers entered")
