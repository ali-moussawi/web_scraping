from tkinter import *
import wazzufscraping 
import indeedscraping
window=Tk()

window.title("find job")

window.geometry("500x500")



h1=Label(window,text="please enter the job you want to search for :",height=2,font=("Arial",15))
h1.pack() # place it in window

h1=Label(window,text="",height=2,font=("Arial",15))
h1.pack() # place it in window

h1=Label(window,text="job name :",height=2,font=("Arial",15))
h1.pack() # place it in window
work_var=StringVar()
work_var.set("")
work_input=Entry(window,width=20,font=("Arial",20),textvariable=work_var)
work_input.pack()

h1=Label(window,text="location of the job (lebanon is default location) :",height=2,font=("Arial",15))
h1.pack() # place it in window
location_var=StringVar()
location_var.set("")
work_input1=Entry(window,width=20,font=("Arial",20),textvariable=location_var)
work_input1.pack()

h1=Label(window,text="",height=1,font=("Arial",15))
h1.pack() 



	###############################indeed################################

# def searchindeed():
# 	window1=Tk()
# 	window1.title("indeed")
# 	window1.geometry("600x300")

# 	h1=Label(window1,text="enter the location of job you would search for:",height=2,font=("Arial",15))
# 	h1.pack() # place it in window
# 	location_var=StringVar()
# 	location_var.set("")
# 	work_input=Entry(window1,width=20,font=("Arial",20),textvariable=location_var)
# 	work_input.pack()
# 	h1=Label(window1,text="",height=2,font=("Arial",15))
# 	h1.pack() 
# 	btn=Button(window1,text="start searching",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="white",activebackground="black",command=start_searching)
# 	btn.pack()

# 	window1.mainloop()
	



# def start_searching():
	
# 	print(location_var)
# 	# location_var=searchindeed()
# 	if (location_var==""):
# 		h2=Label(window1,text=f"please enter a valid location ",height=1,font=("Arial",10))
# 		h2.pack() 
# 		return

# 	else:
# 		location=location_var.get()
# 		# wazzufscraping.search_wazzuf(searchfor)
# 		h2=Label(window1,text=f"more than 100 {location} job has been added to your file ",height=2,font=("Arial",15))
# 		h2.pack() # place it in window


	###############################indeed end ################################


	
	###############################wazzuf######################################

def searchwazzuf():
	#get the text
	val=work_var.get()
	h2=Label(window,text="",height=2,font=("Arial",15))

	h2.pack() 
	if (val==""):
		h2=Label(window,text=f"please enter a job name to search ",height=1,font=("Arial",10))
		h2.pack() 
		return

	else:
		searchfor=(work_var.get()).replace(".","")
		wazzufscraping.search_wazzuf(searchfor)
	
		h2=Label(window,text=f"more than 100 {searchfor} job has been added to your file ",height=2,font=("Arial",15))
		h2.pack() # place it in window

	############################### end wazzuf################################

def searchindeed():
	val=work_var.get()
	h2=Label(window,text="",height=2,font=("Arial",15))

	h2.pack() 
	if (val==""):
		h2=Label(window,text=f"please enter a job name to search ",height=1,font=("Arial",10))
		h2.pack() 
		return

	else:
		searchfor=(work_var.get()).replace(".","")
		location=location_var.get()
		indeedscraping.search_indeed(searchfor,location)
	
		h2=Label(window,text=f"{searchfor} jobs has been added to your file ",height=2,font=("Arial",15))
		h2.pack() # place it in window



# create the button

h1=Label(window,text="",height=2,font=("Arial",15))
h1.pack() # place it in window


btn=Button(window,text="search with wazzuf",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="white",activebackground="black",command=searchwazzuf)
btn.pack()

h1=Label(window,text="",height=1,font=("Arial",15))
h1.pack() 


btn=Button(window,text="search with Indeed",width=20,height=2,bg="#e91e63",fg="white",borderwidth=0,activeforeground="white",activebackground="black",command=searchindeed)
btn.pack()



window.mainloop() ## run app infinitely
