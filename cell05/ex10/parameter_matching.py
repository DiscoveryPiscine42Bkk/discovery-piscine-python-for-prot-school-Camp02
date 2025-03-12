import sys

def main():
    if len(sys.argv) != 2:
        print("none")
        return
    
    param = sys.argv[1]
    user_input = input("Enter a word: ")

    if user_input == param:
        print("Good job!")
    else:
        print("Nope, sorry...")

if __name__ == "__main__":
    main()
input()