lst=list(map(int,input().split()))
new_list=[]
for i in lst:
    if i not in new_list:
        new_list.append(lst.count(i))
print(max(new_list))

