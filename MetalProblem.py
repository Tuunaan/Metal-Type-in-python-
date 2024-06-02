Hard= ""
CarCon= ""
tensen= ""
hard= int(input("\nHardness:"))
carb_con= float(input("\nCarbon Content:"))
tnsl= int(input("\nTensile strength:"))

if hard>50 :
    Hard = True
if carb_con<0.7 :
    CarCon= True
if tnsl>560 :
    tensen= True



if Hard and CarCon and tensen:
    print("Grade is 10")
elif Hard and CarCon :
    print("Grade is 9")
elif tensen and CarCon :
    print("Grade is 8")
elif Hard and tensen :
    print("Grade is 7")
elif Hard or CarCon or tensen:
    print("Grade is 6")
else:
    print("Grade is 5")
