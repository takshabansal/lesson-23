data = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 10
}
print("Dictionary:", data)
value = input("Enter a value to find its frequency: ")
try:
    value = int(value)
except ValueError:
    pass
frequency = list(data.values()).count(value)
print(f"The value '{value}' appears {frequency} time(s) in the dictionary.")