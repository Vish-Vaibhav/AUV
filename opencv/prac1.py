def sing_green_bottles(start_bottles):

    if start_bottles <= 0:
        raise ValueError("Start bottles must be a positive integer.")

    num_bottles = start_bottles
    while num_bottles > 0:
        # Use f-strings for concise and readable string formatting
        print(f"\nThere are {num_bottles} green bottles hanging on the wall, {num_bottles} green bottles hanging on the wall,")
        if num_bottles > 1:
            print(f"And if one green bottle should accidentally fall,\n{num_bottles - 1} green bottles will be hanging on the wall.\n")
        else:
            print("And if one green bottle should accidentally fall,\nThere will be no more green bottles hanging on the wall.\n")

        # Use a more flexible input validation loop:
        while True:
            user_input = input("How many green bottles will be hanging on the wall? ")
            try:
                answer = int(user_input)
                if answer >= 0 and answer <= num_bottles:
                    break  # Valid input, exit the validation loop
                else:
                    print("Invalid answer. Please enter a non-negative number less than or equal to the current number of bottles.")
            except ValueError:
                print("Invalid answer. Please enter a whole number.")

        # Provide informative feedback:
        if answer == num_bottles - 1:
            print(f"Yes! There will be {answer} green bottles hanging on the wall.\n")
        else:
            print("No, try again.")

        num_bottles -= 1

    # Add a final message for completeness:
    print("\nThere are no more green bottles hanging on the wall.")

if __name__ == "__main__":
    start_bottles = int(input("How many green bottles are hanging on the wall initially? "))
    sing_green_bottles(start_bottles)
