'''
Quick program to demonstrate match case
Match-case is a structure you can use for pattern matching. 
We'll probably always use if-elif-else instead, but it's good to know
that this exists
'''

def main():
    color = input("What is your favorite color? ")

    match color.lower():
        # each case is a value to check if it matches the value of color
        case "blue":
            print("Blue is a beautiful color")
        case "magenta":
            print("Magenta is a mix of red and blue")
        # | is "or"
        case "green" | "brown":
            print("You must like plants a lot")
        # This behaves like the "else" case
        case _:
            print(f"I agree that {color} is very nice")

main()

