from tkinter import *

# Inițializare fereastră principală
root = Tk()
root.title('Quiz App')
root['bg'] = 'steel blue'
root.geometry('1200x800')

# Contor pentru întrebări
count = 0
username = ""

# Adăugare widget-uri inițiale
label_t = Label(root, text='Car Logo Quiz', font=('Arial', 50), bg='steel blue')
label_t.place(x=600, y=50)

label1 = Label(root, text='Username =', font=('Arial', 50), bg='steel blue')
label1.place(x=300, y=235)

entry1 = Entry(root, font=('Arial', 30))
entry1.place(x=700, y=250)

# Încărcare imagini
img1 = PhotoImage(file='D:\\Python\\Quiz\\Photos_quiz\\Lexus.png')
img2 = PhotoImage(file='D:\\Python\\Quiz\\Photos_quiz\\Jaguar1.png')
img3 = PhotoImage(file='D:\\Python\\Quiz\\Photos_quiz\\Subaru.png')
img4 = PhotoImage(file='D:\\Python\\Quiz\\Photos_quiz\\Cadillac.png')
img5 = PhotoImage(file='D:\\Python\\Quiz\\Photos_quiz\\Cupra.png')

def show_question(question_num, img, options, correct_option):
    global count

    for widget in root.winfo_children():
        widget.destroy()

    label_q = Label(root, text=f'Question {question_num}:', font=('Arial', 40), bg='steel blue')
    label_q.place(x=650, y=0)

    label_img = Label(root, image=img)
    label_img.place(x=650, y=100)

    def check_answer(selected_option):
        global count
        if selected_option == correct_option:
            count += 1
        if question_num < 5:
            next_question()
        else:
            show_final_screen()

    button_y = 400
    for option in options:
        Button(root, text=option, font=('Arial', 30), command=lambda opt=option: check_answer(opt)).place(x=700, y=button_y)
        button_y += 100

def next_question():
    if next_question.q_num == 1:
        show_question(1, img1, ['Mazda', 'Honda', 'Opel', 'Lexus'], 'Lexus')
    elif next_question.q_num == 2:
        show_question(2, img2, ['Jaguar', 'Peugeot', 'Lamborghini', 'Porsche'], 'Jaguar')
    elif next_question.q_num == 3:
        show_question(3, img3, ['Toyota', 'Subaru', 'Hyundai', 'Nissan'], 'Subaru')
    elif next_question.q_num == 4:
        show_question(4, img4, ['Cadillac', 'Bentley', 'Dodge', 'Rolls Royce'], 'Cadillac')
    elif next_question.q_num == 5:
        show_question(5, img5, ['Maserati', 'Cupra', 'Acura', 'Infiniti'], 'Cupra')
    next_question.q_num += 1

next_question.q_num = 1

def show_final_screen():
    for widget in root.winfo_children():
        widget.destroy()

    label_ft = Label(root, text='Username =', font=('Arial', 45), bg='steel blue')
    label_ft.place(x=400, y=250)
    label_f = Label(root, text=username, font=('Arial', 45), bg='steel blue')
    label_f.place(x=730, y=250)

    label_ft1 = Label(root, text='Points =', font=('Arial', 45), bg='steel blue')
    label_ft1.place(x=400, y=350)
    label_f1 = Label(root, text=count, font=('Arial', 45), bg='steel blue')
    label_f1.place(x=620, y=350)

def comm1():
    global username
    username = entry1.get()
    next_question()

button1 = Button(root, text='SUBMIT', font=('Arial', 30), command=comm1)
button1.place(x=680, y=350)

# Pornire buclă principală
root.mainloop()