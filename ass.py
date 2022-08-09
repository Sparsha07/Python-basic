 

print("Enter marks of 5 subjects out of 100:")
sub1=float(input("Enter maths marks:"))
print(sub1)
sub2=float(input("Enter science marks:"))
sub3=float(input("Enter history marks:"))
sub4=float(input("Enter english marks:"))
sub5=float(input("Enter marathi marks:"))

total_marks=sub1+sub2+sub3+sub4+sub5
avg=total_marks/5.0
percentage=total_marks/500*100
passing=50

print("Total Marks:",total_marks)
print("Average:",avg)
print("Percentage:",percentage,"%")
if percentage > passing:
  print("Student is Pass")
elif percentage == passing:
  print("Student is Pass")
else:
  print("Student is Fail")
