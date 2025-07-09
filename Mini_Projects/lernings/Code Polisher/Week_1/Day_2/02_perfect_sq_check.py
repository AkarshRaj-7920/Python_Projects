# Perfect Square Checker

# Module
import math

# Functions
def is_perfect_square_root(n: int) -> bool:
    '''
    Checks if the give non-negative integer is a perfect square.
    Args:
        n (int): The Input number in form of integer
    Returns:
        A word which tells the user weather the entered number is perfect square or not
    '''

    if n < 0:
        return False
    
    root = math.isqrt(n)
    return root * root == n

# Input
def main():
    while True:
        user_input = input("• Enter a Integral Number: ")
        if not user_input.strip().isdigit():
            print(" ○ Invalid Input. Please Enter an Integral Value... \n")
        else:
            break

    int_user_input = int(user_input.strip())    # Conversion

    result = is_perfect_square_root(int_user_input)
    print(f"• Perfect Square Root: {result}")

if __name__ == "__main__":
    main()
