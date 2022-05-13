from tkinter import *
import wazzufscraping 
import indeedscraping
import threading
window=Tk()

window.title("find job")

window.geometry("500x700")

window.configure(bg='black') 

window.resizable(False,True)
h1=Label(window,text="please enter the job you want to search for :",height=2,font=("Arial",15),fg='#e91e63',bg="black")
h1.pack() # place it in window

h1=Label(window,text="",height=2,font=("Arial",15),bg="black")
h1.pack() # place it in window

h1=Label(window,text="job name :",height=2,font=("Arial",15),bg="black",fg="#e91e63")
h1.pack() # place it in window
work_var=StringVar()
work_var.set("")
work_input=Entry(window,width=20,font=("Arial",20),textvariable=work_var)
work_input.pack()

h1=Label(window,text="location  :",height=2,font=("Arial",15),bg="black",fg="#e91e63")
h1.pack() # place it in window
location_var=StringVar()
location_var.set("")
work_input1=Entry(window,width=20,font=("Arial",20),textvariable=location_var)
work_input1.pack()

h1=Label(window,text="",height=1,font=("Arial",15),bg="black")
h1.pack() 




def searchwazzuf():
	#get the text
	val=work_var.get()
	h2=Label(window,text="",height=2,font=("Arial",15),bg="black")

	h2.pack() 
	if (val==""):
		h2=Label(window,text=f"please enter a job name to search ",height=1,font=("Arial",10),bg="black",fg="white")
		h2.pack() 
		return

	else:
		searchfor=(work_var.get()).replace(".","")
		try:
			wazzufscraping.search_wazzuf(searchfor)
		except Exception:
			
			h2=Label(window,text="No Internet !",height=2,font=("Arial",15),bg="black",fg="white")
			h2.pack() # place it in window
		else:
			h2=Label(window,text=f"more than 100 {searchfor} job has been added to your file ",height=2,font=("Arial",15),bg="black",fg="white")
			h2.pack() # place it in window



def searchindeed():
	val=work_var.get()
	h2=Label(window,text="",height=2,font=("Arial",15),bg="black",fg="white")

	h2.pack() 
	if (val==""):
		h2=Label(window,text=f"please enter a job name to search ",height=1,font=("Arial",10),bg="black",fg="white")
		h2.pack() 
		return

	else:
		searchfor=(work_var.get()).replace(".","")
		location=location_var.get()
		try:
			indeedscraping.search_indeed(searchfor,location)
		except Exception:
			h2=Label(window,text="added a new file but some links are not working !",height=2,font=("Arial",15),bg="black",fg="white")
			h2.pack() # place it in window
		else :
			h2=Label(window,text=f"{searchfor} jobs has been added to your file ",height=2,font=("Arial",15),bg="black",fg="white")
			h2.pack() # place it in window



# create the button

h1=Label(window,text="",height=2,font=("Arial",15),bg="black")
h1.pack() # place it in window


btn=Button(window,text="search with wazzuf",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="black",activebackground="white",command=searchwazzuf)
btn.pack()

h1=Label(window,text="",height=1,font=("Arial",15),bg="black")
h1.pack() 


btn=Button(window,text="search with Indeed",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="black",activebackground="white",command=searchindeed)
btn.pack()



window.mainloop() ## run app infinitely



# fg = font color
#bg =background color










# try:
	# pass
#except Exception:
 	# pass
#except Exception:
 	# pass

#else :
	# pass

#finally :
	# pass


# why we need error handling :
# when we try something in python and it goes error
# a usefull information are appered when error is happened
# but if we would not want something like this to appear
# or desplayed to the people who are using our software
# so if we can expect that there is an code that will throw 
# an error, then we can use these try and accept blocks 
# to handle them in the way we want.
# try:
	# f=open('testfile.txt'):will throw error if file not found 
#1 except Exception:      Exception= type of Exception
 	# print(sorry file not found)
#2 except Exception as e:      Exception = type of Exception
 	# print(e)   e=the exeptio he catches
 	# we can add more and more 


#else :
	# if no exception is thrown

#finally :
	# runs no matter is happen