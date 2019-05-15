##import tkinter as tk
##from tkinter import *
import sqlite3
##import matplotlib.pyplot as plt
##from matplotlib import style
##style.use("fivethirtyeight")
#import Pmw
import tkinter as tk
from tkinter import ttk,font
import tkinter.messagebox as tm

def other_functions():
    app.destroy()
    class Page(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
        def show(self):
            self.lift()
    #homepage
    class Page1(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
##           canvas = tk.Canvas(self)
##           canvas.pack()
 
           image1 = tk.PhotoImage(master=self, file="homepage2.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1
           label = tk.Label(self, text=" ")
           label.pack(side="top", expand=True)

           style = ttk.Style(self)
           style.configure('TButton', background='blue',relief="raised")
    ##       if 1==0:
    ##           style.configure('TButton', foreground='red')#blue
    ##       else:
    ##           style.configure('TButton', foreground='blue')
            #different frames
           def initialise():
               carbohydrates.configure(bg = "#5DADE2")
               proteins.configure(bg = "#5DADE2")
               fats.configure(bg = "#5DADE2")
               vitaminsA.configure(bg = "#5DADE2")
               lblunch.delete(0,tk.END)
               lbbreakfast.delete(0,tk.END)
               lbsuper.delete(0,tk.END)
               lbsnacks.delete(0,tk.END)
            
           b1 = ttk.Button(self, text="Page 1")
           b1.place(x=800,y=50,width=60)# .grid(row=0,column=9,sticky=tk.E)
           b2 = ttk.Button(self, text="Page 2")
           b2.place(x=865,y=50,width=60)#.grid(row=0,column=10)
           b3 = ttk.Button(self, text="Page 3")
           b3.place(x=930,y=50,width=60)#.grid(row=0,column=11)
           b4 = ttk.Button(self, text="initialise",command=initialise)
           b4.place(x=975,y=700,width=60)
           b5 = tk.Button(self, text=" ",bg="green")
           b5.place(x=10,y=700,width=60)
           

           label = tk.Label(self, text="Nutrients").place(x=10,y=20)  #.grid(row=0,column=0)
           label = tk.Label(self, text="perfect diet if all nutrients are green").place(x=70,y=700)

           y1=170
           #, ('proteins', 2),('fibres', 3), ('vitamins', 4)
           def color_change():

               carbohydrates.configure(bg = "red")


           global carbohydrates
           global proteins
           global fats
           global vitaminsA
           carbohydrates=tk.Button(self, text='Carbohydrates', state='normal',fg='yellow',bg="#5DADE2")
           carbohydrates.place(x=10,y=170,width=85)
           proteins=tk.Button(self, text='proteins',fg='yellow',bg="#5DADE2")
           proteins.place(x=10,y=210,width=85)
           fats=tk.Button(self, text='fats',fg='yellow',bg="#5DADE2")
           fats.place(x=10,y=250,width=85)
           vitaminsA=tk.Button(self, text='vitamins A',fg='yellow',bg="#5DADE2")
           vitaminsA.place(x=10,y=290,width=85)
           #carbohydrates.configure(fg="blue")

           
           #for text, value in [('Breakfast', 1), ('Super', 2)]:
           breakfast=ttk.Button(self, text='Breakfast').place(x=350,y=200,width=85)
           supper=ttk.Button(self, text='Super').place(x=350,y=480,width=85)


           y1=200
           #for text, value in [('Lunch', 1), ('Snacks', 2)]:
           lunch=ttk.Button(self, text='Lunch').place(x=700,y=200,width=85)
           snacks=ttk.Button(self, text='Snacks').place(x=700,y=480,width=85)
           y1+=280

           #lunchlistbox
 

           global lblunch 
           lblunch=tk.Listbox(self, width=100)#.place(x=350,y=y1,width=290)
           lblunch.place(x=700,y=235,width=290)
   

           global lbsnacks
           lbsnacks=tk.Listbox(self, width=100)
           lbsnacks.place(x=700,y=515,width=290)
           


           #breakfastlistbox
           y1=235
  

           global lbbreakfast
           lbbreakfast=tk.Listbox(self, width=100)
           lbbreakfast.place(x=350,y=235,width=290)
           

           #Superlistbox
           y1=515
 

           global lbsuper
           lbsuper=tk.Listbox(self, width=100)
           lbsuper.place(x=350,y=515,width=290)


           
    #food
    class Page2(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
##           canvas = tk.Canvas(self)
##           canvas.pack()
           image1 = tk.PhotoImage(master=self, file="food list.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1
           #label = ttk.Label(self, text="This is page 2")
           #label.pack(side="top", fill="both", expand=True)
           label1 = ttk.Label(self, text=" Carbohydrates", font='times 12').place(x=20,y=40)
           label2 = ttk.Label(self, text=" Proteins", font='times 12').place(x=20,y=200)
           label3 = ttk.Label(self, text=" Fats", font='times 12').place(x=20,y=360)
           label4 = ttk.Label(self, text=" Vitamin A", font='times 12').place(x=20,y=520)

           def add2break():
               balancedmeal=[]
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               if var1.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",("Posho","K,Na,Fats"))
                   lbbreakfast.insert(tk.END,("Posho","K,Na,Fats"))
                   balancedmeal.append("Posho")
                   carbohydrates.configure(bg="green")
                   check1.deselect()
                   p1.lift()
                   root1.destroy()
               if var2.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('Nyasa','Na,VitaminC,Fe'))
                   lbbreakfast.insert(tk.END,('Nyasa','Na,VitaminC,Fe'))
                   carbohydrates.configure(bg="green")
                   balancedmeal.append("Nyasa")
                   check2.deselect()
                   p1.lift()
                   root1.destroy()
               if var3.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   lbbreakfast.insert(tk.END,("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   carbohydrates.configure(bg="green")
                   balancedmeal.append("Sugarcane")
                   check3.deselect()
                   p1.lift()
                   root1.destroy()
               if var4.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   lbbreakfast.insert(tk.END,("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   carbohydrates.configure(bg="green")
                   balancedmeal.append("Sweetpotatoes")
                   check4.deselect()
                   p1.lift()
                   root1.destroy()
               if var5.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('chicken','vitmnB, K ,Po'))
                   lbbreakfast.insert(tk.END,('chicken','vitmnB, K ,Po'))
                   proteins.configure(bg="green")
                   balancedmeal.append("chicken")
                   check5.deselect()
                   p1.lift()
                   root1.destroy()
               if var6.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   lbbreakfast.insert(tk.END,('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   proteins.configure(bg="green")
                   balancedmeal.append("beans")
                   check6.deselect()
                   p1.lift()
                   root1.destroy()
               if var7.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('eggs','fat,Fe,vitamins,minerals'))
                   lbbreakfast.insert(tk.END,('eggs','fat,Fe,vitamins,minerals'))
                   proteins.configure(bg="green")
                   balancedmeal.append("eggs")
                   check7.deselect()
                   p1.lift()
                   root1.destroy()
               if var8.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('beef','Zn,Fe,vitaminB12'))
                   lbbreakfast.insert(tk.END,('beef','Zn,Fe,vitaminB12'))
                   proteins.configure(bg="green")
                   balancedmeal.append("beef")
                   check8.deselect()
                   p1.lift()
                   root1.destroy()
               if var9.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   lbbreakfast.insert(tk.END,('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   fats.configure(bg="green")
                   balancedmeal.append("ovaccado")
                   check9.deselect()
                   p1.lift()
                   root1.destroy()
               if var10.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('gnuts','Na,K,fat'))
                   lbbreakfast.insert(tk.END,('gnuts','Na,K,fat'))
                   balancedmeal.append("gnuts")
                   fats.configure(bg="green")
                   check10.deselect()
                   p1.lift()
                   root1.destroy()
               if var11.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('Fattyfish','vitaminD,fat'))
                   lbbreakfast.insert(tk.END,('Fattyfish','vitaminD,fat'))
                   balancedmeal.append("Fattyfish")
                   fats.configure(bg="green")
                   check11.deselect()
                   p1.lift()
                   root1.destroy()
               if var12.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   lbbreakfast.insert(tk.END,('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   balancedmeal.append("liver")
                   vitaminsA.configure(bg="green")
                   check12.deselect()
                   p1.lift()
                   root1.destroy()
               if var13.get()==1:
                   cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   lbbreakfast.insert(tk.END,('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   balancedmeal.append("greenvegetables")
                   vitaminsA.configure(bg="green")
                   check13.deselect()
                   p1.lift()
                   root1.destroy()
               cur.execute("INSERT INTO BALANCEDMEAL VALUES (NULL,?)",(balancedmeal))    
##               def bmeal():
##                   con=sqlite3.connect("diet.db")
##                   cur=con.cursor()
##                   cur.execute("SELECT MEAL FROM BALANCEDMEAL")
##                   rows=cur.fetchall()
##                   
##                   #cur.execute("INSERT INTO BALANCEDMEAL2 VALUES (NULL,?)",(m,))
##    
##
##                       
##               bmeal()
               con.commit()
               con.close()
        
           def add2lunch():
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               if var1.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",("Posho","K,Na,Fats"))
                   lblunch.insert(tk.END,("Posho","K,Na,Fats"))
                   carbohydrates.configure(bg="green")
                   check1.deselect()
                   p1.lift()
                   root1.destroy()
                   
               if var2.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('Nyasa','Na,VitaminC,Fe'))
                   lblunch.insert(tk.END,('Nyasa','Na,VitaminC,Fe'))
                   carbohydrates.configure(bg="green")
                   check2.deselect()
                   p1.lift()
                   root1.destroy()
               if var3.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   lblunch.insert(tk.END,("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   carbohydrates.configure(bg="green")
                   check3.deselect()
                   p1.lift()
                   root1.destroy()
               if var4.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   lblunch.insert(tk.END,("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   carbohydrates.configure(bg="green")
                   check4.deselect()
                   p1.lift()
                   root1.destroy()
               if var5.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('chicken','vitmnB, K ,Po'))
                   lblunch.insert(tk.END,('chicken','vitmnB, K ,Po'))
                   proteins.configure(bg="green")
                   check5.deselect()
                   p1.lift()
                   root1.destroy()
               if var6.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   lblunch.insert(tk.END,('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   proteins.configure(bg="green")
                   check6.deselect()
                   p1.lift()
                   root1.destroy()
               if var7.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('eggs','fat,Fe,vitamins,minerals'))
                   lblunch.insert(tk.END,('eggs','fat,Fe,vitamins,minerals'))
                   proteins.configure(bg="green")
                   check7.deselect()
                   p1.lift()
                   root1.destroy()
               if var8.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('beef','Zn,Fe,vitaminB12'))
                   lblunch.insert(tk.END,('beef','Zn,Fe,vitaminB12'))
                   proteins.configure(bg="green")
                   check8.deselect()
                   p1.lift()
                   root1.destroy()
               if var9.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   lblunch.insert(tk.END,('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   fats.configure(bg="green")
                   check9.deselect()
                   p1.lift()
                   root1.destroy()
               if var10.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('gnuts','Na,K,fat'))
                   lblunch.insert(tk.END,('gnuts','Na,K,fat'))
                   fats.configure(bg="green")
                   check10.deselect()
                   p1.lift()
                   root1.destroy()
               if var11.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('Fattyfish','vitaminD,fat'))
                   lblunch.insert(tk.END,('Fattyfish','vitaminD,fat'))
                   fats.configure(bg="green")
                   check11.deselect()
                   p1.lift()
                   root1.destroy()
               if var12.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   lblunch.insert(tk.END,('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   vitaminsA.configure(bg="green")
                   check12.deselect()
                   p1.lift()
                   root1.destroy()
               if var13.get()==1:
                   cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   lblunch.insert(tk.END,('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   vitaminsA.configure(bg="green")
                   check13.deselect()
                   p1.lift()
                   root1.destroy()
               
               con.commit()
               con.close()
           def add2super():
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               if var1.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",("Posho","K,Na,Fats"))
                   lbsuper.insert(tk.END,("Posho","K,Na,Fats"))
                   carbohydrates.configure(bg="green")
                   check1.deselect()
                   p1.lift()
                   root1.destroy()
               if var2.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('Nyasa','Na,VitaminC,Fe'))
                   lbsuper.insert(tk.END,('Nyasa','Na,VitaminC,Fe'))
                   carbohydrates.configure(bg="green")
                   check2.deselect()
                   p1.lift()
                   root1.destroy()
               if var3.get()==1:
                   cur.execute("INSERT INTO  SUPER VALUES (NULL,?,?)",("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   lbsuper.insert(tk.END,("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   carbohydrates.configure(bg="green")
                   check3.deselect()
                   p1.lift()
                   root1.destroy()
               if var4.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   lbsuper.insert(tk.END,("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   carbohydrates.configure(bg="green")
                   check4.deselect()
                   p1.lift()
                   root1.destroy()
               if var5.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('chicken','vitmnB, K ,Po'))
                   lbsuper.insert(tk.END,('chicken','vitmnB, K ,Po'))
                   proteins.configure(bg="green")
                   check5.deselect()
                   p1.lift()
                   root1.destroy()
               if var6.get()==1:
                   cur.execute("INSERT INTO  SUPER VALUES (NULL,?,?)",('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   lbsuper.insert(tk.END,('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   proteins.configure(bg="green")
                   check6.deselect()
                   p1.lift()
                   root1.destroy()
               if var7.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('eggs','fat,Fe,vitamins,minerals'))
                   lbsuper.insert(tk.END,('eggs','fat,Fe,vitamins,minerals'))
                   proteins.configure(bg="green")
                   check7.deselect()
                   p1.lift()
                   root1.destroy()
               if var8.get()==1:
                   cur.execute("INSERT INTO SUPER  VALUES (NULL,?,?)",('beef','Zn,Fe,vitaminB12'))
                   lbsuper.insert(tk.END,('beef','Zn,Fe,vitaminB12'))
                   proteins.configure(bg="green")
                   check8.deselect()
                   p1.lift()
                   root1.destroy()
               if var9.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   lbsuper.insert(tk.END,('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   fats.configure(bg="green")
                   check9.deselect()
                   p1.lift()
                   root1.destroy()
               if var10.get()==1:
                   cur.execute("INSERT INTO SUPER  VALUES (NULL,?,?)",('gnuts','Na,K,fat'))
                   lbsuper.insert(tk.END,('gnuts','Na,K,fat'))
                   fats.configure(bg="green")
                   check10.deselect()
                   p1.lift()
                   root1.destroy()
               if var11.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('Fattyfish','vitaminD,fat'))
                   lbsuper.insert(tk.END,('Fattyfish','vitaminD,fat'))
                   fats.configure(bg="green")
                   check11.deselect()
                   p1.lift()
                   root1.destroy()
               if var12.get()==1:
                   cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   lbsuper.insert(tk.END,('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   vitaminsA.configure(bg="green")
                   check12.deselect()
                   p1.lift()
                   root1.destroy()
               if var13.get()==1:
                   cur.execute("INSERT INTO SUPER  VALUES (NULL,?,?)",('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   lbsuper.insert(tk.END,('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   vitaminsA.configure(bg="green")
                   check13.deselect()
                   p1.lift()
                   root1.destroy()
               
               con.commit()
               con.close()

           def add2snacks():
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               if var1.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",("Posho","K,Na,Fats"))
                   lbsnacks.insert(tk.END,("Posho","K,Na,Fats"))
                   carbohydrates.configure(bg="green")
                   
                   p1.lift()
                   root1.destroy()
               if var2.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('Nyasa','Na,VitaminC,Fe'))
                   lbsnacks.insert(tk.END,('Nyasa','Na,VitaminC,Fe'))
                   carbohydrates.configure(bg="green")
                   
                   p1.lift()
                   root1.destroy()
               if var3.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   lbsnacks.insert(tk.END,("Sugarcane","Mg,Zn,Ca,Fe,K"))
                   carbohydrates.configure(bg="green")
                   check3.deselect()
                   p1.lift()
                   root1.destroy()
               if var4.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   lbsnacks.insert(tk.END,("Sweetpotatoes","vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po"))
                   carbohydrates.configure(bg="green")
                   check4.deselect()
                   p1.lift()
                   root1.destroy()
               if var5.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('chicken','vitmnB, K ,Po'))
                   lbsnacks.insert(tk.END,('chicken','vitmnB, K ,Po'))
                   proteins.configure(bg="green")
                   check5.deselect()
                   p1.lift()
                   root1.destroy()
               if var6.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   lbsnacks.insert(tk.END,('beans','vitmnC,vitmnB6,Cu,K,Po,Mg'))
                   proteins.configure(bg="green")
                   check6.deselect()
                   p1.lift()
                   root1.destroy()
               if var7.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('eggs','fat,Fe,vitamins,minerals'))
                   lbsnacks.insert(tk.END,('eggs','fat,Fe,vitamins,minerals'))
                   proteins.configure(bg="green")
                   check7.deselect()
                   p1.lift()
                   root1.destroy()
               if var8.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('beef','Zn,Fe,vitaminB12'))
                   lbsnacks.insert(tk.END,('beef','Zn,Fe,vitaminB12'))
                   proteins.configure(bg="green")
                   check8.deselect()
                   p1.lift()
                   root1.destroy()
               if var9.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   lbsnacks.insert(tk.END,('ovaccado','vitmnC,vitmnE,vitmnK,vitmnB6'))
                   fats.configure(bg="green")
                   check9.deselect()
                   p1.lift()
                   root1.destroy()
               if var10.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('gnuts','Na,K,fat'))
                   lbsnacks.insert(tk.END,('gnuts','Na,K,fat'))
                   fats.configure(bg="green")
                   check10.deselect()
                   p1.lift()
                   root1.destroy()
               if var11.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('Fattyfish','vitaminD,fat'))
                   lbsnacks.insert(tk.END,('Fattyfish','vitaminD,fat'))
                   fats.configure(bg="green")
                   check11.deselect()
                   p1.lift()
                   root1.destroy()
               if var12.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   lbsnacks.insert(tk.END,('liver','vitmnB6,vitmnA,vitmnC,fat'))
                   vitaminsA.configure(bg="green")
                   check12.deselect()
                   p1.lift()
                   root1.destroy()
               if var13.get()==1:
                   cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   lbsnacks.insert(tk.END,('greenvegetables','Fe,Ca,vitmnC,vitmnE,vitmnK'))
                   vitaminsA.configure(bg="green")
                   check13.deselect()
                   p1.lift()
                   root1.destroy()
               
               con.commit()
               con.close()
        

           def des():
               check1.deselect()
               
           global menu
           def menu():
               global root1
               root1=tk.Tk()
               root1.geometry('300x350')
               root1.resizable(width=False, height=False)
               check10=tk.Checkbutton(root1, text='Breakfast', state='normal',command=add2break)
               check10.place(x=20,y=60)
               check11=tk.Checkbutton(root1, text='Lunch', state='normal',command=add2lunch)
               check11.place(x=20,y=90)
               check12=tk.Checkbutton(root1, text='Super', state='normal',command=add2super)
               check12.place(x=20,y=120)
               check13=tk.Checkbutton(root1, text='Snacks', state='normal',command=add2snacks)
               check13.place(x=20,y=150)
               root1.mainloop()




           #carbohydrates
           #carbohydrates
           var1=tk.IntVar()
           check1=tk.Checkbutton(self, text='Posho(K,Na,Fats)', state='normal',variable=var1,onvalue = 1, offvalue = 0,command=menu)
           check1.place(x=20,y=60)#command=add_break
           var2=tk.IntVar()
           check2=tk.Checkbutton(self, text='Nyasa(Na,VitaminC,Fe)', state='normal',variable=var2,onvalue = 1, offvalue = 0,command=menu)
           check2.place(x=20,y=80)
           var3=tk.IntVar()
           check3=tk.Checkbutton(self, text='Sugarcane(Mg,Zn,Ca,Fe,K)', state='normal',variable=var3,onvalue = 1, offvalue = 0,command=menu)
           check3.place(x=20,y=100)
           var4=tk.IntVar()
           check4=tk.Checkbutton(self, text='Sweetpotatoes(vitmnA,vitmnB,vitmnC,Mg,Cu,K,Po)', state='normal',variable=var4,onvalue = 1, offvalue = 0,command=menu)
           check4.place(x=20,y=120)

           #proteins
           var5=tk.IntVar()
           check5=tk.Checkbutton(self, text='chicken(vitmnB, K ,Po)', state='normal',variable=var5,onvalue = 1, offvalue = 0,command=menu)
           check5.place(x=20,y=220)
           var6=tk.IntVar()
           check6=tk.Checkbutton(self, text='beans(vitmnC ,vitmnB6,Cu,K,Po,Mg)', state='normal',onvalue = 1, offvalue = 0,variable=var6,command=menu)
           check6.place(x=20,y=240)
           var7=tk.IntVar()
           check7=tk.Checkbutton(self, text='eggs(fat,Fe,vitamins,minerals)', state='normal',onvalue = 1, offvalue = 0,variable=var7,command=menu)
           check7.place(x=20,y=260)
           var8=tk.IntVar()
           check8=tk.Checkbutton(self, text='beef(Zn,Fe,vitaminB12)', state='normal',variable=var8,onvalue = 1, offvalue = 0,command=menu)
           check8.place(x=20,y=280)

           #fats
           var9=tk.IntVar()
           check9=tk.Checkbutton(self, text='ovaccado', state='normal',variable=var9,onvalue = 1, offvalue = 0,command=menu)
           check9.place(x=20,y=380)
           var10=tk.IntVar()
           check10=tk.Checkbutton(self, text='gnuts', state='normal',variable=var10,onvalue = 1, offvalue = 0,command=menu)
           check10.place(x=20,y=412)
           var11=tk.IntVar()
           check11=tk.Checkbutton(self, text='Fattyfish', state='normal',variable=var11,onvalue = 1, offvalue = 0,command=menu)
           check11.place(x=20,y=452)

           #vitamins
           var12=tk.IntVar()
           check12=tk.Checkbutton(self, text='liver(Zn,Fe,vitaminB12,Cu,Mg)', state='normal',variable=var12,onvalue = 1, offvalue = 0,command=menu)
           check12.place(x=20,y=560)
           var13=tk.IntVar()
           check13=tk.Checkbutton(self, text='greenvegetables(Fe,vitaminA,C&K)', state='normal',variable=var13,onvalue = 1, offvalue = 0,command=menu)
           check13.place(x=20,y=600)
           #choose
           #dicta={check1:var1,check2:var2,check3:var3,check4:var4,check5:var5,check6:var6,check7:var7,check8:var8,check9:var9,check10:var10,check11:var11,check12:var12,check13:var13}

    class Page3(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
##           canvas = tk.Canvas(self)
##           canvas.pack()
           image1 = tk.PhotoImage(master=self, file="price.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1     

           
           label = ttk.Label(self, text="Enter the amount of money you have :", font='times 12')
           label.place(x=50,y=50)
           label2 = ttk.Label(self, text="Meal1", font='times 12')
           label2.place(x=300,y=73)
           lbfoods=tk.Listbox(self, width=100)
           lbfoods.place(x=300,y=100,width=290)
           global priceno
           priceno=tk.StringVar()
           price=tk.Entry(self,textvariable=priceno)
           price.place(x=300,y=50,width=290)
           def findit(priceno=0):
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               cur.execute("SELECT * FROM PRICE1 WHERE AMOUNT <= ?",(priceno,))
               rows=cur.fetchall()
               con.close()
               return rows

           def search_command():
               lbfoods.delete(0,tk.END)
               for row in findit(priceno.get()):
                   lbfoods.insert(tk.END,row)
               



           search = ttk.Button(self, text="search",command=search_command)
           search.place(x=700,y=50,width=60)
           

    class Page4(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)


    class Page5(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           #label = ttk.Label(self, text="This is page 5")
           #label.pack(side="right", fill="both", expand=True)
           


           


    class Page6(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 6")
           label.pack(side="right", fill="both", expand=True)

    class Page7(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 7")
           label.pack(side="right", fill="both", expand=True)

    class Page8(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 7")
           label.pack(side="right", fill="both", expand=True)


    class Page9(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 7")
           label.pack(side="right", fill="both", expand=True)


    class Page10(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           #label = ttk.Label(self, text="This is page 7")
           #label.pack(side="right", fill="both", expand=True)
##           canvas = tk.Canvas(self)
##           canvas.pack()
           image1 = tk.PhotoImage(master=self, file="homepage.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1
           def mouthinfo():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))


               root = tk.Tk()


               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               canvas.bind('<Configure>', on_configure)


           

               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               cw = tk.Label(frame,justify=tk.LEFT, font="Times 15",bg='indigo',fg='white',text="""How to Prevent Mouth Problems During Cancer Treatment\nTo help prevent or minimize mouth problems, consider these tips:\nSee your dentist.\n Try to see your dentist before treatment begins, so he or she can conduct a thorough teeth cleaning and check for potential sources of dental irritation that may cause problems during cancer treatment. Once treatment begins, be sure to see your dentist again so he or she can watch for any potential issues.
               \n•	Maintain good oral health to help prevent infection and tooth decay.\nBrush three times a day with a soft toothbrush, floss daily, and eat a healthy diet low in sugar. (However, don’t floss if it causes bleeding when your platelet count is low.)
               \n•	To help lessen the symptoms of mouth sores (also called mucositis),\nask for ice chips or sugar-free popsicles to suck on while you receive chemotherapy.\n Research shows that this may help decrease mouth sores.
               \n•	Talk with your doctor. He or she may be able to prescribe a medication to help prevent sores and ease discomfort.\nYour doctor may also recommend over-the-counter pain relievers, such as Tylenol, to help reduce mouth pain.
               \n•	Avoid commercial mouthwashes, because they contain alcohol that may burn your mouth.\nInstead, rinse your mouth with warm salt water or baking soda and water (a teaspoon of either dissolved in eight ounces of warm water).
               \n•	Avoid spicy meals and foods that are difficult to chew.\nCitrus and tomato juice may also irritate your mouth when you have mouth sores\n•	Drink at least eight glasses of water or juices daily. Drinking fluids throughout the day can help with dry mouth (also called xerostomia). It is also important to avoid caffeinated beverages, because caffeine can increase mouth.
               \nRadiation therapy, chemotherapy, and several cancer medications can cause mouth sores, ulcers, and tender gums\n.All can cause your mouth, throat, and tongue to feel sore, raw,\ndry and may lead to dehydration, poor eating, and weight loss\n.The following tips and recommendations may help\n you to manage sore mouth, throat, and tongue.\nChoose soft, bland foods.\nSofter foods will be easier to chew and swallow\n.Soups and stews are good options, as long as meats are soft and tender\n.Try breakfast foods like instant oatmeal, grits, pancakes, waffles, and cold \ncereal that has been softened in milk.\nPick side dishes like cottage or ricotta cheese, macaroni \nand cheese, mashed white or sweet potatoes, and rice or risotto\n.Try desserts like custard, tapioca pudding, ice cream\n, milkshakes, and sherbet\nChoose snacks like applesauce, gelatin, smoothies, and yogurt.\nPrepare foods in ways that make them easier to eat\nCut foods into small pieces.\nYou may consider using a blender or\n food processor to puree foods.\nCook foods until they are soft and tender.\nServe foods with gravy, broths, or sauces.\nChoose soft or canned fruits or applesauce instead of raw fruits with tough skins.\nAvoid foods and drinks that make mouth sores worse.\nAvoid citrus fruits and juices, salty or spicy foods, and acidic foods like tomatoes.\nDo not drink carbonated or caffeinated drinks.\nRefrain from having beer, wine, liquor, or any other type of alcohol.nAvoid very hot foods.\nHot foods can cause mouth and throat discomfort.\nChoose room temperature or cold foods that are soothing.\nAllow soups and hot foods to cool to room temperature before serving\nTry freezing fruits, and suck on frozen fruit pops, fruit ices, or ice chips.\nChoose foods that are good sources of protein to combat weight loss.\nAim to have a good source of protein with meals and snacks.\nGround meats, eggs, cottage cheese, yogurt, custard, beans, lentils, and smoothies are \ngood soft food choices that also provide protein.\nEat small, frequent meals. You may find it easier to eat smaller amounts at a time.\nDrink at least 8-10 eight-ounce glasses of water each day.\nDrink liquids with your meals as this will make it easier to swallow foods.\nSip cool drinks in between your meals.\nDrink with a straw. This can help push the foods past the painful sores in your mouth.\nAvoid caffeinated or/and carbonated beverages.\nAvoid alcohol. Alcohol can irritate the mouth.\nUse good mouth care.\nRinse your mouth several times a day.\n Mix one quart water and one tablespoon baking soda to\n make a rinse that removes food and promotes healing.\nDo not use a mouthwash that has alcohol. Alcohol makes a sore mouth worse.\nUse a toothbrush with soft bristles.\nRemove dentures (except during eating) if your gums are sore. Keep dentures clean\nAvoid cigarettes, cigars, and tobacco products\nAsk your doctor about special mouthwashes and sprays that can numb the mouth and throat\nTell your doctor if your gums are bleeding or if you have white \npatches in your mouth. Both can be signs of infection.\n """)

               cw.pack(padx=2, pady=2, fill=tk.BOTH)





               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()

               
           def mouth():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               label1=ttk.Label(root,text="POSTMOUTH DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label1.place(x=720,y=70)
               buton1=tk.Button(root,text="more info",bg="white",font="Times 20",fg="black",relief="raised")
               buton1.place(x=720,y=700)
              
               def menu():
                   global root1
                   root1=tk.Tk()
                   root1.geometry('300x350')
                   root1.resizable(width=False, height=False)
                   check10=tk.Checkbutton(root1, text='Breakfast', state='normal',command=add2break)
                   check10.place(x=20,y=60)
                   check11=tk.Checkbutton(root1, text='Lunch', state='normal',command=add2lunch)
                   check11.place(x=20,y=90)
                   check12=tk.Checkbutton(root1, text='Super', state='normal',command=add2super)
                   check12.place(x=20,y=120)
                   check13=tk.Checkbutton(root1, text='Snacks', state='normal',command=add2snacks)
                   check13.place(x=20,y=150)
                   root1.mainloop()
               var56=tk.IntVar()
               check56=tk.Checkbutton(root, text="fatmilk",variable=var56,onvalue = 1, offvalue = 0,command=menu).place(x=720,y=100)

               def add2break():
               
                   con=sqlite3.connect("diet.db")
                   cur=con.cursor()
                   if var56.get()==1:
                       cur.execute("INSERT INTO BREAKFAST VALUES (NULL,?,?)",("fatmilk","Fats"))
                       lbbreakfast.insert(tk.END,("fatmilk","Fats"))
                       carbohydrates.configure(bg="green")
                       #check56.deselect()
                       #p1.lift()
                       root1.destroy()

               def add2lunch():
                   con=sqlite3.connect("diet.db")
                   cur=con.cursor()
                   if var56.get()==1:
                       cur.execute("INSERT INTO LUNCH VALUES (NULL,?,?)",("fatmilk","Fats"))
                       lblunch.insert(tk.END,("fatmilk","Fats"))
                       carbohydrates.configure(bg="green")
                       #check1.deselect()
                       #p1.lift()
                       root1.destroy()
               def add2super():
                   con=sqlite3.connect("diet.db")
                   cur=con.cursor()
                   if var56.get()==1:
                       cur.execute("INSERT INTO SUPER VALUES (NULL,?,?)",("fatmilk","Fats"))
                       lbsuper.insert(tk.END,("fatmilk","Fats"))
                       carbohydrates.configure(bg="green")
                       #check1.deselect()
                       #p1.lift()
                       root1.destroy()
               def add2snacks():
                   con=sqlite3.connect("diet.db")
                   cur=con.cursor()
                   if var56.get()==1:
                       cur.execute("INSERT INTO SNACKS VALUES (NULL,?,?)",("fatmilk","Fats"))
                       lbsnacks.insert(tk.END,("fatmilk","Fats"))
                       carbohydrates.configure(bg="green")
                       root1.destroy()





               
            
            
            
            

               canvas.bind('<Configure>', on_configure)
               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               logo3=tk.PhotoImage(file="with mouthproblem.gif")#gif/.pmb
               var56=tk.IntVar()
               check56=tk.Checkbutton(root, text="fatmilk",variable=var56,onvalue = 1, offvalue = 0,command=menu).place(x=720,y=100)
               var57=tk.IntVar()
               check57=tk.Checkbutton(root, text="wheatbread",variable=var57,onvalue = 1, offvalue = 0).place(x=720,y=150)
               var58=tk.IntVar()
               check58=tk.Checkbutton(root, text="brown rice",variable=var58,onvalue = 1, offvalue = 0).place(x=720,y=200)
               var59=tk.IntVar()
               check59=tk.Checkbutton(root, text="Orange",variable=var59,onvalue = 1, offvalue = 0).place(x=720,y=250)
               buton1=tk.Button(root,text="more info",bg="white",font="Times 20",fg="black",relief="raised",command=mouthinfo)
               buton1.place(x=720,y=700)
            

            
            
               w5=ttk.Label(frame,text="foods eaten to prevent malaria",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w6=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo3,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               label2=ttk.Label(root,text="HEALTHMOUTH DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label2.place(x=720,y=450)
               var60=tk.IntVar()
               check1=tk.Checkbutton(root, text="Raw galic",variable=var60,onvalue = 1, offvalue = 0).place(x=720,y=500)
               var61=tk.IntVar()
               check1=tk.Checkbutton(root, text="Mashroom",variable=var61,onvalue = 1, offvalue = 0).place(x=720,y=550)
               var62=tk.IntVar()
               check1=tk.Checkbutton(root, text="Carrots",variable=var62,onvalue = 1, offvalue = 0).place(x=720,y=600)
               var63=tk.IntVar()
               check1=tk.Checkbutton(root, text="frozen vegetables",variable=var63,onvalue = 1, offvalue = 0).place(x=720,y=650)

               logo4=tk.PhotoImage(file="healthmouth.gif")#gif/.pmb
            
               w7=ttk.Label(frame,text="foods eaten to avoid mouthproblems",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w8=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()   
           def eyeinfo():
               
               def on_configure(event):
                    canvas.configure(scrollregion=canvas.bbox('all'))


               root = tk.Tk()


               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

            
               canvas.bind('<Configure>', on_configure)


            

               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               cw = tk.Label(frame,justify=tk.LEFT, font="Times 15",bg='indigo',fg='white',text="""Eye Safety
               The eyes, among our most important external organs, are also\n among our most vulnerable and eyes must remain moist to avoid\n irritation; it is also much more sensitive to abrasion and contact with foreign substances.long-term eye injuries can occur if appropriate eye safety measures are not taken. most of these safety considerations are simple and easy to adopt on a daily basis.
               \n•	Safety EyeTips
               \n•	Always handle sharp objects, including knives, scissors,\nand even pencils, with extreme care. Never point them at your\nface or someone else's, and do not allow small children to have access to them.
               \n•	Supervise children’s activities and select toys for them \nthat have no sharp, pointy ends or high velocity projectiles.\n
               \n•	Prepare a well-lit environment whenever you read, write,or\n engage in any activity that requires extended use of the eyes\n. If necessary, wear eyeglasses or contacts of the correct prescription.
               \n•	Know essential first aid steps to take in the event of various\n eye injuries, including how best to flush them with water \nand under what circumstances it is necessary to do so.
               \n•	Have regular eye examination schedule a special one if you notice\n any persistent and unexplained irritation.
               \n•	Always wear proper eye protection, taking special care when working\n with chemicals or power tools or engaging in hobbies \ninvolving small pieces of material.
               \n•	Wear eye safety gear and helmets as appropriate when participating in\n sports, particularly those involving small balls,\nsuch as racquetball. If you have undergone LASIK or another type of refractive surgery, it is especially important to wear eye protection.
               \n•	Sunglasses are crucial for preventing long-term sun damage to the eyes.\n Be sure to select and wear those that block both\n ultraviolet A and ultraviolet B radiation from the sun.
               \n•	Avoid looking directly at the sun, especially during an eclipse.\n
               \n•	Household chemical spray bottles should never be pointed at your face.\nKeep them at arm’s length whenever you spray them.
               \n•	Store dangerous chemicals in a safe, stable location to avoid spills\n and splashes.
               \n•	Wash your hands after using any chemicals so that you do not accidentally\n rub them into your eyes.
               \n•	Never remove protective guards from power tools.
               \n•	Wear protective equipment, including seatbelts in cars and helmets when\n bicycling or skating.
               \nTalk to an Eye Doctor for More Information


               """)

               cw.pack(padx=2, pady=2, fill=tk.BOTH)





               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()
                
               
           def eye():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)
               buton1=tk.Button(root,text="more info",bg="white",font="Times 20",fg="black",relief="raised",command= eyeinfo)
               buton1.place(x=720,y=700)


               label1=ttk.Label(root,text="EYESIGHT DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label1.place(x=720,y=70)
               var14=tk.IntVar()
               check1=tk.Checkbutton(root, text="Carrot",variable=var14,onvalue = 1, offvalue = 0).place(x=720,y=100)
               var15=tk.IntVar()
               check1=tk.Checkbutton(root, text="Chickpeas",variable=var15,onvalue = 1, offvalue = 0).place(x=720,y=150)
               var16=tk.IntVar()
               check1=tk.Checkbutton(root, text="rawtomatoes",variable=var16,onvalue = 1, offvalue = 0).place(x=720,y=200)
               var17=tk.IntVar()
               check1=tk.Checkbutton(root, text="Boiled egg",variable=var17,onvalue = 1, offvalue = 0).place(x=720,y=250)



               canvas.bind('<Configure>', on_configure)
               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               logo3=tk.PhotoImage(file="witheyeproblem.gif")#gif/.pmb
               #moto3="""Foods Good for Your Eyes\nTomatoes,carrots,mangoes\nlean meat poutry\nlegumes such as beans\n,peas for sharpening\n your vision,enhancement of your retina\nand reduce eye problems\n"""
               w5=ttk.Label(frame,text="foods eaten to prevent eyedefects",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w6=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo3,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               label2=ttk.Label(root,text="HEALTHYEYES DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label2.place(x=720,y=400)
               var18=tk.IntVar()
               check1=tk.Checkbutton(root, text="Lean meat",variable=var18,onvalue = 1, offvalue = 0).place(x=720,y=450)
               var19=tk.IntVar()
               check1=tk.Checkbutton(root, text="Beans",variable=var19,onvalue = 1, offvalue = 0).place(x=720,y=500)
               var20=tk.IntVar()
               check1=tk.Checkbutton(root, text="Mango",variable=var20,onvalue = 1, offvalue = 0).place(x=720,y=550)
               var21=tk.IntVar()
               check1=tk.Checkbutton(root, text="Sukuma wiki",variable=var21,onvalue = 1, offvalue = 0).place(x=720,y=600)



               logo4=tk.PhotoImage(file="no eyeproblem.gif")#gif/.pmb
               #moto4="""Tips to keep your teeth health\ntake boiled eggs to boost the amount\nof protective pigment in the macula, the part\n of your eye that controls central\nvision.,chickpeas containa low-fat\n high-fiber option to help keep \nyour vision sharp at night,vegatables\n like sukuma wiki,,nakati \nare good for eye pigment \ndevelopment in additition\n to carrots and thus better \neye sight"""
               w7=ttk.Label(frame,text="foods eaten to keep health eyesight",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w8=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()


            

           def typhoidinfo():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))


               root = tk.Tk()

                

               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)
               canvas.bind('<Configure>', on_configure)
               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               cw = tk.Label(frame,justify=tk.LEFT, font="Times 15",bg='indigo',fg='white',text="""Typhoid fever is a bacterial infection that can spread throughout the body,\n affecting many organs. Without prompt treatment, it can cause serious complications\n and can be fatal.
               \nIt's caused by a bacterium called Salmonella typhi,\nwhich is related to the bacteria that cause salmonella .\nTyphoid fever is highly contagious. An infected person can pass the bacteria out of their body in their poo (stools) or, less commonly, in their pee (urine).
               \nIf someone else eats food or drinks water that's been contaminated with a small amount of infected poo or urine\n, they can become infected with the bacteria and develop typhoid fever.
               \nWho's affected?\nTyphoid fever is most common in parts of the world that have poor sanitation and limited access to clean water.\nWorldwide, children are thought to be most at risk of developing typhoid fever.
               \nThis may be because their immune system (the body's natural defence against infection and illness) is still developing.\n\nBut children with typhoid fever tend to have milder symptoms than adults.\n
               \nTyphoid fever is uncommon in the UK, with an estimated 500 cases occurring each year.\nIn most of these cases, the person developed the infection while visiting relatives in Bangladesh, India or Pakistan.
               \nSymptoms of typhoid fever\nThe main symptoms of typhoid fever are:\n•	a high temperature that can reach 39 to 40C\n•	general aches and pains\n•	cough\n•	constipation\nAs the infection progresses, you may lose your appetite, feel sick, and have a  diaheorria Some people may develop a rash.
               \nIf typhoid fever isn't treated, the symptoms will continue to get worse over the following weeks and \nthe risk of developing potentially fatal complications will increase.
               \nHow typhoid fever is treated\nTyphoid fever requires prompt treatment with antibiotics.\nIf typhoid fever is diagnosed early, the infection is likely to be mild and can usually be \ntreated at home with a 7- to 14-day course of antibiotic tablets.\n
               \nMore serious cases of typhoid fever usually require admission to hospital so antibiotic injections can be given\nWith prompt antibiotic treatment, most people will start to feel better within a few days and serious complications are very rare.
               \nDeaths from typhoid fever are now virtually unheard of in the UK.\nIf typhoid fever isn't treated, it's estimated that up to 1 in 5 people with the condition will die.
               \nSome of those who survive will have complications caused by the infection.\nTyphoid fever vaccination\nThese involve either having a single injection or taking 3 capsules over alternate days.\n
               \nVaccination is recommended for anyone planning to travel to parts of the world where typhoid fever is widespread.\nIt's particularly important if you're planning to live or work closely with local people.
               \nBut as neither vaccine offers 100% protection, it's also important to follow some precautions when travelling.\nFor example, you should only drink bottled or boiled water, and you should avoid foods that could potentially be contaminated\n.
               \nHigh-risk areas\n\The areas with the highest rates of typhoid fever are:\n•	the Indian subcontinent\n•	Africa\n•	south and southeast Asia\n•	South America\n

               """)
               cw.pack(padx=2, pady=2, fill=tk.BOTH)





               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()



               
           def typhoid():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               label2=ttk.Label(root,text="POSTTYPHOID DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label2.place(x=720,y=70)
               buton1=tk.Button(root,text="more info",bg="white",font="Times 20",fg="black",relief="raised",command=typhoidinfo)
               buton1.place(x=720,y=700)

               var22=tk.IntVar()
               check1=tk.Checkbutton(root, text="Barley water",variable=var22,onvalue = 1, offvalue = 0).place(x=720,y=100)
               var23=tk.IntVar()
               check1=tk.Checkbutton(root, text="Fortified water",variable=var23,onvalue = 1, offvalue = 0).place(x=720,y=150)
               var64=tk.IntVar()
               check1=tk.Checkbutton(root, text="Buttermilk",variable=var64,onvalue = 1, offvalue = 0).place(x=720,y=200)
               var24=tk.IntVar()
               check1=tk.Checkbutton(root, text="frozen nakati",variable=var24,onvalue = 1, offvalue = 0).place(x=720,y=250)

            

               canvas.bind('<Configure>', on_configure)
               frame2 = tk.Frame(canvas)
               frame2.configure(bg="indigo")
               canvas.create_window(90,90, window=frame2, anchor='nw')
               logo4=tk.PhotoImage(file="typhoidpatient.gif")#gif/.pmb
               #moto4="""Adiet for typhoid patients \nshould be one that islight \nand easy to digest. Keep in\n mind that a patient who\n has typhoid has a low appetite.\nFluids in the form of tender\ncoconut water, barley water\nelectrolyte fortified water\nfresh fruit juice,vegetable soup,buttermilk and water\nshould be consumed until \nbody temperature comes\n back to normal"""
               w6=ttk.Label(frame2,text="foods eaten to prevent typhoid",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w6=tk.Label(frame2,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               label2=ttk.Label(root,text="PRETYPHOID DEIT",background="red",foreground="blue",font=("Helvetica 15"))#label
               label2.place(x=720,y=450)
               var25=tk.IntVar()
               check1=tk.Checkbutton(root, text="Boiled clean water",variable=var25,onvalue = 1, offvalue = 0).place(x=720,y=500)
               var26=tk.IntVar()
               check1=tk.Checkbutton(root, text="Coconut water",variable=var26,onvalue = 1, offvalue = 0).place(x=720,y=550)
               var27=tk.IntVar()
               check1=tk.Checkbutton(root, text="Yorghut",variable=var27,onvalue = 1, offvalue = 0).place(x=720,y=600)
               var28=tk.IntVar()
               check1=tk.Checkbutton(root, text="Boiled fish",variable=var28,onvalue = 1, offvalue = 0).place(x=720,y=650)

            
               logo5=tk.PhotoImage(file="pretyphoid.gif")#gif/.pmb
               #moto5="""Tips to avoid typhoid\n Drink boiled water.and \nkeep your body hydrated\n.Consume 3 – 4 liters of fluids in\n the form of water,\n fruit juices, tender coconut water\n and soup.\nEat small frequent meals \nrather than large meals to ease\n digestion and for maximum\n nutrient utilization by the body\n.Try not to include spices as\n much as possible till the fever\n recovers.take eggs,yoghut\nand boiledfishdepending on your \ntolerance level"""
               w9=ttk.Label(frame2,text="foods eaten to avoid typhoid",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w10=tk.Label(frame2,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo5,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()
           def moreinfo():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()


               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)


               canvas.bind('<Configure>', on_configure)


               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               cw = tk.Label(frame,justify=tk.LEFT, font="Times 15",bg='indigo',fg='white',text="""Malaria is a mosquito-borne disease caused by a parasite./n People with malaria often experience fever, chills, and flu-like illness. Left untreated, they may develop severe complications and die. In 2016 an estimated 216 million cases of malaria occurred worldwide and 445,000 people died, mostly children in the African Region. About 1,700 cases of malaria are diagnosed in the United States each year. The vast majority of cases in the United States are in travelers and immigrants returning from countries where malaria transmission occurs, many from sub-Saharan Africa and South Asia.
               \nPrevention
               \nThere's a significant risk of getting malaria if you travel to an affected area\n It's very important you take precautions to prevent the disease.
               \nMalaria can often be avoided using the ABCD approach to prevention, which stands for:\n
               \n•	Awareness of risk – find out whether you're at risk of getting malaria.\n
               \n•	Bite prevention – avoid mosquito bites by using insect repellent,\n covering your arms and legs, and using a mosquito net.
               \n•	Check whether you need to take malaria prevention tablets – if you do,\n make sure you take the right antimalarial tablets at the right dose, and finish the course.
               \n•	Diagnosis – seek immediate medical advice if you have malaria symptoms,\n including up to a year after you return from travelling.
               \nThese are outlined in more detail below.\nBeing aware of the risks\nTo check whether you need to take preventative malaria treatment for the countries you're visiting, website.
               \nIt's also important to visit your GP or local travel clinic for malaria \nadvice as soon as you know where you're going to be travelling.\nEven if you grew up in a country where malaria is common, you still need to take precautions to protect yourself from infection if you're travelling to a risk area.
               \nNobody has complete immunity to malaria, and any level of natural protection \nyou may have had is quickly lost when you move out of a risk area.\nPreventing bites\n•	Stay somewhere that has effective air conditioning and screening on doors/n and windows ormake sure doors and windows close properly./n•	Sleep under an intact mosquito net that's been treated with insecticide.
               \n•	Use insect repellent (DEET)on your skin and in sleeping environments./n Remember to reapply it frequently. The most effective repellents contain diethyltoluamide (DEET) and are available in sprays, roll-ons, sticks and creams.
               \n•	Wear light, loose-fitting trousers rather than shorts, and wear shirts with long sleeves.\n This is particularly important during early evening and at night, when mosquitoes prefer to feed.
               \n•	Tea tree oils or bath oils offer any protection against mosquito bites.\nAntimalarial tablets
               \nThere's currently no vaccine available that offers protection againsmalaria,so it's very important\n to take antimalarial medication to reduce your chances of getting the disease.
               \nHowever, antimalarials only reduce your risk of infection by about 90%, so taking steps to avoid bites is also important.\nWhen taking antimalarial medication:\n•	make sure you get the right antimalarial tablets before you go/ncheck with your GP or pharmacist if you're unsure
               \n•	follow the instructions included with your tablets carefully\n•	depending on the type you're taking, continue to take your tablets for up to four weeks after returning from your trip to cover the incubation period of the disease
               \n•	take medicine, such as Warfarin, to prevent blood clots\n•	use combined hormonal contraception, such as ceneptives 
               \n•	If you've taken antimalarial medication in the past, don't assume it's suitable for future trips.\n The antimalarial you need to take depends on which strain of malaria is carried by the mosquitoes and whether they're resistant to certain types of antimalarial medication.
               \nGet immediate medical advice
               \nYou must seek medical help straight away if you become ill while travelling in an area where malaria is found/n, or after returning from travelling, even if you've been taking antimalarial tablets.
               \nMalaria can get worse very quickly, so it's important that it's diagnosed and treated as soon as possible.\nIf you develop symptoms of malaria while still taking antimalarial tablets, either while you're travelling or in the days and weeks after you return, remember to tell the doctor which type you have been taking. The same type of antimalarial shouldn't be used to treat you as well.
               \nIf you develop symptoms after returning home, visit your GP or a hospital doctor and tell them which countries\n you've travelled to in the last 12 months, including any brief stopovers.
               \nDEET insect repellents\nThe chemical DEET is often used in insect repellents. It's not recommended for babies who are less than two months old.\nDEET is safe for older children, adults and pregnant women if you follow the manufacturer's instructions:
               \n•	use on exposed skin\n•	don't spray directly on to your face – spray into your hands and pat on to your face\n•	avoid contact with lips and eyes\n•	wash your hands after applying/n•	don't apply to broken or irritated skin
               \n•	make sure you apply DEET after applying sunscreen, not before""")

               cw.pack(padx=2, pady=2, fill=tk.BOTH)





               root.geometry('920x750')
               root.configure(bg="indigo")
               root.mainloop()
           def malaria():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
                
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               label1=ttk.Label(root,text="POSTMALARIA DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label1.place(x=720,y=70)    
               buton1=tk.Button(root,text="more info",bg="white",font="Times 20",fg="black",relief="raised",command=moreinfo)
               buton1.place(x=720,y=700)
               var29=tk.IntVar()
               check1=tk.Checkbutton(root, text="Apple",variable=var29,onvalue = 1, offvalue = 0).place(x=720,y=100)
               var30=tk.IntVar()
               check1=tk.Checkbutton(root, text="Berrie",variable=var30,onvalue = 1, offvalue = 0).place(x=720,y=150)
               var31=tk.IntVar()
               check1=tk.Checkbutton(root, text="Orange juice",variable=var31,onvalue = 1, offvalue = 0).place(x=720,y=200)
               var32=tk.IntVar()
               check1=tk.Checkbutton(root, text="passion juice",variable=var32,onvalue = 1, offvalue = 0).place(x=720,y=250)

               canvas.bind('<Configure>', on_configure)
               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               logo3=tk.PhotoImage(master=canvas,file="postmalaria.gif")#gif/.pmb
               #moto3="""Malaria is a protozoal \ndisease,which is associated\n with high grade fever \nand is often transmitted \nby female Anopheline mosquito\n bites.The mosquito transport\n the parasite from one \ninfected human to another.\n These parasites then enter \nthe blood stream and infecting \nthe red blood cells.\nThe main symptoms of\n malaria are fever, chills,\n headache, nausea \nand vomiting, etc.’There \nis no specific diet for malaria\n but adequate nutrition \nis the key for improvement.\nA good diet should focus\n on strengthening the patient’s\n immune system without \naffectingliver, kidney and \ndigestive system"""
               w5=ttk.Label(frame,text="foods eaten to prevent malaria",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w6=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo3,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               label2=ttk.Label(root,text="PRE-MALARIA DIET",background="red",foreground="blue",font=("Helvetica 15"))#label
               label2.place(x=720,y=450)
               var33=tk.IntVar()
               check1=tk.Checkbutton(root, text="Watermelon",variable=var33,onvalue = 1, offvalue = 0).place(x=720,y=500)
               var34=tk.IntVar()
               check1=tk.Checkbutton(root, text="Ripebanana",variable=var34,onvalue = 1, offvalue = 0).place(x=720,y=550)
               var35=tk.IntVar()
               check1=tk.Checkbutton(root, text="Pear",variable=var35,onvalue = 1, offvalue = 0).place(x=720,y=600)
               var36=tk.IntVar()
               check1=tk.Checkbutton(root, text="Pawpaw",variable=var36,onvalue = 1, offvalue = 0).place(x=720,y=650)

            
               logo4=tk.PhotoImage(file="premalaria.gif")#gif/.pmb
               #moto4="""Fruits such as oranges \nand pears also add antibodies \nto fight against malariaparasites\nsleep under a mosquitonet \nalso sleep under a mosquitonet\n"""
               w7=ttk.Label(frame,text="foods eaten to avoid malaria",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w8=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)
               root.geometry('920x750')
               root.configure(bg="indigo")


               root.mainloop()   


            





            
           buton1=tk.Button(self,text="Malaria",bg="white",font="Times 20",fg="black",relief="raised",command=malaria)
           buton1.place(x=220,y=140)


           buton2=tk.Button(self,text="Typhoid",bg="white",font="Times 20",fg="black",relief="raised",command=typhoid)
           buton2.place(x=220,y=200)


           buton3=tk.Button(self,text="Eyesdiseases",bg="white",font="Times 20",fg="black",relief="raised",command=eye)
           buton3.place(x=220,y=260)


           buton4=tk.Button(self,text="Mouthproblems",bg="white",font="Times 20",fg="black",relief="raised",command=mouth)
           buton4.place(x=220,y=320)




    class Page11(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           #label = ttk.Label(self, text="This is page 7")
           #label.pack(side="right", fill="both", expand=True)
##           canvas = tk.Canvas(self)
           
           image1 = tk.PhotoImage(master=self, file="BACKGR.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1

           def weightgain():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               canvas.bind('<Configure>', on_configure)
               frame = tk.Frame(canvas)
               frame.configure(bg="indigo")
               canvas.create_window(90,90, window=frame, anchor='nw')
               w = tk.Scrollbar(root,orient='vertical')
               wg=tk.Button(frame,text="<<<WEIGHT MONITOR>>>",font='times 15', foreground = 'purple',background='green').pack(side='top',fill=tk.BOTH,expand=True)

               buton5=tk.Button(frame,text="food list for weight gain",bg="white",font="Times 20",fg="black",relief="raised",command=foodlistgain)
               buton5.pack(side='top')

               logo3=tk.PhotoImage(file="wloss.gif")#gif/.pmb
           
               moto3="""1. Whole Eggs \n
           Once feared for being high in cholesterol,\nwhole eggs have been making a comeback.\nNew studies show that they don't\nadversely affect blood cholesterol and don't\ncause heart attacks.
           they are among the best foods\nyou can eat if you need to lose weight.\nThey're high in protein, healthy fats,\n and can make you feel full with a\nvery low amount of calories.\nEggs are also incredibly nutrient dense\n and can help you get all the nutrients\nyou need on a calorie restricted diet.\nAlmost all the nutrients are found in\nthe yolks.
           """
               w5=ttk.Label(frame,text="EGGS",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w6=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo3,text=moto3,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)#image=logo3
               logo4=tk.PhotoImage(file="Capture.PNG")#gif/.pmb
               moto4="""2. Drink Coffee.
           Coffee has many benefits for health \nand sports performance — and may also help \ndecrease your appetite.
           Rzarch shows that coffee increases \nthe release of peptide YY (PYY). This hormone \nis produced in the gut in response to eating \nand promotes a feeling of fullness \n
           decffeinated coffee may produce the highest\n reduction in hunger"""
               w7=ttk.Label(frame,text="DRINKS",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w8=tk.Label(frame,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,text=moto4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)#,image=logo4
               root.geometry('920x750')
               root.configure(bg="indigo")
               root.mainloop()   


           def weightloss():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               canvas.bind('<Configure>', on_configure)
               frame2 = tk.Frame(canvas)
               frame2.configure(bg="indigo")
               canvas.create_window(90,90, window=frame2, anchor='nw')
               w = tk.Scrollbar(root,orient="vertical")
               logo4=tk.PhotoImage(file="wgain.png")#gif/.pmb
               moto4="""1. Boiled Potatoes\nThey have several properties that make \nthem a perfect food, both for weight loss \nand optimal health.They contain an incredibly diverse range \nof nutrients, a little bit of almost everything \nwe need.There have even been accounts of \npeople living on nothing but potatoes alone \nfor extended periods of time.They are particularly high in potassium,\n a nutrient that most people don't get \nenough of and plays an important role in \nblood pressure control.\nIf you boil the potatoes, \nthen allow them to cool for a while, \nthen they will form large amounts of resistant starch,\n a fiber-like substance that has been shown to \nhave all sorts of health benefits\nincluding weight loss (22).Sweet potatoes,\n turnips and other root vegetables \nare also excellent."""

               wg=tk.Button(frame2,text="<<<WEIGHT MONITOR>>>",font='times 15', foreground = 'purple',background='green').pack(side='top',fill=tk.BOTH,expand=True)
               buton9=tk.Button(frame2,text="food list for weight loss",bg="white",font="Times 20",fg="black",relief="raised",command=foodlistloss)
               buton9.pack(side='top')
               w6=ttk.Label(frame2,text="POTATOES",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w7=tk.Label(frame2,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo4,text=moto4,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)#,image=logo4
               home=tk.Button(frame2,text="<BACK",bg="white",font="Times 20",fg="black",relief="raised",command=root)
               home.pack(side='bottom')
               logo5=tk.PhotoImage(file="wtgaincombo.gif")#gif/.pmb
               moto5=""" 2.Opt for Fiber-Rich Foods \nhigh fiber intake stretches the stomach, \nslows its emptying rate and influences the \nrelease of fullness hormones .
           \nIn addition, fiber can ferment in the bowel. \nThis produces short-chain fatty acids thought to \nfurther help promote feelings of fullness .
           \nEating an extra 14 grams of fiber each day may \nincrease your calorie intake by up to 10%. \nOver 3.8 months, this could lead to a gain of up\n to 4.2 lbs (1.9 kg)."""
               w9=ttk.Label(frame2,text="FIBERS",font='times 15', foreground = 'purple',background='#AFEEEE').pack(side='top',fill=tk.BOTH,expand=True)
               w10=tk.Label(frame2,compound=tk.LEFT,justify=tk.LEFT,padx=1,image=logo5,text=moto5,font='Times',fg='white',bg="indigo").pack(side='top',anchor=tk.W,fill=tk.BOTH,expand=True)#,image=logo5
               root.geometry('920x750')
               root.configure(bg="indigo")
               root.mainloop()    




            
           buton1=tk.Button(self,text="Weight loss",bg="white",font="Times 20",fg="black",relief="raised",command=weightloss)
           buton1.place(x=220,y=140)


           buton2=tk.Button(self,text="Weight gain",bg="white",font="Times 20",fg="black",relief="raised",command=weightgain)
           buton2.place(x=220,y=200)

           def foodlistloss():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               canvas.bind('<Configure>', on_configure)
               
               image2 = tk.PhotoImage(master=self, file="BACKGR.png")
               panel2 = tk.Label(self,image = image2,height=700)
               panel2.place(x=0,y=0)
               panel2.image = image2
               
               frame3 = tk.Frame(canvas)
               frame3.configure(bg="white")
               root.configure(bg='white')
               canvas.create_window(90,90, window=frame3, anchor='nw',)
               w = tk.Scrollbar(root,orient="vertical")
               done=tk.Button(frame3,text="DONE",bg="yellow",font="Times 20",fg="black",relief="raised")
               done.pack(side='top')
               back1=tk.Button(frame3,text="<BACK",bg="yellow",font="Times 20",fg="black",relief="raised",command=weightloss)
               back1.pack(side='bottom')


               var37=tk.IntVar()
               w1 = tk.Checkbutton(frame3,text="lemon",variable=var37,onvalue = 1, offvalue = 0)
               var65=tk.IntVar()
               w2 = tk.Checkbutton(frame3,text="irish potatoes",variable=var65,onvalue = 1, offvalue = 0)
               var38=tk.IntVar()
               w3 = tk.Checkbutton(frame3,text="Meat",variable=var38,onvalue = 1, offvalue = 0)
               var39=tk.IntVar()
               w4 = tk.Checkbutton(frame3,text="water",variable=var39,onvalue = 1, offvalue = 0)
               var40=tk.IntVar()
               w5 = tk.Checkbutton(frame3,text="gnuts",variable=var40,onvalue = 1, offvalue = 0)
               var41=tk.IntVar()
               w6 = tk.Checkbutton(frame3,text="ovacado",variable=var41,onvalue = 1, offvalue = 0)
               var42=tk.IntVar()
               w7 = tk.Checkbutton(frame3,text="chicken",variable=var42,onvalue = 1, offvalue = 0)
               var43=tk.IntVar()
               w8 = tk.Checkbutton(frame3,text="Eggs",variable=var43,onvalue = 1, offvalue = 0)
               var44=tk.IntVar()
               w9 = tk.Checkbutton(frame3,text="Greens",variable=var44,onvalue = 1, offvalue = 0)
               var45=tk.IntVar()
               w10 = tk.Checkbutton(frame3,text="fruits",variable=var45,onvalue = 1, offvalue = 0)
               w1.pack()
               w2.pack()
               w3.pack()
               w4.pack()
               w5.pack()
               w6.pack(side='top')
               w7.pack(side='top')
               w8.pack(side='top')
               w9.pack(side='top')
               w10.pack(side='top')

           def foodlistgain():
               def on_configure(event):
                   canvas.configure(scrollregion=canvas.bbox('all'))
               root = tk.Toplevel()
               canvas = tk.Canvas(root, width=700, height=700)
               canvas.pack(fill=tk.BOTH,side=tk.TOP)
               scrollbar = tk.Scrollbar(root, command=canvas.yview)
               scrollbar.pack(side=tk.RIGHT,anchor=tk.W, fill='y')

               canvas.configure(yscrollcommand = scrollbar.set)

               canvas.bind('<Configure>', on_configure)
               frame3 = tk.Frame(canvas)
               frame3.configure(bg="white")
               root.configure(bg='white')
               canvas.create_window(90,90, window=frame3, anchor='nw',)
               w = tk.Scrollbar(root,orient="vertical")
               done=tk.Button(frame3,text="DONE",bg="yellow",font="Times 20",fg="black",relief="raised")
               done.pack(side='top')
               back=tk.Button(frame3,text="<BACK",bg="yellow",font="Times 20",fg="black",relief="raised",command=weightgain)
               back.pack(side='bottom')



               var46=tk.IntVar()
               w1 = tk.Checkbutton(frame3,text="Posho",variable=var46,onvalue = 1, offvalue = 0)
               var47=tk.IntVar()
               w2 = tk.Checkbutton(frame3,text="Nyasa",variable=var47,onvalue = 1, offvalue = 0)
               var48=tk.IntVar()
               w3 = tk.Checkbutton(frame3,text="Beans",variable=var48,onvalue = 1, offvalue = 0)
               var49=tk.IntVar()
               w4 = tk.Checkbutton(frame3,text="Cassava",variable=var49,onvalue = 1, offvalue = 0)
               var50=tk.IntVar()
               w5 = tk.Checkbutton(frame3,text="sweet potatoes",variable=var50,onvalue = 1, offvalue = 0)
               var51=tk.IntVar()
               w6 = tk.Checkbutton(frame3,text="Fattyfish",variable=var51,onvalue = 1, offvalue = 0)
               var52=tk.IntVar()
               w7 = tk.Checkbutton(frame3,text="irish potatoes",variable=var52,onvalue = 1, offvalue = 0)
               var53=tk.IntVar()
               w8 = tk.Checkbutton(frame3,text="Beans",variable=var53,onvalue = 1, offvalue = 0)
               var54=tk.IntVar()
               w9 = tk.Checkbutton(frame3,text="sugar cane",variable=var54,onvalue = 1, offvalue = 0)
               var55=tk.IntVar()
               w10 = tk.Checkbutton(frame3,text="smoothes",variable=var55,onvalue = 1, offvalue = 0)
               w1.pack()
               w2.pack()
               w3.pack()
               w4.pack()
               w5.pack()
               w6.pack(side='top')
               w7.pack(side='top')
               w8.pack(side='top')
               w9.pack(side='top')
               w10.pack(side='top')
                       


           



    class Page12(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 7")
           label.pack(side="right", fill="both", expand=True)


    class Page13(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           label = ttk.Label(self, text="This is page 7")
           label.pack(side="right", fill="both", expand=True)

    class Page14(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
    ##       label = ttk.Label(self, text="This is page 7")
    ##       label.pack(side="right", fill="both", expand=True)
##           canvas = tk.Canvas(self)
           image1 = tk.PhotoImage(master=self, file="weightmonitor.png")
           panel1 = tk.Label(self,image = image1,height=700)
           panel1.place(x=0,y=0)
           panel1.image = image1
           self.tk_focusFollowsMouse()
           def kconnect():
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               cur.execute("CREATE TABLE IF NOT EXISTs WEIGHTMONITOR(ID INTEGER PRIMARY KEY AUTOINCREMENT,week integer,weight integer)")
               con.commit()
               con.close()
           kconnect()
           X1Lable= tk.Label(self,text="Week no.:",font="Times 10",bg="blue",fg="white")
           X2Lable= tk.Label(self,text="Week no.:",font="Times 10",bg="blue",fg="white")
           X3Lable= tk.Label(self,text="Week no.:",font="Times 10",bg="blue",fg="white")
           X4Lable= tk.Label(self,text="Week no.:",font="Times 10",bg="blue",fg="white")
    

           Y1Lable= tk.Label(self,text="Weight1:",font="Times 10",bg="blue",fg="white")
           Y2Lable= tk.Label(self,text="Weight2:",font="Times 10",bg="blue",fg="white")
           Y3Lable= tk.Label(self,text="Weight3:",font="Times 10",bg="blue",fg="white")
           Y4Lable=tk. Label(self,text="Weight4:",font="Times 10",bg="blue",fg="white")
           tLable=tk. Label(self,text="Target Weight:",font="Times 10",bg="blue",fg="white")
           namel=tk.Label(self,text="Graph Title:")
           def clear1():
               x1.delete(0,tk.END)
               y1.delete(0,tk.END)
               x2.delete(0,tk.END)
               x3.delete(0,tk.END)
               x4.delete(0,tk.END)
               y2.delete(0,tk.END)
               y3.delete(0,tk.END)
               y4.delete(0,tk.END)

           def dele(id):
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               cur.execute("DELETE FROM  WEIGHTMONITOR WHERE id=?",(id,))
        
               con.commit()
               con.close()


           


           
           #listbox=tk.Listbox(root, width=70,height=15)
           listbox=tk.Listbox(self, width=100)
           global tt
           def selectionCommand2(event):
               global tt
               yoid= listbox.curselection()[0]
               tt=listbox.get(yoid)
               x1.delete(0,tk.END)
               x1.insert(tk.END,tt[1])
               y1.delete(0,tk.END)
               y1.insert(tk.END,tt[2])
               x2.delete(0,tk.END)
               x3.delete(0,tk.END)
               x4.delete(0,tk.END)
               y2.delete(0,tk.END)
               y3.delete(0,tk.END)
               y4.delete(0,tk.END)
        

               if len(tt) == 0:
                   print( 'No selection')
               else:
                   print ('Selection:', tt[0])

           def delete():
               #if (len(x1n.get())!=0):
               dele(tt[0])
               clear1()
               view_command()
           clear= ttk.Button(self,text="clear",command=clear1)
           delete= ttk.Button(self,text="Delete",command=delete)
##           listbox = Pmw.ScrolledListBox(self,
##               items=(),
##               labelpos='nw',
##               label_text='Record week weight',
##               listbox_height = 6,
##               selectioncommand=selectionCommand2,
##               dblclickcommand=selectionCommand2,
##               usehullsize = 1,
##               hull_width = 300,
##               hull_height = 200,
##             )
           #sb=tk.Scrollbar(root)
           listbox.bind('<<ListboxSelect>>',selectionCommand2)
           sb=tk.Scrollbar(self)
           sb.place(x=850,y=500)
           listbox.configure(yscrollcommand=sb.set)
           sb.configure(command=listbox.yview)
           x1n=tk.StringVar()
           x1=tk.Entry(self,textvariable=x1n,width=15,font='courier 10',bg="light blue")
           x2n=tk.StringVar()
           x2=tk.Entry(self,textvariable=x2n,width=15,font='courier 10',bg="light blue")
           x3n=tk.StringVar()
           x3=tk.Entry(self,textvariable=x3n,width=15,font='courier 10',bg="light blue")
           x4n=tk.StringVar()
           x4=tk.Entry(self,textvariable=x4n,width=15,font='courier 10',bg="light blue")
           y1n=tk.StringVar()
           y1=tk.Entry(self,textvariable=y1n,width=15,font='courier 10',bg="light blue")
           y2n=tk.StringVar()
           y2=tk.Entry(self,textvariable=y2n,width=15,font='courier 10',bg="light blue")
           y3n=tk.StringVar()
           y3=tk.Entry(self,textvariable=y3n,width=15,font='courier 10',bg="light blue")
           y4n=tk.StringVar()
           y4=tk.Entry(self,textvariable=y4n,width=15,font='courier 10',bg="light blue")
           tn=tk.StringVar()
           t=tk.Entry(self,textvariable=tn,width=15,font='courier 10',bg="light blue")
           n1n=tk.StringVar()





           n1=tk.Entry(self,textvariable=n1n)
           tLable.place(x=300,y=140)
           Y1Lable.place(x=300,y=200)
           Y2Lable.place(x=300,y=250)
           Y3Lable.place(x=300,y=300)
           Y4Lable.place(x=300,y=350)
           t.place(x=395,y=140)
           y1.place(x=365,y=200)
           y2.place(x=365,y=250)
           y3.place(x=365,y=300)
           y4.place(x=365,y=350)

           listbox.place(x=300,y=450)
           delete.place(x=700,y=400)

           clear.place(x=500,y=400)



           X1Lable.place(x=550,y=200)

           X2Lable.place(x=550,y=250)

           X3Lable.place(x=550,y=300)
           X4Lable.place(x=550,y=350)
           x1.place(x=615,y=200)
           x2.place(x=615,y=250)
           x3.place(x=615,y=300)
           x4.place(x=615,y=350)
           #plot
           def graph():
               try:
                   X1=float(x1.get())
                   X2=float(x2.get())
                   X3=float(x3.get())
                   X4=float(x4.get())
                   #X5=float(Entry.get(x5))

                   #name=str(n1.get())
                   T=float(t.get())
                   Y1=float(y1.get())
                   Y2=float(y2.get())
                   Y3=float(y3.get())
                   Y4=float(y4.get())
               except ValueError:
                   tm.showerror("ValueError", "Please fill in proper values in all fields")
               try:
##                   plt.plot([X1,X2,X3,X4],[Y1,Y2,Y3,Y4],label="Progress")
##                   plt.axhline(y=T,linewidth=2, color='r',label="Target Weight")
##                   plt.legend()
##                   plt.xlabel("TIME(Weeks)")
##                   plt.ylabel("WEIGHT(Kgs)")
##                   plt.title("PROGRESS WEIGHTLOSS/GAIN")
##                   plt.show()
                   tm.showinfo("Notification", "The data visualisation Graph will \nsoon be incorparated into the compiled software\nwe are sorry for the inconvinience")
                   
               except UnboundLocalError:
                   tm.showerror("UnboundLocalError", "Please fill digits in all fields")
                   
           plotbut= ttk.Button(self,text="show progress:",command=graph)#,command=graph
           plotbut.place(x=300,y=400)
           def add_command():
               if(len(y1n.get())!=0):
                   key=[x1n,x2n,x3n,x4n]
                   value=[y1n,y2n,y3n,y4n]
                   listbox.delete(0,tk.END)
                   for i in range(len(key)):
                       k=key[i].get()
                       v=value[i].get()
                       con=sqlite3.connect("diet.db")
                       cur=con.cursor()
                       cur.execute("INSERT INTO WEIGHTMONITOR VALUES (NULL,?,?)",(k,v))
                       print("just put this in:",k,v)
                       con.commit()
                       con.close()
                       #listbox.delete(0,END)
                       listbox.insert(tk.END,(v,k))
           def view_command():
               con=sqlite3.connect("diet.db")
               cur=con.cursor()
               cur.execute("SELECT * FROM WEIGHTMONITOR")
               rows=cur.fetchall()
               con.close()
               listbox.delete(0,tk.END)
               for row in rows:
                   listbox.insert(tk.END,row)
            
        
           save= ttk.Button(self,text="save",command=add_command)
           save.place(x=410,y=400)
           listrecords= ttk.Button(self,text="Listrecords",command=view_command)#
           listrecords.place(x=600,y=400)



               

    class Page15(Page):
       def __init__(self, *args, **kwargs):
           Page.__init__(self, *args, **kwargs)
           #label = ttk.Label(self, text="")
           #label.pack(side="top", expand=True)

    class MainView(tk.Frame):
        def __init__(self, *args, **kwargs):
            tk.Frame.__init__(self, *args, **kwargs)
            global p1
            p1 = Page1(self)
            global p2
            p2 = Page2(self)
            p3 = Page3(self)
            p4 = Page4(self)
            p5 = Page5(self)
            p6 = Page6(self)
            p7 = Page7(self)
            p8 = Page8(self)
            p9 = Page9(self)
            p10 = Page10(self)
            p11 = Page11(self)
            p12 = Page12(self)
            p13 = Page13(self)
            p14= Page14(self)
            p15= Page15(self)

            buttonframe = tk.Frame(self)
            container = tk.Frame(self)
            buttonframe.pack(side="top", fill="both", expand=False)
            container.pack(side="top", fill="both", expand=True)
##
            p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p3.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p4.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p5.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p6.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p7.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p8.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p9.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p10.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p11.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p12.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p13.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p14.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            p15.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
            

            b1 = ttk.Button(buttonframe, text="Home", command=p1.lift)
            b2 = ttk.Button(buttonframe, text="Foodlist", command=p2.lift)
            b3 = ttk.Button(buttonframe, text="Price", command=p3.lift)
            b4 = ttk.Button(buttonframe, text="Page 4", command=p4.lift)
            #b5 = ttk.Button(buttonframe, text="Page 5", command=p5.lift)
            #b6 = ttk.Button(buttonframe, text="Page 6", command=p6.lift)
            #b7 = ttk.Button(buttonframe, text="Page 7", command=p7.lift)
            #b8 = ttk.Button(buttonframe, text="Page 8", command=p8.lift)
            #b9 = ttk.Button(buttonframe, text="Page 9", command=p9.lift)
            b10 = ttk.Button(buttonframe, text="Disiese", command=p10.lift)
            b11 = ttk.Button(buttonframe, text="Recommendations", command=p11.lift)
            #b12 = ttk.Button(buttonframe, text="Page12", command=p12.lift)
            #b13 = ttk.Button(buttonframe, text="Page13", command=p13.lift)
            b14 = ttk.Button(buttonframe, text="WeightMonitor", command=p14.lift)
            #b15 = ttk.Button(buttonframe, text="Page15", command=p15.lift)

            b1.pack(side="left")
            b2.pack(side="left")
            b3.pack(side="left")
            b4.pack(side="left")
            #b5.pack(side="left")
            #b6.pack(side="left")
            #b7.pack(side="left")
            #b8.pack(side="left")
            #b9.pack(side="left")
            b10.pack(side="left")
            b11.pack(side="left")
            #b12.pack(side="left")
            #b13.pack(side="left")
            b14.pack(side="left")
            #b15.pack(side="left")

            p1.show()

    if __name__ == "__main__":
        root = tk.Tk()
        
        main = MainView(root)
        main.pack(side="top", fill="both", expand=True)
        root.wm_geometry("1160x800")
        root.title("MyProgress")

        #menuebar
        menu=tk.Menu(main)
        root.config(menu=menu)
        subMenu=tk.Menu(menu)
        #file
        menu.add_cascade(label="File",menu=subMenu)
        subMenu.add_command(label="Goto")
        subMenu.add_command(label="New")
        subMenu.add_separator()
        subMenu.add_command(label="exit")
        #edit
        editMenu=tk.Menu(menu)
        menu.add_cascade(label="Edit",menu=editMenu)
        editMenu.add_command(label="edit")

        


        
        root.mainloop()
        


class Diet(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.tk_focusFollowsMouse()
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        
        for F in (LoginFrame,RegisterF):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame(LoginFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg='#DAD8D4') #D0CECA #DAD8D4
        image1 = tk.PhotoImage(master=self,file="image.png")
        panel1 = tk.Label(self,image = image1,height=900,bg='#DAD8D4')
        panel1.place(x=0,y=0)
        panel1.image = image1
        style = ttk.Style()
        style.configure('A.TButton',foreground='black',background='purple',padding=5,relief='flat',width=15,font='courier 30 bold')
        style.map('A.TButton',foreground=[('pressed','red'),('active','blue')],background=[('pressed','!disabled','black'),('active','white')])
        style.configure('a.TButton',foreground='black',background='purple',padding=5,relief='flat',width=20,font='helitia 10 ')
        style.map('a.TButton',foreground=[('pressed','red'),('active','blue')],background=[('pressed','!disabled','black'),('active','white')])

        

        l1 = tk.Label(self, text='Welcome to my Diet App', font='Algerian 40', fg = '#C20B0B',bg='#DAD8D4')
        l1.grid(row=0, column=3,columnspan=8,padx=20)
        
        
        l1 = tk.Label(self, text='Login to get whats fit for you!!!...', font='times 25', fg = '#C4220E',bg='#DAD8D4')
        l1.grid(row=2, column=3, pady=25,columnspan=4)
        
        self.label_username = ttk.Label(self, text="Username", style='A.TButton', font='times 15')
        self.label_password = ttk.Label(self, text="Password", style='A.TButton', font='times 15')
        self.username=tk.StringVar()
        self.entry_username = tk.Entry(self,  width=30,font='courier 15 bold',textvariable=self.username)
        self.password=tk.StringVar()
        self.entry_password = tk.Entry(self, show="*", width=30,font='courier 15 bold',textvariable=self.password)

        self.label_username.grid(row=4,column=3,pady=5,padx=20)
        self.label_password.grid(row=5,column=3,pady=5,padx=20)
        self.entry_username.grid(row=4,column=4,pady=5,padx=5)
        self.entry_password.grid(row=5,column=4,pady=5,padx=5)

        self.checkbox = tk.Checkbutton(self, text="Keep me logged in", width=20, font='times 15',bg='#DAD8D4')
        self.checkbox.grid(columnspan=2,row=7,column=4)

        self.logbtn = ttk.Button(self,style='a.TButton',text="Login", command=self._login_btn_clicked)
        self.logbtn.grid(column=4,row=9, pady=5,sticky='e')
        

        register = tk.Button(self, text= 'Register', font='helitica 15 bold',bg='#DAD8D4',fg='#C4220E',command=lambda:controller.show_frame(RegisterF))
        register.grid(row=10,column=4, pady=20,sticky='e')

        self.grid(row=5,column=3)
        self.controller=controller

    def _login_btn_clicked(self):
        if len(self.username.get().strip())==0:
            tm.showerror("Login error", "Please enter the username")
        elif len(self.password.get().strip())==0:
            tm.showerror("Login error", "Please enter the password")
        else:
            conn=sqlite3.connect("data.db")
            cur=conn.cursor()
            sql="SELECT * FROM user WHERE username='{}' AND password='{}'".format(self.username.get(),self.password.get())
            cur.execute(sql)
            user=cur.fetchall()
            if len(user)!=0:
                self.username.set("")
                self.password.set("")
                self.logbtn.config(command=lambda:other_functions())
            else:
                tm.showerror("Login error", "username and password do not match any existing account")
            cur.close()
            conn.close()
            
class RegisterF(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        tk.Frame.config(self, bg="#DAD8D4")
        style = ttk.Style()
        style.configure('B.TButton',foreground='black',background='purple',padding=5,relief='flat',width=10,font='courier 20 bold')
        style.map('B.TButton',foreground=[('pressed','red'),('active','blue')],background=[('pressed','!disabled','black'),('active','white')])
        style.configure('a.TButton',foreground='black',background='purple',padding=5,relief='flat',width=11,font='helitia 10 ')
        style.map('a.TButton',foreground=[('pressed','red'),('active','blue')],background=[('pressed','!disabled','black'),('active','white')])

        
        mydiet = tk.Label(self, text='MY DIET APP', font='helitica 25 bold',bg='#DAD8D4',fg='#C4220E')
        mydiet.grid(row=1, column=1)
        note = tk.Label(self, text='Eat Health and Live Longer', font='helitica 20 bold',bg='#DAD8D4',fg='#C4220E')
        note.grid(row=2,column=2,pady=10)
        self.username=tk.StringVar()
        username_label = tk.Label(self, text= 'username', font='helitica 20 bold',bg='#DAD8D4',fg='#C4220E' )
        username_label.grid(row=3,column=1, pady=5)
        username_entry = tk.Entry(self,  width=30,font='courier 15',textvariable=self.username)
        username_entry.grid(row=3,column=2, pady=5)
        self.password=tk.StringVar()
        password_label = tk.Label(self, text= 'Password', font='helitica 20 bold',bg='#DAD8D4',fg='#C4220E' )
        password_label.grid(row=7,column=1, pady=5)
        password_entry = tk.Entry(self,  width=30,font='courier 15',textvariable=self.password,show="*")
        password_entry.grid(row=7,column=2, pady=5)
        self.confirm=tk.StringVar()
        confirm_label = tk.Label(self, text= 'Confirm', font='helitica 20 bold',bg='#DAD8D4',fg='#C4220E' )
        confirm_label.grid(row=8,column=1, pady=5)
        confirm_entry = tk.Entry(self,  width=30,font='courier 15',textvariable=self.confirm,show="*")
        confirm_entry.grid(row=8,column=2, pady=5)
        
        submit = tk.Button(self, text= 'Submit', font='helitica 15 bold',bg='#DAD8D4',fg='#C4220E',command=self.register_user )
        submit.grid(row=9,column=4 , pady=5)
        submit = tk.Button(self, text= 'Login', font='helitica 15 bold',bg='#DAD8D4',fg='#C4220E',command=lambda:controller.show_frame(LoginFrame) )
        submit.grid(row=10,column=4 , pady=5)
    def register_user(self):
        
        if self.confirm.get()!=self.password.get():
            tm.showerror("Error", "Passwords don't match")

            
        else:
            if len(self.username.get().strip())==0:
                tm.showerror("Error", "Please enter the username!!!")
            elif len(self.password.get().strip()) ==0:
                tm.showerror("Error", "Please enter the password!!!")
                
            else:
                conn=sqlite3.connect("data.db")
                cur=conn.cursor()
                sql="SELECT * FROM user WHERE username='{}'".format(self.username.get())
                cur.execute(sql)
                redundant=cur.fetchall()
                if len(redundant)!=0:
                    tm.showerror("DB Error", "The username is already taken!!!")
                else:
                    sql="INSERT INTO user(username,password)VALUES('{}','{}')".format(self.username.get(),self.password.get())
                    cur.execute(sql)
                    conn.commit()
                    self.username.set("")
                    self.password.set("")
                    self.confirm.set("")
                    tm.showinfo("Success", "Your account was successfully created, you may now login!")
                cur.close()
                conn.close()

                

        

app = Diet()
app.title('My Diet')
app.geometry("900x800")
app.mainloop()
