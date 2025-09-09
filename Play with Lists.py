l=[5,3,2,6,2,6,2,6,2,6,1,4]
print("original list:",l)
count=0
for i in l:
     count+=i
avg=count/len(l)
print("sum=")
l.sort()
print("smalest element is",l[0])
print("largest element is",l[-1])