delete = Button(root, text="Delete",font=("italic",10), bg="white", 
command=delete)
delete.place(x=70, y=200)
update= Button(root, text="Update",font=("italic",10), bg="white", 
command=update)
update.place(x=130, y=200)
get =Button(root, text="Get", font=("italic", 10), bg="white", command=get)
get.place(x=190,y=200)
list = Listbox(root)
list.place(x=290, y=200) 
print("everything is fine")
root.mainloop()