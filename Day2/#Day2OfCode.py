print("Welcome to the tip calculator.")
total_bil=float(input("what was the total bill? Rs." ))
x=int(input("What persentage tip would you like to give? 10, 12, or 15?"))
person=int(input("How many people to split the bill?"))

tip=(total_bil*x)/100
total=(total_bil+tip)
payByEachPerson=total/person
print("Each person Should pay:",payByEachPerson)



print("for exit press enter")
input()
