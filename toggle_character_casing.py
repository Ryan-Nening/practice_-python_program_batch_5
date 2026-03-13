def toggle_character_casing():
    user_input = input("Enter your fullname: ")
    toggled_result = user_input.swapcase()
    print(f"Output: {toggled_result}")

if __name__ == "__main__":
    toggle_character_casing()