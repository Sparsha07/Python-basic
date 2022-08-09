from re import S


s=int(input("Enter the number to be reversed: "))
s2=int(input("Enter the number to be reversed: "))



def reverse_num(n):
    a = str(n)
    return int(a[::-1])

a = reverse_num(s)
print(a)
b = reverse_num(s2)
print(b)

sum = a + b
r_sum = reverse_num(sum)
print(r_sum)
