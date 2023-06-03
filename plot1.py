# read File
with open('clean_data.csv', encoding="utf8") as file:
    data = file.read().split("\n")


header = data[0]
# print(header)
stundets = data[1:]
stundets.pop()
# print(stundets)
total_student = len(stundets)

header = header.split(",")
subjects = header[5:]
print(subjects)
for i in range(len(stundets)):
    stundets[i] = stundets[i].split(',')

not_take_exam = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for s in stundets:
    for i in range(5, 16):
        if s[i] == "-1":
            not_take_exam[i-5] += 1

not_take_exam_percentage = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in range(0,11):
    not_take_exam_percentage[i] = round(not_take_exam[i]*100/total_student,2)

print(not_take_exam_percentage)
