def greetings(name="Alexandra"):

    if not isinstance(name, str):
        print("Error:It was not a name.")
    else:
        print(f"Hello, {name}!")


greetings("Wil")
greetings()
greetings(42)
input()