#Program to find the number of Notes dispatched buy ATM:----
Amount=int(input("Enter the amount to be despens: "))
temp=Amount-100
rs2k=temp//2000
temp1=temp%2000
rs5=temp1//500
temp2=temp1%500
rs1=((temp2//100)+1)
print("Rs 2000 Notes=",rs2k)
print("Rs 500 Notes=",rs5)
print("Rs 100 Notes=",rs1)
