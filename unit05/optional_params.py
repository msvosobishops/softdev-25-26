'''
Notes for optional parameters with default values
'''

def greet_user(name, age=16, height=65, language="english"):
    if language == "english":
        print(f"Hello, {name}. I see you are {age} yrs old and {height} inches tall.")
    else:
        print(f"Hola, {name}. Veo como tu tienes {age} anos y eres {height} alto.")


def main():
    greet_user("Brooke", 15, 64, "english")
    greet_user("Ari", 15, 70, "spanish")
    greet_user("Charlotte")
    greet_user("Anya", height=64)

    print(print("hi"))

main()