''' Recursive code
    Sam Treadwell
    10/25/2022 '''

def iter_factorial(x):
        answer = 1
        for i in range(1, x+1):
            answer *= i
        return answer
print(iter_factorial(10))

def recur_factorial(x):
        if x == 1:
            return x
        else:   
            return recur_factorial(x-1) * x
print(recur_factorial(10))