from tkinter import *
from PIL import Image,ImageTk
import random
import csv
import os
#from playsound import playsound

    

#path
absolute_path = os.path.dirname(__file__)

imgpath1 = os.path.join(absolute_path, 'agent.png')
imgpath2 = os.path.join(absolute_path, 'client.png')
imgpath3 = os.path.join(absolute_path, 'error.ico')
imgpath4 = os.path.join(absolute_path, 'erroragent.png')
imgpath5 = os.path.join(absolute_path, 'errormessage.png')
imgpath6 = os.path.join(absolute_path, 'icon.ico')
imgpath7 = os.path.join(absolute_path, 'main.png')
imgpath8 = os.path.join(absolute_path, 'toto.gif')



class toto(Label):
    def __init__(self, master, path):
        self._gif = Image.open(path)
        self._frames = []
        try:
            while True:
                self._frames.append(ImageTk.PhotoImage(self._gif.copy()))
                self._gif.seek(len(self._frames)) 
        except EOFError:
            pass

        self._frame_index = 0
        self._num_frames = len(self._frames)

        super().__init__(master, image=self._frames[0])

    def start_animation(self):
        self._animate()

    def stop_animation(self):
        self.after_cancel(self._anim_id)

    def _animate(self):
        self._frame_index = (self._frame_index + 1) % self._num_frames
        self.configure(image=self._frames[self._frame_index])
        self._anim_id = self.after(50, self._animate)


#Path
absolute_path = os.path.dirname(__file__)
path1 = os.path.join(absolute_path, 'data.csv')
#Data
Data = []
#Check
isFile = os.path.isfile(path1)
if isFile==False:
    with open(path1, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(Data)
#Loading Data
with open(path1, "r") as f:
    reader = csv.reader(f)
    Data = list(reader)


class Bank():

    def __init__(self,ID,MDP,Sold):
        self.ID=ID
        self.MDP=MDP
        self.Sold=Sold
            
#Cote Agent   
    
    def AjouterCompte():
        if Data==[]:
            n=1
        else:
            n=0
            while n<=int(Data[-1][0]):
                n+=1
        Compte=Bank(int((f"{n}{random.randint(0,100)}")),random.randint(1024,8956),0) 
        Data.append([n,Compte.ID,Compte.MDP,Compte.Sold])
        global gide
        gide=Compte.ID
        global gmdp
        gmdp=Compte.MDP
        global gsold
        gsold=Compte.Sold

#Cote Client
    def ModifierMDP(x,n_mdp):
        Data[x][2]=int(n_mdp)
        with open(path1, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(Data)
    
    def Affichersold(x):
        return Data[x][3]
    
    def Deposer(x,Money):
        if int(Money)<0:
            pass
        else:
            S=int(Data[x][3])
            S+=int(Money)
            Data[x][3]=S
            with open(path1, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(Data)

    def Retirer(x,Money):
        if int(Money)>int(Data[x][3]):
            pass
        else:
            S=int(Data[x][3])
            S-=int(Money)
            Data[x][3]=S
            with open(path1, "w", newline="") as f:
                writer = csv.writer(f)
                writer.writerows(Data)
#Saisie
    def Clientcheck(ide,mdp):
        for i in range(len(Data)):
            if ide==int(Data[i][1]) and mdp==int(Data[i][2]):
                    return 1


    def id_to_mdp(ide):
        for i in range(len(Data)):
            if int(ide)==int(Data[i][1]):
                return i
            
#def ModifierMDP(id_to_mdp(ide.get()),n_mdp):



#-----------------------------------------------------------main programme-------------------------------------------------------------------

#-------------------heading--------------------#
main_window = Tk()                             #
main_window.title('bank')                      #
main_window.iconbitmap(imgpath6)               #
main_window.geometry('990x660')                #
main_window.resizable(0,0)                     #
#----------------------------------------------#

#-------------------background--------------------#
bgimg = ImageTk.PhotoImage(file=imgpath7)         #
bgLabel = Label(main_window,image=bgimg)          #
bgLabel.place(x=0,y=0)                            #
#-------------------------------------------------#
gif = toto(main_window, imgpath8)
gif.start_animation()
gif.place(x=443,y=420)
#--------------------------Client login widgets#------------------------------------------------------------------------------------------
lb1 = Label(main_window,text='Identifiant',font=('bold', 20),bg='black',fg='white')                            
lb1.place(x=665,y=220)                                                                                  
                                                                                                        
ide = Entry(main_window, width=12,bg='black',fg='white',font=('bold', 20))                                      
ide.place(x=665,y=270)                                                                                   
                                                                                                        
lb2 = Label(main_window,text='Mot de pass',font=('bold', 20),bg='BLACK',fg='white')                            
lb2.place(x=665,y=320)                                                                                  
                                                                                                        
psw = Entry(main_window, width=12,bg='black',fg='white',font=('bold', 20))                                     
psw.place(x=665,y=370)                                                                                  
                                                                                                        
sub = Button(main_window,font=('TkDefaultFont', 20),text='sub',width=9,height=1,bg='black',fg='white', command=lambda: open_client(main_window))                    
sub.place(x=680,y=450)                                                                                  
#------------------------------------------------------------------------------------------------------------------------------------------

#-------------------------------------------------------------------Agent login widgets----------------------------------------------
lb3 = Label(main_window,text='Identifiant',font=('TkDefaultFont', 20),bg='black',fg='white')                    
lb3.place(x=145,y=220)                                                                                   
                                                                                                         
ad = Entry(main_window, width=12,bg='black',fg='white',font=('bold', 20))                                       
ad.place(x=145,y=270)                                                                                    
                                                                                                         
lb4 = Label(main_window,text='Mot de pass',font=('TkDefaultFont', 20),bg='black',fg='white')                    
lb4.place(x=145,y=320)                                                                                   
                                                                                                         
pswd = Entry(main_window, width=12,bg='black',fg='white',font=('bold', 20))                                     
pswd.place(x=145,y=370)                                                                                  
                                                                                                         
subd = Button(main_window,font=('TkDefaultFont', 20),text='sub',width=9,height=1,bg='black',fg='white',command=lambda: open_agent(main_window))         
subd.place(x=160,y=450)                                                                                  
#----------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------quit button-------------------------------------------------------------------
quit = Button(main_window,font=('TkDefaultFont', 20),text='quit',width=5,height=1,bg='black',fg='white', command=quit)         
quit.place(x=450,y=550)
#----------------------------------------------------------------------------------------------------------------------------------------
#-------------------------return to the the window------------------------#
def return_to_window1(current_window, previous_window):
    current_window.destroy()
    previous_window.deiconify()
#-------------------------------------------------------------------------#

#-----------------------------agent window-----------------------------------------------------------------------------------------------------------------
def open_agent(main_window):
    if ad.get() == 'admin'and pswd.get() == 'admin':
        main_window.withdraw()
        agent_window = Toplevel(main_window)
        agent_window.title("Client")
        agent_window.geometry('930x600')
        agent_window.resizable(0,0)                            
        new_bg = ImageTk.PhotoImage(file=imgpath1)       
        new_bglabel = Label(agent_window,image=new_bg)                 
        new_bglabel.place(x=0,y=0)                            
        new_bglabel.pack()

        mdf_btn = Button(agent_window,text='Ajouter un Compte',font=('bold', 15),bg='black',fg='white',width=24,height=1,command=lambda:ajouter_c(main_window))                            
        mdf_btn.place(x=330,y=280)                                                                                  
                                                                                                                                                                                                                                    
        n_sub = Button(agent_window,text='retourner',font=('bold', 15),bg='black',fg='white',width=24,command=lambda: return_to_window1(agent_window, main_window))                
        n_sub.place(x=330,y=450) 

        agent_window.mainloop()

    else :
        main_window.withdraw()
        error_window = Toplevel(main_window)
        error_window.title("error")
        error_window.iconbitmap(imgpath3)                    
        error_window.geometry('400x200')
        error_window.resizable(0,0)                            
        new_bg = ImageTk.PhotoImage(file=imgpath4)       
        new_bglabel = Label(error_window,image=new_bg)                 
        new_bglabel.place(x=0,y=0)                            
        new_bglabel.pack()                                                                                                                                                                                                             
        n_sub = Button(error_window,text='ok',font=('bold', 10),bg='black',fg='white',width=10,command=lambda: return_to_window1(error_window, main_window))                
        n_sub.place(x=150,y=160) 

        error_window.mainloop()


#------------------------------ajouter un compte window--------------------------------------------------------------------------------------------------------------------------
def ajouter_c(agent_window):
    agent_window.withdraw()
    aj_window = Toplevel(agent_window)
    aj_window.title("Client")
    aj_window.geometry('930x600')
    aj_window.resizable(0,0)                            
    new_bg = ImageTk.PhotoImage(file=imgpath1)       
    new_bglabel = Label(aj_window,image=new_bg)                 
    new_bglabel.place(x=0,y=0)   
    Bank.AjouterCompte()
    with open(path1, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(Data)
    lab_add = Label(aj_window,text='Identifiant',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab_add.place(x=330,y=220)
    lab_add = Label(aj_window,text=gide,font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab_add.place(x=330,y=260)
    lab_add = Label(aj_window,text='Mot de Pass',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab_add.place(x=330,y=300)
    lab_add = Label(aj_window,text=gmdp,font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab_add.place(x=330,y=340)


    aj_window.mainloop()
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


#--------------------------client window--------------------------------------------------------------------------------
def open_client(main_window):

    if Bank.Clientcheck(int(ide.get()),int(psw.get())) == 1:
            
            main_window.withdraw()
            client_window = Toplevel(main_window)
            client_window.title("Client")
            client_window.geometry('930x600')
            client_window.resizable(0,0)                            
            new_bg = ImageTk.PhotoImage(file=imgpath2)       
            new_bglabel = Label(client_window,image=new_bg)                 
            new_bglabel.place(x=0,y=0)                            
            new_bglabel.pack()

            mdf_btn = Button(client_window,text='Modifier Mot de Passe',font=('bold', 15),bg='black',fg='white',width=24,height=1 ,command=lambda:Modifier_mdp(main_window))                            
            mdf_btn.place(x=330,y=220)                                                                                  
                                                                                                                        
            aff_btn = Button(client_window,text='Afficher Solde',font=('bold', 15),bg='black',fg='white',width=24,height=1,command=lambda:Afficher_solde(main_window))                                      
            aff_btn.place(x=330,y=270)                                                                                   
                                                                                                                        
            dep_btn = Button(client_window,text='Déposer une somme d argent',font=('bold', 15),bg='black',fg='white',width=24,height=1,command=lambda:Déposer_arg(main_window))                            
            dep_btn.place(x=330,y=320)                                                                                  
                                                                                                                        
            ret_psw = Button(client_window,text='Retirer une somme d argent',font=('bold', 15),bg='black',fg='white',width=24,height=1,command=lambda:Retirer_arg(main_window))                                     
            ret_psw.place(x=330,y=370)                                                                                  
                                                                                                                        
            n_sub = Button(client_window,text='retourner',font=('bold', 15),bg='black',fg='white',width=24,command=lambda: return_to_window1(client_window, main_window))               
            n_sub.place(x=330,y=450) 

            client_window.mainloop()
    
    else:
            
            main_window.withdraw()
            erreur_window = Toplevel(main_window)
            erreur_window.title("error")
            erreur_window.iconbitmap(imgpath3)                    #
            erreur_window.geometry('400x200')
            erreur_window.resizable(0,0)                            
            new_bg = ImageTk.PhotoImage(file=imgpath5)       
            new_bglabel = Label(erreur_window,image=new_bg)                 
            new_bglabel.place(x=0,y=0)                            
            new_bglabel.pack()
                                                                                                                                                                                                                        
            n_sub = Button(erreur_window,text='ok',font=('bold', 10),bg='black',fg='white',width=10,command=lambda: return_to_window1(erreur_window, main_window))                
            n_sub.place(x=150,y=160) 

            erreur_window.mainloop()
#----------------------------------------------------------------------------------------------------------
#-----------------------------------------------Modifier Mot de Passe window--------------------------------------------------------------------------------
def Modifier_mdp(client_window):
    client_window.withdraw()
    modifier_WINDOW = Toplevel(client_window)
    modifier_WINDOW.title("Client")
    modifier_WINDOW.geometry('930x600')
    modifier_WINDOW.resizable(0,0)                            
    new_bg = ImageTk.PhotoImage(file=imgpath2)       
    new_bglabel = Label(modifier_WINDOW,image=new_bg)                 
    new_bglabel.place(x=0,y=0)                            
    

    lab = Label(modifier_WINDOW,text='saisir un nouveau mot de pass',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab.place(x=330,y=260)
    ent = Entry(modifier_WINDOW,font=('bold', 15),bg='black',fg='white',width=24)                            
    ent.place(x=330,y=300)
    btn1 = Button(modifier_WINDOW,text='sub',font=('bold', 15),bg='black',fg='white',width=10,height=1,command=lambda:Bank.ModifierMDP(Bank.id_to_mdp(ide.get()),ent.get()))                          
    btn1.place(x=400,y=360)

    modifier_WINDOW.mainloop()
#-----------------------------------------------------------------------------------------------
#---------------------------------------------------Afficher Solde window------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Afficher_solde(client_window):
    client_window.withdraw()
    affichage_window = Toplevel(client_window)
    affichage_window.title("Client")
    affichage_window.geometry('930x600')
    affichage_window.resizable(0,0)                            
    new_bg = ImageTk.PhotoImage(file=imgpath2)       
    new_bglabel = Label(affichage_window,image=new_bg)                 
    new_bglabel.place(x=0,y=0)                            
    
    lab = Label(affichage_window,text='Votre sold est ',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab.place(x=330,y=260)
    ent = Label(affichage_window,text=f'{Bank.Affichersold(Bank.id_to_mdp(ide.get()))} DH',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    ent.place(x=330,y=300)


    affichage_window.mainloop()

#-----------------------------------------------------------------------------------
#---------------------------------------------------Déposer  window------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Déposer_arg(client_window):
    client_window.withdraw()
    deposer_window = Toplevel(client_window)
    deposer_window.title("Client")
    deposer_window.geometry('930x600')
    deposer_window.resizable(0,0)                            
    new_bg = ImageTk.PhotoImage(file=imgpath2)       
    new_bglabel = Label(deposer_window,image=new_bg)                 
    new_bglabel.place(x=0,y=0)    

    lab = Label(deposer_window,text='Saisir la somme a deposer',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab.place(x=330,y=260)
    ent = Entry(deposer_window,font=('bold', 15),bg='black',fg='white',width=24)                            
    ent.place(x=330,y=300)
    btn1 = Button(deposer_window,text='sub',font=('bold', 15),bg='black',fg='white',width=10,height=1,command=lambda:Bank.Deposer(Bank.id_to_mdp(ide.get()),ent.get()))                            
    btn1.place(x=400,y=360)

    deposer_window.mainloop()


#-----------------------------------------------------------------------------------------------------

#-----------------------------------------------------Retirer window----------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def Retirer_arg(client_window):
    client_window.withdraw()
    retirer_window = Toplevel(client_window)
    retirer_window.title("Client")
    retirer_window.geometry('930x600')
    retirer_window.resizable(0,0)                            
    new_bg = ImageTk.PhotoImage(file=imgpath2)       
    new_bglabel = Label(retirer_window,image=new_bg)                 
    new_bglabel.place(x=0,y=0)     

    lab = Label(retirer_window,text='saisir le somme a Retirer',font=('bold', 15),bg='black',fg='white',width=24,height=1)                            
    lab.place(x=330,y=260)
    ent =  Entry(retirer_window,font=('bold', 15),bg='black',fg='white',width=24)                            
    ent.place(x=330,y=300)
    btn1 = Button(retirer_window,text='sub',font=('bold', 15),bg='black',fg='white',width=10,height=1,command=lambda:Bank.Retirer(Bank.id_to_mdp(ide.get()),ent.get()))                            
    btn1.place(x=400,y=360)


    retirer_window.mainloop()


#---------------------------------------------------------------------------------------------------------


main_window.mainloop()