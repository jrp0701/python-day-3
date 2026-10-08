def vote_age_check():
    persons_age = input("How old are you?")
    if persons_age >= 18:
        print("You can vote!")
    else:
        print("Sorry, you cannot vote.")

def main():
    vote_age_check()

main()