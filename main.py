from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox

def handle_login():
    email = email_input.get()
    password = password_input.get()

    if email == 'sharthakkumar003@gmail.com' and password == '1234':
        messagebox.showinfo("Success", "Login Successful") 
    else:
        messagebox.showerror("Error", "Login Failed")  

root = Tk()
root.title('Login Form')

try:
    root.iconbitmap('favicon.ico')
except:
    print("Icon file not found. Skipping.")

root.minsize(400, 400)
root.geometry('350x500')
root.configure(background='#0096DC')

try:
    img = Image.open('images.jpeg')
    resized_img = img.resize((70, 70))
    img = ImageTk.PhotoImage(resized_img)
    img_label = Label(root, image=img, bg='#0096DC')
    img_label.pack(pady=(10, 10))
except:
    print("Image file not found. Skipping image.")

text_label = Label(root, text='Flipkart', fg='white', bg='#0096DC', font=('Verdana', 24))
text_label.pack()

email_label = Label(root, text='Enter Email', fg='white', bg='#0096DC', font=('Verdana', 12))
email_label.pack(pady=(20, 5))

email_input = Entry(root, width=30, font=('Verdana', 10))
email_input.pack(ipady=5, pady=(1, 15))

password_label = Label(root, text='Enter Password', fg='white', bg='#0096DC', font=('Verdana', 12))
password_label.pack(pady=(10, 5))

password_input = Entry(root, width=30, font=('Verdana', 10), show='*')  
password_input.pack(ipady=5, pady=(1, 15))

login_btn = Button(root, text='Login Here', bg='white', fg='black', width=20, height=2, font=('Verdana', 10),
                   command=handle_login)
login_btn.pack(pady=(10, 20))

root.mainloop()
