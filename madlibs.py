def mad_libs():
    print("Welcome to the Mad Libs Game!")
    print("Provide words to fill in the blanks and create a funny story!")

    # Collect inputs from the user
    name = input("Enter a name: ")
    place = input("Enter a place: ")
    animal = input("Enter an animal: ")
    action = input("Enter a verb (action): ")
    food = input("Enter a type of food: ")

    # Create a story
    story = f"""
    One day, {name} decided to visit {place}.
    While walking around, {name} saw a {animal} trying to {action}.
    It was so funny that {name} couldn't stop laughing!
    Later, they both sat together and enjoyed some delicious {food}.
    What an unforgettable day for {name}!
    """

    print("\nHere’s your Mad Libs story:")
    print(story)

if __name__ == "__main__":
    mad_libs()
