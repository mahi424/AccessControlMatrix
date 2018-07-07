details=[]
owners=[]
groupsOfUser={}
with open("out2.txt", "r") as f:
	lines=f.readlines()
	for line in lines:
		data=line.split()
		if len(data)>2:
			d={
			"permission":data[0],
			"owner":data[2],
			"group":data[3],
			"filename":data[8],
			}
			groupsOfUser[data[2]]=data[3]
			if data[2] not in owners:
				owners.append(data[2])
			details.append(d)
# print(details)

permissions={}
p=[]
temp={}
listOfItems=[]
for user in owners:
	# print(user)
	for detail in details:
		# print(detail)
		if detail["owner"]==user:
			temp[detail["filename"]]=detail["permission"][1:4]
			x=detail["permission"][1:4]
			# print("case1")
		elif detail["group"]==groupsOfUser[user]:
			temp[detail["filename"]]=detail["permission"][4:7]
			# print("case2")
		else:
			temp[detail["filename"]]=detail["permission"][7:10]
			# print("case3")
		if detail["filename"] not in listOfItems:
			listOfItems.append(detail["filename"])
	if temp is not None:
		permissions[user]=dict(temp)
		temp.clear()

# print(permissions)
# print(listOfItems)
items="     "
underline="====="
for item in listOfItems:
	items+="{0:^25}".format(item)
	underline+="{0:=^25}".format("")
print(items)
print(underline)

row=""
for user in permissions.keys():
	# print(user)
	row=""
	row=row+str(user)
	# for key in permissions[user].keys():
	# 	row+="{0:^25}".format(str(permissions[user][key]))
	for key in listOfItems:
		row+="{0:^25}".format(str(permissions[user][key]))
	print(row)
