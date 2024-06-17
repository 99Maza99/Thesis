#Imported libraries
import tkinter as tk
from tkinter import ttk
from tkinter import Canvas, Frame, Scrollbar

#Self made libraries
import GUItool
import Commandtool
import DBtool

tab_text = "entry"
Conn = None
labelscanner = None



class OnTabEvents:
    def scannerfocus(event):
        global labelscanner
        global sellentry_entries,sellpersonel_entries
        global buyentry_entries,buypersonel_entries
        global tab_text
        entries = []

        selected_tab = event.widget.select()
        tab_text = event.widget.tab(selected_tab,"text")

        if tab_text == "Buy" :
            entries = buyentry_entries + buypersonel_entries
            print(entries)
            labelscanner.stop()
            labelscanner.update(widgets=entries , operation= "entry")
            labelscanner.start()
        
        if tab_text == "Sell" :
            entries = sellentry_entries + sellpersonel_entries
            labelscanner.stop()
            labelscanner.update(widgets=sellentry_entries , operation= "entry")
            labelscanner.start()

        print(tab_text)

    def frameconfig(event):
        canvas.configure(scrollregion=Canvas.bbox("all"))

    def mousewheel(event):
        canvas.yview_scroll(int(-1*(event.delta/120)), "units")


class TabFunction :
    def build(root,conn,scanner): ##Builds, and packs everything to the provided frame, or window
        global Conn
        global labelscanner
        labelscanner = scanner
        Conn   = conn
        billno = 0

        ##Creates a notebook widget, that allows the tab functionality
        Entryframe = ttk.Notebook(root) 
        Entryframe.pack(fill='both',expand=True)



        ############################################################################
        ############################## Buy tab design ##############################
        ############################################################################

        BuyTab = ttk.Frame(root)
        Entryframe.add(BuyTab,text='Buy')

        #Functionality
        """canvas = Canvas(BuyTab)
        scrollbar = Scrollbar(BuyTab, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side='right',fill='y')
        canvas.pack(side='left',fill='both',expand='true')

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor='nw')
        frame.bind("<Configure>", OnTabEvents.frameconfig)"""

        ##BuyBill table instance
        global buybill_frame,buybill_table,buyerrorlabel
        buybillblock  = GUItool.Table.billtable(billno,BuyTab)
        buybill_frame = buybillblock[0]
        buybill_table = buybillblock[1]
        buyerrorlabel = buybillblock[2]

        ##Item entry instance
        global buyentry_frame,buyentry_entries
        buyentryblock    = GUItool.Frames.entryframe(BuyTab,buybill_table)
        buyentry_frame   = buyentryblock[0]
        buyentry_entries = buyentryblock[1]

        ##Personel entry instance
        global buypersonel_frame,buypersonel_entries
        buypersonelblock    = GUItool.Frames.personelframe(conn,BuyTab)
        buypersonel_frame   = buypersonelblock[0]
        buypersonel_entries = buypersonelblock[1]

        ##Buttons
        #buybutton  = Button(BuyTab,  text="Buy" , command= lambda : Controller.savebill("Buy"))

        #Packing
        buyentry_frame.pack(fill='both',expand=True,padx=10)
        buybill_frame.pack(fill='both',expand=True,padx=10)
        buypersonel_frame.pack(fill='both',expand=True,padx=10)
        
        #############################################################################
        ############################## Sell tab design ##############################
        #############################################################################
        
        SellTab = ttk.Frame(Entryframe)
        Entryframe.add(SellTab,text="Sell")
        ##BuyBill table instance
        global sellbill_frame,sellbill_table,sellerrorlabel
        sellbillblock  = GUItool.Table.billtable(billno,SellTab)
        sellbill_frame  = sellbillblock[0]
        sellbill_table = sellbillblock[1]
        sellerrorlabel = sellbillblock[2]

        ##Item entry instance
        global sellentry_frame,sellentry_entries
        sellentryblock    = GUItool.Frames.entryframe(SellTab,buybill_table)
        sellentry_frame   = sellentryblock[0]
        sellentry_entries = sellentryblock[1]

        ##Personel entry instance
        global sellpersonel_frame,sellpersonel_entries
        sellpersonelblock    = GUItool.Frames.personelframe(conn,SellTab)
        sellpersonel_frame   = sellpersonelblock[0]
        sellpersonel_entries = sellpersonelblock[1]

        #Packing
        sellentry_frame.pack(fill='both',expand=True,padx=10)
        sellbill_frame.pack(fill='both',expand=True,padx=10)
        sellpersonel_frame.pack(fill='both',expand=True,padx=10)

        #Buttons
        #sellbutton = Button(SellTab, text="Sell", command= lambda : Controller.savebill("Sell"))




        ##Binds
        Entryframe.bind     ("<<NotebookTabChanged>>", OnTabEvents.scannerfocus)



    """ buybill_table.bind           ('<<TreeviewSelect>>', lambda event : Controller.fillfromtable())
        buyentry_entries[0].bind     ('<Tab>'             , lambda event : Controller.fillfromdb(conn,"Item"))
        buypersonel_entries[0].bind  ('<Tab>'             , lambda event : Controller.fillfromdb(conn,"Personel"))


        sellbill_table.bind           ('<<TreeviewSelect>>', lambda event : Controller.fillfromtable())
        sellentry_entries[0].bind     ('<Tab>'             , lambda event : Controller.fillfromdb(conn,"Item"))
        sellpersonel_entries[0].bind  ('<Tab>'             , lambda event : Controller.fillfromdb(conn,"Personel"))
"""
        ##Buttons


    
