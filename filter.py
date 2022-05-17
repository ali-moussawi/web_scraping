from tkinter import *
import pandas as pd
import matplotlib.pyplot as plt



window=Tk()

window.title("find job")

window.geometry("500x400")

window.configure(bg='black') 

window.resizable(False,False)
h1=Label(window,text="enter the file name from the data folder :",height=1,font=("Arial",15),fg='#e91e63',bg="black")
h1.pack() # place it in window


h1=Label(window,text="",height=2,font=("Arial",15),bg="black")
h1.pack() # place it in window
work_var=StringVar()
work_var.set("")
work_input=Entry(window,width=20,font=("Arial",20),textvariable=work_var)
work_input.pack()
h1=Label(window,text="",height=1,font=("Arial",15),fg='#e91e63',bg="black")
h1.pack() # place it in window
h1=Label(window,text="",height=1,font=("Arial",15),fg='#e91e63',bg="black")
h1.pack() # place it in window



###########################################################################

def filter():
	window.destroy()
	value=work_var.get()
	df=pd.read_csv(f"./data/{value}"+".csv",encoding='unicode_escape')


	exp=df.loc[:,"skills"].values
	experience=[]
	for i in range(len(exp)):
		for j in range(len(exp[i])):
			if exp[i][j].isdigit():
				experience.append(exp[i][j])
				break


	title=df.loc[:,"job title"].values

	number=len(experience)
	plt.hist(experience, bins = number)
	plt.show()



Button(window, text="Next",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="black",activebackground="white",command=filter).pack()


window.mainloop() ## run app infinitely