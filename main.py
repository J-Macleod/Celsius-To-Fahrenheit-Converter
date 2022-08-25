def convert_c(c):

    f = ((9/5) * float(c)) + 32
    print("Fahrenheit: " + str(f))

up = True

while up:
    print("================================================")
    c = input("Celsius: ")
    convert_c(c)

