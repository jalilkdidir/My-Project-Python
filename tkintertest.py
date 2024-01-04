from tkinter import *
from tkinter import ttk
from attr import frozen
from ttkbootstrap import Style
from adbutils import adb

style = Style()

root = style.master
style = Style(theme='solar')
root.geometry('700x600')
root.resizable(False,False)

# notebook

nb = ttk.Notebook(root,width=700,height=100)
frm1= Frame(root,bg='silver')
frm2=Frame(root,bg='silver')
frm3= Frame(root,bg='silver')
frm4=Frame(root,bg='silver')
frm5= Frame(root,bg='silver')
frm6=Frame(root,bg='silver')
import subprocess



# frams 

nb.add(frm1,text='ADB')
nb.add(frm2,text='MTK')
nb.add(frm3,text='SPD')
nb.add(frm4,text='Qualcomm')
nb.add(frm5,text='Xiaomi')
nb.add(frm6,text='Fastboot')
nb.grid()


# Define the ADB path if it's not in your system environment variables
adb_path = "C:/Users/jalil/Desktop/ppython/adb.exe"


# All def def def def def 

def get_devices_list():
  devices_list = []
  process = subprocess.Popen([adb_path, "devices"], stdout=subprocess.PIPE)
  output, error = process.communicate()
  output = output.decode().strip()

  for line in output.splitlines():
    if line.startswith("List of devices attached"):
      continue
    device_id, device_status = line.split("\t")
    if device_status == "device":
      devices_list.append(device_id)
  return devices_list


# def reboot

def reboot ():
   
   # ADB command to reboot the device
   adb_reboot_command = [adb_path, "reboot"]

   try:
    # Run the ADB command to reboot the device
    subprocess.run(adb_reboot_command, check=True)
    info_text.config(state=NORMAL)
    info_text.delete(1.0, END)
    info_text.insert(END, "Reboot command sent successfully.")
    

   except subprocess.CalledProcessError as e:
    info_text.config(state=NORMAL)
    info_text.delete(1.0, END)
    info_text.insert(END, "Error rebooting the device :\nPlease Connect Your Device . . . ",frozen)
    #print(f"Error rebooting the device: {e}")



def get_device_info():
    devices = adb.device_list()

    info_text.config(state=NORMAL)
    info_text.delete(1.0, END)

    if not devices:
        info_text.insert(END, "No devices connected.")
    else:
        for device in devices:
            info_text.insert(END, "Device Serial: {}\n".format(device.serial))
            info_text.insert(END, "Device Name: {}\n".format(device.getprop("ro.vendor.oplus.market.name")))
            info_text.insert(END, "Firmware Version: {}\n".format(device.getprop("ro.build.display.id")))
            info_text.insert(END,"Device Name: {}\n".format(device.getprop("ro.vendor.oplus.market.name")))
            info_text.insert(END,"Firmware Version: {}\n".format(device.getprop("ro.build.display.id")))
            info_text.insert(END,"Device Security Patch: {}\n".format(device.getprop("ro.build.version.security_patch")))
            info_text.insert(END,"Device Model Name: {}\n".format(device.getprop("ro.product.model")))
            info_text.insert(END,"Device Manufacturer: {}\n".format(device.getprop("ro.product.manufacturer")))
            info_text.insert(END,"Device Version: {}\n".format(device.getprop("ro.build.version.release\n")))
            info_text.insert(END,"Device Contry : {}\n".format(device.getprop("gsm.operator.iso-country\n"))) 
            info_text.insert(END,"Device CPU: {}\n".format(device.getprop("ro.product.cpu.abi")))
            info_text.insert(END,"Device Manufacturer CPU: {}\n".format(device.getprop("ro.soc.manufacturer")))
            info_text.insert(END,"Device Model: {}\n".format(device.getprop("ro.soc.model"))) 
            info_text.insert(END,"Device Sim Contry: {}\n".format(device.getprop("sys.sim.switch.current")))
            info_text.insert(END,"Device Network Type: {}\n".format(device.getprop("gsm.network.type")))
            info_text.insert(END,"Device Baseband: {}\n".format(device.getprop("gsm.version.baseband")))
            info_text.insert(END,"Device Bootloader: {}\n".format(device.getprop("ro.boot.vbmeta.device_state")))
            info_text.insert(END,"Device Fingerprint: {}\n".format(device.getprop("ro.bootimage.build.fingerprint")))
            info_text.insert(END,"Device full ID: {}\n".format(device.getprop("ro.build.display.full_id")))
            info_text.insert(END,'')
            
            info_text.insert(END,'')
            

            info_text.insert(END, "\n")  # Add a newline between devices

            # Add more properties as needed

        info_text.insert(END, "Done\n\n")
    info_text.config(state=DISABLED)    


##########################
# ADB command and button #
##########################


device_combo = ttk.Combobox(frm1,height=1,width=18)
device_combo["values"] = get_devices_list()
device_combo.grid(row=0,column=0)

b1 = ttk.Button(frm1, text='info', bootstyle='primar',width=11, command=get_device_info)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm1, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm1, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm1, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm1, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm1, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm1, text='Reboot', bootstyle='primar',width=11,command=reboot)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm1, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm1, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2) 


########################
# MTK command and button#
########################


b1 = ttk.Button(frm2, text='info', bootstyle='primar',width=11)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm2, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm2, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm2, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm2, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm2, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm2, text='Reboot', bootstyle='primar',width=11)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm2, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm2, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2)



##########################
# SPD command and button #
##########################


b1 = ttk.Button(frm3, text='info', bootstyle='primar',width=11)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm3, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm3, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm3, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm3, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm3, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm3, text='Reboot', bootstyle='primar',width=11)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm3, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm3, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2)


###############################
# QUALCOMM command and button #
###############################


b1 = ttk.Button(frm4, text='info', bootstyle='primar',width=11)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm4, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm4, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm4, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm4, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm4, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm4, text='Reboot', bootstyle='primar',width=11)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm4, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm4, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2)


#############################
# XIAOMI command and button #
#############################


b1 = ttk.Button(frm5, text='info', bootstyle='primar',width=11)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm5, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm5, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm5, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm5, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm5, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm5, text='Reboot', bootstyle='primar',width=11)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm5, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm5, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2)


#############################
# XIAOMI command and button #
#############################


device_combo = ttk.Combobox(frm6,height=1,width=18)
device_combo.grid(row=0,column=0)

b1 = ttk.Button(frm6, text='info', bootstyle='primar',width=11)
b1.grid(row=0,column=2,padx=2)

b1 = ttk.Button(frm6, text='FRP', bootstyle='primar',width=11)
b1.grid(row=0,column=3,padx=2)

b1 = ttk.Button(frm6, text='Reset ID', bootstyle='primar',width=11)
b1.grid(row=0,column=4,padx=2)

b1 = ttk.Button(frm6, text='APP info', bootstyle='primar',width=11)
b1.grid(row=0,column=5,padx=2)

b1 = ttk.Button(frm6, text='install APP', bootstyle='primar',width=11)
b1.grid(row=0,column=6,padx=2)

b1 = ttk.Button(frm6, text='unistall APP', bootstyle='primar',width=11)
b1.grid(row=0,column=7,padx=2)

b1 = ttk.Button(frm6, text='Reboot', bootstyle='primar',width=11)
b1.grid(row=1,column=7,padx=2,pady=5)

b1 = ttk.Button(frm6, text='To Fastoot', bootstyle='primar',width=11)
b1.grid(row=1,column=3,padx=2)

b1 = ttk.Button(frm6, text='To Recovery', bootstyle='primar',width=11)
b1.grid(row=1,column=2,padx=2) 



info_text = Text(root, height=30, width=115)
info_text.grid()



root.mainloop()