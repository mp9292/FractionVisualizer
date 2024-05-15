import matplotlib.pyplot as plt
from fractions import Fraction

def display_fraction_image(numerator, denominator):
    # Create a pie chart to represent the fraction
    sizes = [numerator, denominator - numerator]
    labels = [f'{numerator}/{denominator}', f'{denominator - numerator}/{denominator}']
    plt.pie(sizes, labels=labels, autopct='%1.1f%%')
    plt.title(f'Fraction: {numerator}/{denominator}')
    plt.show()

def main():
    # Input fraction from the user
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Display the fraction as an image
    display_fraction_image(numerator, denominator)

if __name__ == "__main__":
    main()
