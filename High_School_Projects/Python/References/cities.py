#Using break to exit a loop
prompt = input("Tell me something, and I will repeat it back to you: ")
prompt += "\nEnter 'quit' to end the program."
while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")