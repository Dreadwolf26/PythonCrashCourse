from name_function import get_formatted_name

print("Enter q anytime to quit")
while True:
    first = input("\nPlease enter your first name ")
    if first =="q":
        break
    middle = input('\nPlease iput your Middle name: ')
    if middle == 'q':
        break
    last = input("\nPlease enter your last name: ")
    if last =="q":
        break
    
    formatted_name = get_formatted_name(first_name=first, middle_name=middle,last_name=last)
    print(f"Your name in proper format: {formatted_name}")