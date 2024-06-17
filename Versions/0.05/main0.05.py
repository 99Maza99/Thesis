#Imported libraries (Some maybe downloaded)
import tkinter
from tkinter import ttk

#Self made libraries
import EntryTab
import DBtool
from Scantool import Scanner

#Global stuffs
labelscanner = Scanner(widgets= None , operation="Standby")
labelscanner.start()
#Root window
root = tkinter.Tk()



#Main frame
Mainframe = ttk.Notebook(root)
Mainframe.pack(fill='both', expand=True)

EntryTabFrame = ttk.Frame(Mainframe)##Creates a frame that works as a tab that would fit into the notebook widget
conn = DBtool.Connection.start()##Starts a connection to the database

EntryTab.TabFunction.build(EntryTabFrame, conn, labelscanner)
Mainframe.add(EntryTabFrame, text="EntryTab")




if __name__ == "__main__":

    ##Starts Threads for the GUIs
    root.mainloop()