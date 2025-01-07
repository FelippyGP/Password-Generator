import string
import secrets
import pyperclip
import customtkinter as ctk  

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")  

window = ctk.CTk()
window.title('Password Generator')
window.geometry("560x245")


CheckVar0 = ctk.BooleanVar(value=False)
CheckVar1 = ctk.BooleanVar(value=False)
CheckVar2 = ctk.BooleanVar(value=False)
CheckVar3 = ctk.BooleanVar(value=False)


def copy_to_clipboard():
    pyperclip.copy(pass_label.cget('text'))
 


def generate_password():
    chars = ''

    if CheckVar0.get():
        chars += string.ascii_lowercase
    if CheckVar1.get():
        chars += string.ascii_uppercase
    if CheckVar2.get():
        chars += string.digits
    if CheckVar3.get():
        chars += string.punctuation
    if chars == '':
        chars += string.ascii_lowercase
        check0.select()
        
    
    password = ''.join(secrets.choice(chars) for i in range(int(slider.get())))
    pass_label.configure(text=password)


pass_label = ctk.CTkLabel(master=window, text='password', font=('Calibri', 14))
pass_label.pack(pady=5)

output_frame = ctk.CTkFrame(master=window)
output_frame.pack(pady=10)


button1 = ctk.CTkButton(master=output_frame, text='Copiar', command=copy_to_clipboard)
button1.pack(side='left', padx=5)

button2 = ctk.CTkButton(master=output_frame, text='Gerar', command=generate_password)
button2.pack(side='left', padx=5)


input_frame = ctk.CTkFrame(master=window)
input_frame.pack(pady=10)


slider_int = ctk.IntVar(value=8)

slider = ctk.CTkSlider(master=input_frame, from_=4, to=72, number_of_steps=72,variable=slider_int,
command= lambda value: slider_label.configure(text=f"{int(slider_int.get()):02}"))
slider.pack(side='left', padx=5)
slider.set(4) 

slider_label = ctk.CTkLabel(master=input_frame,text='04')
slider_label.pack(side='left', padx=5)


check0 = ctk.CTkCheckBox(master=input_frame, text="Minúsculo", variable=CheckVar0)
check0.pack(pady=5)

check1 = ctk.CTkCheckBox(master=input_frame, text="Maiúsculas", variable=CheckVar1)
check1.pack(pady=5)

check2 = ctk.CTkCheckBox(master=input_frame, text="Números", variable=CheckVar2)
check2.pack(pady=5)

check3 = ctk.CTkCheckBox(master=input_frame, text="Caracteres", variable=CheckVar3)
check3.pack(pady=5)


window.mainloop()
