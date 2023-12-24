import wx
import os

class AddressBook(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self,None,-1,"Address Book",size=(520,700))
        self.panel=wx.Panel(self,-1)
        self.SetBackgroundColour("#95CAE4")
       
        self.title=wx.StaticText(self.panel,-1,"ADDRESS BOOK DATABASE",pos=(120,10))
        self.firstname=wx.StaticText(self.panel,-1,"FirstName",pos=(50,50))
        #self.firstname1=wx.TextCtrl(self.panel,-1,"",pos=(160,50),size=(100,20))
        self.secondname=wx.StaticText(self.panel,-1,"SecondName",pos=(35,80))
        #self.secondname1=wx.TextCtrl(self.panel,-1,"",pos=(160,80),size=(100,20))
        self.addressline1=wx.StaticText(self.panel,-1,"Address(Line1)",pos=(30,110))
        self.addressline2=wx.StaticText(self.panel,-1,"Address(Line2)",pos=(30,140))
        self.addressline3=wx.StaticText(self.panel,-1,"Address(Line3)",pos=(30,170))
        self.city=wx.StaticText(self.panel,-1,"City",pos=(85,200))
        self.state=wx.StaticText(self.panel,-1,"State or Province",pos=(20,230))
        self.zip=wx.StaticText(self.panel,-1,"Postal(zip)Code",pos=(25,260))
        self.homephe=wx.StaticText(self.panel,-1,"HomePhone",pos=(40,290))
        self.workphe=wx.StaticText(self.panel,-1,"WorkPhone",pos=(45,320))
        self.mobile=wx.StaticText(self.panel,-1,"Mobile",pos=(70,350))
        self.email=wx.StaticText(self.panel,-1,"Primary Email",pos=(35,380))
        self.email2=wx.StaticText(self.panel,-1,"Secondary Email",pos=(20,410))
        self.notes=wx.StaticText(self.panel,-1,"Notes",pos=(75,440))

        self.firstname1=wx.TextCtrl(self.panel,-1,"",pos=(130,50),size=(170,20))
        self.secondname1=wx.TextCtrl(self.panel,-1,"",pos=(130,80),size=(170,20))
        self.addressline11=wx.TextCtrl(self.panel,-1,"",pos=(130,110),size=(250,20))
        self.addressline21=wx.TextCtrl(self.panel,-1,"",pos=(130,140),size=(250,20))
        self.addressline31=wx.TextCtrl(self.panel,-1,"",pos=(130,170),size=(250,20))
        
        self.city1=wx.TextCtrl(self.panel,-1,"",pos=(130,200),size=(170,20))
        self.state1=wx.TextCtrl(self.panel,-1,"",pos=(130,230),size=(170,20))
        self.zip1=wx.TextCtrl(self.panel,-1,"",pos=(130,260),size=(170,20))
        self.homephe1=wx.TextCtrl(self.panel,-1,"",pos=(130,290),size=(170,20))
        self.workphe1=wx.TextCtrl(self.panel,-1,"",pos=(130,320),size=(170,20))
        self.mobile1=wx.TextCtrl(self.panel,-1,"",pos=(130,350),size=(170,20))
        self.email3=wx.TextCtrl(self.panel,-1,"",pos=(130,380),size=(170,20))
        self.email4=wx.TextCtrl(self.panel,-1,"",pos=(130,410),size=(170,20))
        self.notes1=wx.TextCtrl(self.panel,-1,"",pos=(130,440),size=(250,100),style=wx.TE_MULTILINE)
        self.btn=wx.Button(self.panel,201,"save",pos=(170,570),size=(70,30))
        self.btn1=wx.Button(self.panel,202,"clear all",pos=(80,570),size=(70,30))
        self.btn2=wx.Button(self.panel,203,"retrieve",pos=(260,570),size=(70,30))
        
        self.Bind(wx.EVT_BUTTON,self.retrive,id=203)
        self.Bind(wx.EVT_BUTTON,self.clear,id=202)
        self.Bind(wx.EVT_BUTTON,self.save,id=201)
       
        self.filename="AddressBookDataBase"
        if not os.path.exists(self.filename):
            os.makedirs('AddressBookDataBase')
        
        


    def save(self,event):
        self.firstname=self.firstname1.GetValue()
        self.secondname=self.secondname1.GetValue()
        self.addressline1=self.addressline11.GetValue()
        self.addressline2=self.addressline21.GetValue()
        self.addressline3=self.addressline31.GetValue()
        self.city=self.city1.GetValue()
        self.state=self.state1.GetValue()
        self.zip=self.zip1.GetValue()
        self.homephe=self.homephe1.GetValue()
        self.workphe=self.workphe1.GetValue()
        self.mobile=self.mobile1.GetValue()
        self.email=self.email3.GetValue()
        self.email2=self.email4.GetValue()
        self.notes=self.notes1.GetValue()
        if (len(self.firstname) and len(self.secondname) and len(self.addressline1) and len(self.addressline2) and len(self.addressline3) and len(self.city) and len(self.state) and len(self.zip) and len(self.homephe) and len(self.workphe) and len(self.mobile) and len(self.email) and len(self.email2) and len(self.notes))>0:
            
           # print self.firstname
            box=wx.TextEntryDialog(None,"Enter AddressBookName To Save","Title","default text")
            if box.ShowModal()==wx.ID_OK:
                self.addressbookname=box.GetValue()
                #self.dial = wx.MessageDialog(None, 'saved successfully', 'Info', wx.OK)
                #self.dial.ShowModal()
                if not os.path.exists('AddressBookDataBase/'+self.addressbookname+'.txt'):
                    
                    
                    self.filename = open('AddressBookDataBase/'+self.addressbookname+'.txt','w')
                    self.filename.write(self.firstname+'\n')
                    self.filename.write(self.secondname+'\n')
                    self.filename.write(self.addressline1+'\n')
                    self.filename.write(self.addressline2+'\n')
                    self.filename.write(self.addressline3+'\n')
                    self.filename.write(self.city+'\n')
                    self.filename.write(self.state+'\n')
                    self.filename.write(self.zip+'\n')
                    self.filename.write(self.homephe+'\n')
                    self.filename.write(self.workphe+'\n')
                    self.filename.write(self.mobile+'\n')
                    self.filename.write(self.email+'\n')
                    self.filename.write(self.email2+'\n')
                    self.filename.write(self.notes+'\n')
                    self.filename.close()
                    self.filename=open('AddressBookDataBase/filenames.txt','a')
                    self.filename.write(self.addressbookname+'\n')
                    self.filename.close()
                    self.dial = wx.MessageDialog(None, 'saved successfully', 'Info', wx.OK)
                    self.dial.ShowModal()

                    
                else:
                    self.dial = wx.MessageDialog(None, 'AddressBookname already exists, enter another name to save', 'Info', wx.OK)
                    self.dial.ShowModal()
                
            else:
                self.dial = wx.MessageDialog(None, 'save cancelled', 'Info', wx.OK)
                self.dial.ShowModal()
                
                    
        else:

            self.dial = wx.MessageDialog(None, 'please fill all fields', 'Info', wx.OK)
            self.dial.ShowModal()

    def clear(self,event):
        self.firstname1.Clear()
        self.secondname1.Clear()
        self.addressline11.Clear()
        self.addressline21.Clear()
        self.addressline31.Clear()
        self.city1.Clear()
        self.state1.Clear()
        self.zip1.Clear()
        self.homephe1.Clear()
        self.workphe1.Clear()
        self.mobile1.Clear()
        self.email3.Clear()
        self.email4.Clear()
        self.notes1.Clear()
        

    def retrive(self,event):

        
        self.fo=open('AddressBookDataBase/filenames.txt','r')
        f=self.fo.readlines()
        self.fo.close()

        self.box=wx.SingleChoiceDialog(None,"choose Address book name","filenames",f)
        if self.box.ShowModal()==wx.ID_OK:
            self.apples=self.box.GetStringSelection()
            self.app=self.apples[:-1]
            self.filenam = open('AddressBookDataBase/'+self.app+'.txt','r')
            line=self.filenam.readlines()
            line1=line[0]
            line2=line[1]
            line3=line[2]
            line4=line[3]
            line5=line[4]
            line6=line[5]
            line7=line[6]
            line8=line[7]
            line9=line[8]
            line10=line[9]
            line11=line[10]
            line12=line[11]
            line13=line[12]
            line14=line[13]
            self.firstname1.SetValue(line1[:-1])
            self.secondname1.SetValue(line2[:-1])
            self.addressline11.SetValue(line3[:-1])
            self.addressline21.SetValue(line4[:-1])
            self.addressline31.SetValue(line5[:-1])
        
            self.city1.SetValue(line6[:-1])
            self.state1.SetValue(line7[:-1])
            self.zip1.SetValue(line8[:-1])
            self.homephe1.SetValue(line9[:-1])
            self.workphe1.SetValue(line10[:-1])
            self.mobile1.SetValue(line11[:-1])
            self.email3.SetValue(line12[:-1])
            self.email4.SetValue(line13[:-1])
            self.notes1.SetValue(line14[:-1])
            self.btn4=wx.Button(self.panel,205,"update",pos=(350,570),size=(70,30))
            self.Bind(wx.EVT_BUTTON,self.update,id=205)
            self.note=wx.StaticText(self.panel,-1,"Note: After modify the existing address book HIT UPDATE button",pos=(10,610))

    def update(self,event):

        
        self.firstname=self.firstname1.GetValue()
        print (self.firstname)
        self.secondname=self.secondname1.GetValue()
        self.addressline1=self.addressline11.GetValue()
        self.addressline2=self.addressline21.GetValue()
        self.addressline3=self.addressline31.GetValue()
        self.city=self.city1.GetValue()
        self.state=self.state1.GetValue()
        self.zip=self.zip1.GetValue()
        self.homephe=self.homephe1.GetValue()
        self.workphe=self.workphe1.GetValue()
        self.mobile=self.mobile1.GetValue()
        self.email=self.email3.GetValue()
        self.email2=self.email4.GetValue()
        self.notes=self.notes1.GetValue()

     
        self.updat = open('AddressBookDataBase/'+self.app+'.txt','w')
        self.updat.write(self.firstname+'\n')
        self.updat.write(self.secondname+'\n')
        self.updat.write(self.addressline1+'\n')
        self.updat.write(self.addressline2+'\n')
        self.updat.write(self.addressline3+'\n')
        self.updat.write(self.city+'\n')
        self.updat.write(self.state+'\n')
        self.updat.write(self.zip+'\n')
        self.updat.write(self.homephe+'\n')
        self.updat.write(self.workphe+'\n')
        self.updat.write(self.mobile+'\n')
        self.updat.write(self.email+'\n')
        self.updat.write(self.email2+'\n')
        self.updat.write(self.notes+'\n')
        self.updat.close()
        self.app=0
        self.btn4.Destroy()
        self.dial = wx.MessageDialog(None, 'updated', 'Info', wx.OK)
        self.dial.ShowModal()

        
       
        
        

        
                    
        

            
            




        
app=wx.App()
frame=AddressBook()
frame.Centre()
frame.Show()
app.MainLoop()
