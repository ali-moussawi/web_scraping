from tkinter import *
import wazzufscraping 
window=Tk()

window.title("find job")

window.geometry("500x500")

h1=Label(window,text="please enter the job you want to search for :",height=2,font=("Arial",15))
h1.pack() # place it in window

work_var=StringVar()
work_var.set(".............python..............")

work_input=Entry(window,width=20,font=("Arial",20),textvariable=work_var)
work_input.pack()

def search():
	#get the text
	searchfor=(work_var.get()).replace(".","")
	wazzufscraping.search(searchfor)
	
	h2=Label(window,text=f"more than 100 {searchfor} job has been added to your file ",height=2,font=("Arial",15))
	h2.pack() # place it in window

# create the button
btn=Button(window,text="search",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,command=search)
btn.pack()


window.mainloop() ## run app infinitely


