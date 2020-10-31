# Code in Python for Goodies Dilemma Problem
# Code written by: Shashwat Shahi (Sambhram Institute of Technology)
file1=open(r"C:\Users\shash\Desktop\HighPeakSW\input.txt","r") #opening file in read mode
lines=file1.readlines() #reads file until EOF
goodies=[] #initialized a goodies list
number_of_employees=int(lines[0][-2]) #assigned number of employees to variable
for i in range(4,len(lines)):
    l=lines[i].split(":")
    goodies.append([l[0],int(l[1])]) #assigned number of goodies from file to list
goodies=sorted(goodies,key=lambda x:x[1]) #sorted the list
min_diff=float('inf') #maximum value assigned to min_diff
for i in range(0,len(goodies)-number_of_employees+1): #calculating the minimum difference
    diff=goodies[i+number_of_employees-1][1]-goodies[i][1]
    if diff<min_diff:
        min_index=i
        min_diff=diff
file1.close() #closing file 1 i.e: input file
file2=open(r"C:\Users\shash\Desktop\HighPeakSW\output.txt","w") #opening output file
file2.write("The goodies selected for distribution are:\n")
file2.write("\n")
for i in range(min_index,min_index+number_of_employees):
    file2.write(goodies[i][0]+":"+str(goodies[i][1])+"\n")
file2.write("\n")
file2.write("And the difference between the chosen goodie with highest price and the lowest price is "+ str(min_diff))
file2.close() #closing output file