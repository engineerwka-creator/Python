def triangle_type ( a, b, c ):
    if a +b >= c and b + c >= a and a + c >= b:
        if a == b == c:
            return "Trójkąt Równoboczny"
        if a == b or b == c or c == a:
            return "Trójkąt Równoramienny"
        return "Trójkąt Różnoboczny"
    else:
        return "To nie trójkąt"

if __name__ == '__main__':
    result = triangle_type (1, 2, 3)
    print (result)

