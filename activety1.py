#take input for the student that he can attend the exam or not
medical_cause=input("did you have a medical cause Y or N: ")
#take input of the attendence
atten = int(input("enter the attendence of the student: "))

#cheaking the user input predicting out out accordingly
if medical_cause == 'Y': #cheaking the condition 1
  print ("you are allowed")
else:
  if atten>=75:  #cheaking the condition 2
    print ("allowed")
  else:
    print ("not allowed")