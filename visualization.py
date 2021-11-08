import datetime
import matplotlib.pyplot as plt
import main


helpingArr_1 = {}
for i in range(len(main.result_1)):
    helpingArr_1[main.result_1[i][0]] = main.result_1[i][1]

plt.bar(helpingArr_1.keys(), helpingArr_1.values(), width=0.5)
plt.xlabel('Category')
plt.ylabel('Quantity')
# plt.show()
plt.savefig('1st.png')

helpingArr_2 = {}
for i in range(len(main.result_2)):
    helpingArr_2[main.result_2[i][0]] = main.result_2[i][1]

fig, ax = plt.subplots()
ax.pie(helpingArr_2.values(), labels=helpingArr_2.keys(), autopct='%1.1f%%', shadow=True, rotatelabels=True)
# plt.show()
plt.savefig('2st.png')
plt.clf()


def to_integer(dt_time):
    return 10000*dt_time.year + 100*dt_time.month + dt_time.day

x = []
y = []
helpingArr_3 = {}
for i in range(len(main.result_3)):
    helpingArr_3[to_integer(main.result_3[i][0])] = main.result_3[i][1]
    x.append(to_integer(main.result_3[i][0]))
    y.append(main.result_3[i][1])

plt.scatter(x, y)
plt.xlabel('Date of release')
plt.ylabel('Size')
# plt.show()
plt.savefig('3st.png')
