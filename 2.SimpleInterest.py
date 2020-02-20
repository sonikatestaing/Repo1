P = float(input("Enter priniciple Amount:"))
R = float(input("Enter Rate of Interest:"))
T=float(input("Enter Time period:"))

SI = (P*R*T/100)

print('Simple interest for Amount = {0}, for rate = {1}, for time = {2} is {3}'.format(P,R,T,SI))
