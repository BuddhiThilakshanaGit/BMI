from tkinter import*
from PIL import Image, ImageTk
import tkinter.messagebox


root=Tk()
root.geometry('580x326')
root.title('BMI')
root.resizable(False, False)
load = Image.open('C:\\Users\\My-Pc\\Desktop\\BMI.gif')
tkimage=ImageTk.PhotoImage(load)
Label(root,image= tkimage).place(x=0, y=0, relwidth=1, relheight=1)


l1=Label(root,text='Insert height',fg='blue',bg='powderblue')
l1.place(x=180,y=80)
l2=Label(root,text='Insert weight',fg='blue',bg='powderblue')
l2.place(x=180,y=105)
l11=Label(root,text='(cm)',fg='blue',bg='powderblue')
l11.place(x=385,y=80)
l22=Label(root,text='(kg) ',fg='blue',bg='powderblue')
l22.place(x=385,y=105)


Height=Entry(root,fg='red',bg='yellow')
Height.place(x=260,y=80)

weight=Entry(root,fg='red',bg='yellow')
weight.place(x=260,y=105)

def find():
    try:
        w=float(weight.get())
        h=int(Height.get())/100
        h2=h*h
        BMI_Calcu=w/h2
        BMI_STR= str(round(BMI_Calcu, 2))
        BCstring='      '+'Your BMI Value='+BMI_STR+'    '
        
        BMI=Label(root,text=BCstring,fg='red',bg='white')
        BMI.place(x=220,y=180)
        
        if BMI_Calcu>18.5 and BMI_Calcu<25:
            state=Label(root,text= 'You     are    Normal',fg='red',bg='white' )
            state.place(x=240,y=200)
    
        elif BMI_Calcu>25 and BMI_Calcu<29:
            state=Label(root,text= 'You are Overweight   ',fg='red',bg='white')
            state.place(x=240,y=200)
        elif BMI_Calcu<18.5:
            state=Label(root,text= 'You Have Malnutrition',fg='red',bg='white')
            state.place(x=240,y=200)
        else:
            state=Label(root,text= 'You    Have   Obesity',fg='red',bg='white')
            state.place(x=240,y=200)
            tkinter.messagebox.showinfo("Warning","You Have a Risk of Diabetes !")

    except ValueError:
        tkinter.messagebox.showinfo("WrongInput","Enter Values For Both Correctly !")
Button(text="FindMyBMI",command=find).place(x=260,y=145)

root.mainloop

