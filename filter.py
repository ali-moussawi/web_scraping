import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("./data/java.csv",encoding='unicode_escape')



exp=df.loc[:,"skills"].values
experience=[]
for i in range(len(exp)):
	# print(len(exp[i]))
	for j in range(len(exp[i])):
		if exp[i][j].isdigit():
			experience.append(exp[i][j])
			break


title=df.loc[:,"job title"].values

plt.figure()

plt.plot(exp,title)
plt.show()
