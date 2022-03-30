msg_0 = "Enter an equation"
msg_1 = "Do you even know what numbers are? Stay focused!"
msg_2 = "Yes ... an interesting math operation. You've slept through all classes, haven't you?"
msg_4 = "Do you want to store the result? (y / n): "
msg_5 = "Do you want to continue calculations? (y / n): "
msg_6 = " ... lazy"
msg_7 = " ... very lazy"
msg_8 = " ... very, very lazy"
msg_9 = "You are"
msg_10 = "Are you sure? It is only one digit! (y / n)"
msg_11 = "Don't be silly! It's just one number! Add to the memory? (y / n)"
msg_12 = "Last chance! Do you really want to embarrass yourself? (y / n)"
M = 0
result = 0


def is_one_digit(v):
    if v.is_integer() and -10 < v < 10:
        return True
    else:
        return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg = msg + msg_6
    if (float(v1) == 1 or float(v2) == 1) and v3 == "*":
        msg = msg + msg_7
    if (float(v1) == 0 or float(v2) == 0) and (v3 == "*" or v3 == "-" or v3 == "+"):
        msg = msg + msg_8
    if msg != "":
        msg = msg_9 + msg
    print(msg)

git -- help

while True:
    print(msg_0)
    num1, op, num2 = input().split()
    if num1 == "M":
        num1 = M
    if num2 == "M":
        num2 = M
    operations = ["/", "-", "+", "*"]
    if op not in operations:
        print(msg_2)
        continue

    try:
        try:
            float(num1)
            float(num2)
        except ZeroDivisionError:
            print(msg_1)

        check(float(num1), float(num2), op)

        if op == "/":
            result = float(num1) / float(num2)
        if op == "+":
            result = float(num1) + float(num2)
        elif op == "-":
            result = float(num1) - float(num2)
        elif op == "*":
            result = float(num1) * float(num2)
        print(result)
    except ZeroDivisionError:
        print("Yeah... division by zero. Smart move...")
        continue
    print(msg_4)
    q = input()  # do you want to store result?
    if q == "y":
        if is_one_digit(result):
            print(msg_10)
            q2 = input()
            if q2 == "y":
                print(msg_11)
                q3 = input()
                if q3 == "y":
                    print(msg_12)
                    q4 = input()
                    if q4 == "y":
                        M = result
        else:
            M = result
    print(msg_5)  # do you want to continue calculation?
    q1 = input()
    if q1 == "y":
        continue
    break
