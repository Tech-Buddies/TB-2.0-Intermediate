def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x, y):
    return x / y

def multiply(x, y):
    return x * y

def SimpleAverage():
    i = [1, 2, 3, 4, 5]
    return sum(i) / len(i)

def WeightedAverage():
    value = [1, 2, 3, 4, 5]
    weight = [10, 20, 30, 40, 50]
    s = 0
    for a, b in zip(value, weight):
        s += a * b
    return s / sum(weight)

def GeometricMean():
    n = [1, 2, 3, 4, 5]
    multiply = 1
    for i in n:
        multiply = multiply * i
    return (multiply) ** (1/len(n))

def HarmonicMean():
    n = [1, 2, 3, 4, 5]
    sum = 0
    for i in n:
        sum += (1) / (i)
    return len(n) / sum

def QuadraticRoot():
    a = 2; b = 10; c = 5
    value = (b**2) - (4*a*c)
    root = value**0.5
    return [(-b + root)/(2*a),(-b - root)/(2*a)]



Sum = add(10, 20)
Minus = subtract(5 ,25)
Division = divide(25, 5)
Multiply = multiply(5, 10)
simple_avg = SimpleAverage()
w_average = WeightedAverage()
gmean = GeometricMean()
hmean = HarmonicMean()
quadratic_root = QuadraticRoot()

print(f"""Sum: {Sum}\nMinus: {Minus}\nDivision = {Division}\nMultiply = {Multiply}""")
print(f"Simple Average : {simple_avg}")
print(f"Weighted Average : {w_average}")
print("Geometric Mean: " +str(gmean))
print("Harmonic Mean: " +str(hmean))
print("Quadratic Root: " +str(quadratic_root))
