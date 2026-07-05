first=int(input("first number="))
second=int(input("second number="))
print("without using temporary variable")
print("before swapping: \nfirst =",first,"\nsecond =",second)
first,second=second,first
print("after swapping: \nfirst =",first,"\nsecond =",second)
print("with using temporary variable")
tem=first
first=second
second=tem
print("after swapping: \nfirst =",first,"\nsecond =",second)
