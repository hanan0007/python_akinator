import akinator
# help(akinator)
aki = akinator.Akinator()
try:
    q = aki.start_game()
    print("Game started successfully.")
except RuntimeError as e:
    print(f"Failed to start the game: {e}")
    exit()

while aki.progression <= 80:
    a = input(q + "\n\t")
    if a == "b":
        try:
            q = aki.back()
        except akinator.CantGoBackAnyFurther:
            print("Can't go back any further.")
    else:
        q = aki.answer(a)

aki.win()

correct = input(
    f"It's {aki.first_guess['name']} ({aki.first_guess['description']})! Was I correct?\n{aki.first_guess['absolute_picture_path']}\n\t"
)
if correct.lower() == "yes" or correct.lower() == "y":
    print("Yay\n")
else:
    print("Oof\n")