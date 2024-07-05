This week's exercises werre interesting and tough. Because of how tough it was, I decided to watch some beginner tutorials on youtube and finally understand what each function and method does. I feel slightly more confident as each week passes by. Just praying that I do ok in the quiz. :)

while True: (keeps the coding running until break)
guess = (low + high) // 2 (Calculates the middle number between 'low' and 'high'. the us eof interger division // ensure a wole number result)
if guess == actual_number: (checks if the guessed number is equal to the actual_number)
guess = guess
tries += 1 (Increases the number of ties by 1.)
break (stops loop if correct )
elif guess < actual_number:
low = guess
tries += 1
else:
high = guess
tries += 1

    return {"guess": guess, "tries": tries}
