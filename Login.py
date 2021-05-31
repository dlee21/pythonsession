import tkinter as tk

window = tk.Tk()
window.title("David's Login")
window.geometry("600x300")
window.resizable(width=True,height=False)

#Function
def validate_id_and_password():
    if ("DAVID" == ent_id.get().upper()):
        print("Yes, all validate. You can login")
        lbl_result_validate_login["text"] = "Yes, you can login"
    else:
        print("No,  incorrect  You cannot login")
        lbl_result_validate_login["text"] = "Sorry, you cannot login"

#Entry Label for id
frm_entry_id = tk.Frame(master=window)
ent_id = tk.Entry(master=frm_entry_id,width=10)
lbl_id = tk.Label(master=frm_entry_id,text="Enter ID: ", width=10)

#Input value for id
lbl_id.grid(row=2,column=0,sticky="w")
ent_id.grid(row=2,column=1,sticky="e")

#Button
btn_validate_login = tk.Button(
    master=window, text="Login",
    command=validate_id_and_password
)

#Label of login output result
lbl_result_validate_login = tk.Label(master=window, text = "")

#Entry label for password
frm_entry_pswd = tk.Frame(master=window)
ent_pswd = tk.Entry(master=frm_entry_pswd , width=15)
lbl_pswd = tk.Label(master=frm_entry_pswd, text="Enter password:", width=15)

#Input value for id
lbl_pswd.grid(row=3,column=0,sticky="w")
ent_pswd.grid(row=3,column=1,sticky="e")

#Placement of labels, buttons, results in the window
frm_entry_id.grid(row=0, column=0, padx=10)
frm_entry_pswd.grid(row=3,column=0, padx=10)
btn_validate_login.grid(row=9, column=0, pady=10)
lbl_result_validate_login.grid(row=10, column=0, padx=10)


window.mainloop()