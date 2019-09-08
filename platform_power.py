import tkinter as tk
from tkinter import *
import telnetlib
import os

ip = ""
telnet_flag = 0

def update_Label(txt):
    result.set(txt)

def PS_tuggle(port, command):
    if (port not in range(1, 9)) or len(str(port)) != 1:
        update_Label("port is\nout of range")

    elif telnet_flag == 0:
        update_Label("Connect first!")
    else:
        global ip
        APC = telnetlib.Telnet(ip, 23)

        APC.read_until("Login:")
        APC.write(b'teladmin\r\n')
        APC.read_until("Password:")
        APC.write(b'telpwd\r\n')
        APC.read_until("> ")

        if command == "On":
            APC.write(b'sw o0' + str(port) + ' on imme\r\n')
        if command == "Off":
            APC.write(b'sw o0' + str(port) + ' off imme\r\n')

        APC.read_until("Outlet<0"+str(port)+"> command is setting")
        update_Label('Command executed Successfully')

        APC.close()

def get_PS_IP():
    global ip
    ip = PS_IP.get()
    response = os.system("ping -n 1 " + ip)

    if response == 0:
        global telnet_flag
        telnet_flag = 1
        update_Label("Connection\nis OK")
    else:
        global telnet_flag
        telnet_flag = 0
        update_Label("no PING\nto PS")

if __name__ == '__main__':
    telnet_flag = 0

    root = tk.Tk()
    root.title("Power Switch Controller")
    root.iconbitmap("Intel.ico")
    root.minsize(width=400, height=115)

    switch_frame = Frame(root)
    switch_frame.pack()

    ##Power Switch ROW##
    ps_lbl = Label(switch_frame, text="Power Switch IP:")
    ps_lbl.grid(column=0, row=0)
    PS_IP = StringVar()
    txt = Entry(switch_frame, width=10, textvariable=PS_IP)
    txt.grid(column=1, row=0)
    connect_Button = Button(switch_frame, text="Connect", width=8, command=get_PS_IP)
    connect_Button.grid(column=2, row=0)
    ##AX6K ROW##
    AX6K_lbl = Label(switch_frame, text="AXEPOINT 6000", width=15)
    AX6K_lbl.grid(row=2, column=0)

    AX6K_PS_lbl = Label(switch_frame, text="Outlet (1-8):")
    AX6K_PS_lbl.grid(row=2, column=3)

    AX6K_PS_PORT = IntVar(value=0)
    AX6K_PORT_window = Entry(switch_frame, width=5, textvariable=AX6K_PS_PORT, font='Helvetica 10 bold')
    AX6K_PORT_window.grid(row=2, column=4)

    AX6K_switch = IntVar(value=-1)
    AX6K_off = Radiobutton(switch_frame, text="Off", variable=AX6K_switch, indicatoron=False, value=0, width=8,
                           command=lambda: PS_tuggle(AX6K_PS_PORT.get(), "Off"))
    AX6K_on = Radiobutton(switch_frame, text="On", variable=AX6K_switch, indicatoron=False, value=1, width=8,
                          command=lambda: PS_tuggle(AX6K_PS_PORT.get(), "On"))
    AX6K_off.grid(row=2, column=1)
    AX6K_on.grid(row=2, column=2)
    ##AX3K ROW##
    AX3K_lbl = Label(switch_frame, text="AXEPOINT 3000", width=15)
    AX3K_lbl.grid(row=3, column=0)

    AX3K_PS_lbl = Label(switch_frame, text="Outlet (1-8):")
    AX3K_PS_lbl.grid(row=3, column=3)

    AX3K_PS_PORT = IntVar(value=0)
    AX3K_PORT_window = Entry(switch_frame, width=5, textvariable=AX3K_PS_PORT, font='Helvetica 10 bold')
    AX3K_PORT_window.grid(row=3, column=4)

    AX3K_switch = IntVar(value=-1)
    AX3K_off = Radiobutton(switch_frame, text="Off", variable=AX3K_switch, indicatoron=False, value=0, width=8,
                           command=lambda: PS_tuggle(AX3K_PS_PORT.get(), "Off"))
    AX3K_on = Radiobutton(switch_frame, text="On", variable=AX3K_switch, indicatoron=False, value=1, width=8,
                          command=lambda: PS_tuggle(AX3K_PS_PORT.get(), "On"))
    AX3K_off.grid(row=3, column=1)
    AX3K_on.grid(row=3, column=2)
    ##CGR ROW##
    CGR_lbl = Label(switch_frame, text="CGR 4X4", width=15)
    CGR_lbl.grid(row=4, column=0)

    CGR_PS_lbl = Label(switch_frame, text="Outlet (1-8):")
    CGR_PS_lbl.grid(row=4, column=3)

    CGR_PS_PORT = IntVar(value=0)
    CGR_PORT_window = Entry(switch_frame, width=5, textvariable=CGR_PS_PORT, font='Helvetica 10 bold')
    CGR_PORT_window.grid(row=4, column=4)

    CGR_switch = IntVar(value=-1)
    CGR_off = Radiobutton(switch_frame, text="Off", variable=CGR_switch, indicatoron=False, value=0, width=8,
                          command=lambda: PS_tuggle(CGR_PS_PORT.get(), "Off"))
    CGR_on = Radiobutton(switch_frame, text="On", variable=CGR_switch, indicatoron=False, value=1, width=8,
                         command=lambda: PS_tuggle(CGR_PS_PORT.get(), "On"))
    CGR_off.grid(row=4, column=1)
    CGR_on.grid(row=4, column=2)
    ##Status Label##
    result = StringVar()
    result.set("Progress")
    result_lbl = Label(switch_frame, textvariable=result, width=15, fg="white", bg="black", font='Helvetica 10 bold')
    result_lbl.grid(row=5, column=0)
    root.mainloop()
