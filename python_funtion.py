def get_total(a, b):
    #local variable declared inside a function
    total = a + b
    return total

print(get_total(5, 2))


# BEGIN: 7e8d9f6g7h8i
total = get_total(5, 2)
print(total)
# END: 7e8d9f6g7h8i


def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b

    def double_it():
        #local variable
        double = total * 2
        print(double)

    double_it()
    #double variable will not be accessible
    print(double)

    return total

special = 5

def get_total(a, b):
    #enclosed scope variable declared inside a function
    total = a + b
    print(special)

    def double_it():
        #local variable
        double = total * 2
        print(special)

    double_it()

    return total