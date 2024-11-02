def fahrenheit_to_celsius():
  try:
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5.0 / 9.0
    print(f"{fahrenheit} degrees Fahrenheit = {celsius}C.")
  except ValueError:
    print("Invalid input. Please enter a valid number for the temperature.")


if __name__ == "__main__":
  fahrenheit_to_celsius()