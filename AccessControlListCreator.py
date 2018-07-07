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
			# owners.add(data[2])
			if data[2] not in owners:
				owners.append(data[2])
			details.append(d)
print(details)

print(value)
# permissions={}
# temp={}
# for user in owners:
# 	print(user)
# 	for detail in details:
# 		# print(detail)
# 		if detail["owner"]==user:
# 			temp[detail["filename"]]=detail["permission"][1:4]
# 			# print("case1")
# 			# permissions[user]=temp
# 		elif detail["group"]==groupsOfUser[user]:
# 			temp[detail["filename"]]=detail["permission"][4:7]
# 			# print("case2")
# 			# permissions[user]=temp
# 		else:
# 			temp[detail["filename"]]=detail["permission"][7:10]
# 			# print("case3")
# 		permissions[user]=temp
# 		temp.clear()
# 			
			
# print(permissions)
# for acls in permissions.keys():
# 	print("Username is "+acls)
# 	for acl in permissions[acls].keys():
# 		# print(str(acl)+" "+permissions[acls][acl])
# 		print("{0:^30} ".format(str(acl))+"{} ".format(permissions[acls][acl]))