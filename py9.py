x = [2, 4, 6, 8, 10, 12]
s1 = x[-1:2:-2]
s2 = x[::-2]
#s3 = x[0::0] ValueError: slice step cannot be zero
s4 = x[1::3]
s5 = x[0]
print(s1, s2, s4, s5)