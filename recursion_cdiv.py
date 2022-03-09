"""
Exercise 165: Greatest Common Divisor
(24 Lines)
Euclid was a Greek mathematician who lived approximately 2,300 years ago. His
algorithm for computing the greatest common divisor of two positive integers, a and
b, is both efficient and recursive. It is outlined below:
If b is 0 then
Return a
Else
Set c equal to the remainder when a is divided by b
Return the greatest common divisor of b and c
Write a program that implements Euclid’s algorithm and uses it to determine the
greatest common divisor of two integers entered by the user.
"""
def common_div(a,b):
    if b == 0 :
        return a
    else:
        c = a % b
        return common_div(b,c)
def main():
    br1 = int(input("a = "))
    br2 = int(input("b= "))
    cd = common_div(br1,br2)
    print("Greatest common divisor is : ", cd)

main()
