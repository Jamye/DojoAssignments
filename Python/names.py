students = [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
]


# def full_name(students):
#     for i in range(len(students)):
#         print students[i]["first_name"] + " " + students[i]["last_name"]

users = {
 'Students': [
     {'first_name':  'Michael', 'last_name' : 'Jordan'},
     {'first_name' : 'John', 'last_name' : 'Rosales'},
     {'first_name' : 'Mark', 'last_name' : 'Guillen'},
     {'first_name' : 'KB', 'last_name' : 'Tonel'}
  ],
 'Instructors': [
     {'first_name' : 'Michael', 'last_name' : 'Choi'},
     {'first_name' : 'Martin', 'last_name' : 'Puryear'}
  ]
 }



"""
Create a program that prints the following format (including number of characters in each combined name):

Students
1 - MICHAEL JORDAN - 13
2 - JOHN ROSALES - 11
3 - MARK GUILLEN - 11
4 - KB TONEL - 7
Instructors
1 - MICHAEL CHOI - 11
2 - MARTIN PURYEAR - 13

Thoughts:
create a loop to access the objects in users
print the key of these objects
create a loop to iterate through the list items(dictionary)
access the values in  inner dictionary
print the concatenated string
"""
# def student_and_instructor():
#     for i in range(len(users)):
#         print [i].key()
        # for show in key.value():
        #     print values

def student_and_instructor():
    for key in users:
        print "%s" % (key)

def student_and_instructor():
    for key in users:
        print key

        for i in range ():
            print str(i + 1) + " - " + students[i]["first_name"] + " " + students[i]["last_name"]
student_and_instructor()




#
#
#
# users = {
#  'students': [
#      {'first_name':  'Michael', 'last_name' : 'Jordan'},
#      {'first_name' : 'John', 'last_name' : 'Rosales'},
#      {'first_name' : 'Mark', 'last_name' : 'Guillen'},
#      {'first_name' : 'KB', 'last_name' : 'Tonel'}
#   ],
#  'instructors': [
#      {'first_name' : 'Michael', 'last_name' : 'Choi'},
#      {'first_name' : 'Trey', 'last_name' : 'Villafane'}
#   ]
#  }
#
# for key, data in users.items():
# 	print "\n%s" %key.title()
# 	counter = 0
#
# 	for value in data:
# 		counter = counter +1
# 		full_name = value["first_name"] + " " + value["last_name"]
# 		full_name_upper = full_name.upper()
# 		name_count = len(value["first_name"]) + len(value["last_name"])
#
# 		print "%d - %s - %d" %(counter, full_name_upper, name_count)
