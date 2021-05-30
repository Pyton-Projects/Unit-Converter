from tkinter import *
from ttkthemes import*
import tkinter.ttk
from tkinter import messagebox
root=Tk()
root.title('Unit Converter')
root.geometry('600x195')
root.maxsize(600,195)
root.minsize(600,195)
def legth_converter():
	try:
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Meter':
				output=(float(input_system1.get())*1000)
				string=f'Result-:{input_system1.get()} KiloMeter = {output} Meter'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string)
				value_goes_len.place(x=1,y=175)
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Centimeter':
				output_1=(float(input_system1.get())*100000)

				string_1=f'Result-:{input_system1.get()} KiloMeter = {output_1} Centimeter'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_1)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Millimeter':
				output_2=(float(input_system1.get())*1e+6)
				string_2=f'Result-:{input_system1.get()} KiloMeter = {output_2} Millimeter'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_2)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Micrometers':
				output_3=(float(input_system1.get())*1e+9)
				string_3=f'Result-:{input_system1.get()} KiloMeter = {output_3} Micrometers'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_3)
				value_goes_len.place(x=1,y=175)# remember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Nanometers':
				output_4=(float(input_system1.get())*1e+12)
				string_4=f'Result-:{input_system1.get()} KiloMeter = {output_4} Nanometers'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_4)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Mile':
				output_5=(float(input_system1.get())/1.609)
				string_5=f'Result-:{input_system1.get()} KiloMeter = {output_5} Mile'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_5)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Yards':
				output_6=(float(input_system1.get())*1093.61)
				string_6=f'Result-:{input_system1.get()} KiloMeter = {output_6} Yards'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_6)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Foot':
				output_7=(float(input_system1.get())*3281)
				string_7=f'Result-:{input_system1.get()} KiloMeter = {output_7} Foot'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_7)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Inch':
				output_8=(float(input_system1.get())*39370)
				string_8=f'Result-:{input_system1.get()} KiloMeter = {output_8} Foot'
				value_goes_len.delete(0,END)
				value_goes_len.insert(1,string_8)
				value_goes_len.place(x=1,y=175)# rember to push!
				
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='Natucail mile':
				error_handle=float(input_system1.get())/1.852
				error_handle_1=f'Result-:{input_system1.get()} KiloMeter = {error_handle} Natucail mile'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,error_handle_1)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='KiloMeter' and LENGTH_tracker_to.get()=='KiloMeter':
				output_10=float(input_system1.get())
				string_10=f'Result-:{input_system1.get()} KiloMeter = {output_10} KiloMeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_10)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='KiloMeter':
				output_11=float(input_system1.get())/1000
				string_11=f'Result-:{input_system1.get()} Meter = {output_11} KiloMeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_11)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Centimeter':
				output_12=float(input_system1.get())*100
				string_12=f'Result-:{input_system1.get()} Meter = {output_12} Centimeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_12)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Millimeter':
				output_13=float(input_system1.get())*1000
				string_13=f'Result-:{input_system1.get()} Meter = {output_13} Millimeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_13)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Micrometers':
				output_14=float(input_system1.get())*1e+6
				string_14=f'Result-:{input_system1.get()} Meter = {output_14} Micrometers'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_14)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Nanometers':
				output_15=float(input_system1.get())*1e+9
				string_15=f'Result-:{input_system1.get()} Meter = {output_15} Nanometers'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_15)
				value_goes_len.place(x=1,y=175)# rember to push!
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Mile':
				output_16=float(input_system1.get())/1609
				string_16=f'Result-:{input_system1.get()} Meter = {output_16} Mile'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_16)
				value_goes_len.place(x=1,y=175)# rember to push! # SOEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Yards':
				output_17=float(input_system1.get())*1.094
				string_17=f'Result-:{input_system1.get()} Meter = {output_17} Yards'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_17)
				value_goes_len.place(x=1,y=175)# rember to push! # SOEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Foot':
				output_18=float(input_system1.get())*3.281
				string_18=f'Result-:{input_system1.get()} Meter = {output_18} Foot'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_18)
				value_goes_len.place(x=1,y=175)# rember to push! # SOEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Inch':
				output_19=float(input_system1.get())*39.37
				string_19=f'Result-:{input_system1.get()} Meter = {output_19} Inch'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_19)
				value_goes_len.place(x=1,y=175)# rember to push! # SOEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Natucail mile':
				output_20=float(input_system1.get())/1852
				string_20=f'Result-:{input_system1.get()} Meter = {output_20} Natucail mile'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_20)
				value_goes_len.place(x=1,y=175)# rember to push! # SOEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Meter' and LENGTH_tracker_to.get()=='Meter':
				output_21=float(input_system1.get())
				string_21=f'Result-:{input_system1.get()} Meter = {output_21} Meter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_21)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='KiloMeter':
				output_22=float(input_system1.get())/100000
				string_22=f'Result-:{input_system1.get()} Centimeter = {output_22} Centimeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_22)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Meter':
				output_23=float(input_system1.get())/100
				string_23=f'Result-:{input_system1.get()} Centimeter = {output_23} Meter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_23)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Millimeter':
				output_24=float(input_system1.get())*10
				string_24=f'Result-:{input_system1.get()} Centimeter = {output_24} Millimeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_24)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Micrometers':
				output_25=float(input_system1.get())*10000
				string_25=f'Result-:{input_system1.get()} Centimeter = {output_25} Micrometers'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_25)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Nanometers':
				output_26=float(input_system1.get())*1e+7
				string_26=f'Result-:{input_system1.get()} Centimeter = {output_26} Nanometers'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_26)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Mile':
				output_27=float(input_system1.get())/160934
				string_27=f'Result-:{input_system1.get()} Centimeter = {output_27} Mile'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_27)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Yards':
				output_28=float(input_system1.get())/91.44
				string_28=f'Result-:{input_system1.get()} Centimeter = {output_28} Yards'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_28)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Foot':
				output_29=float(input_system1.get())/30.84
				string_29=f'Result-:{input_system1.get()} Centimeter = {output_29} Foot'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_29)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Inch':
				output_30=float(input_system1.get())/2.54
				string_30=f'Result-:{input_system1.get()} Centimeter = {output_30} Inch'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_30)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Natucail mile':
				output_31=float(input_system1.get())/185200
				string_31=f'Result-:{input_system1.get()} Centimeter = {output_31} Natucail mile'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_31)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR
			if LENGTH_tracker_FRom.get()=='Centimeter' and LENGTH_tracker_to.get()=='Centimeter':
				output_32=float(input_system1.get())
				string_32=f'Result-:{input_system1.get()} Centimeter = {output_32} Centimeter'
				value_goes_len.delete(0,END)# smart paper
				value_goes_len.insert(1,string_32)
				value_goes_len.place(x=1,y=175)# rember to push! # SPEAKER TRANSALTOR



			'''--------------------------------------------------------'''

	except:
			messagebox.showinfo('Info','Please Enter A Vaild Number!')
			value_goes_len.delete(0,END)# smart paper
			value_goes_len.place(x=12323,y=175) 
tracking_unit=StringVar()
Frequency_tracker_to=StringVar()
Frequency_tracker_from=StringVar()
tracking_input=StringVar()
LENGTH_tracker_FRom=StringVar()
LENGTH_tracker_to=StringVar()
LENGTH_converter_value_TO=('KiloMeter','Meter','Centimeter','Millimeter','Micrometers','Nanometers','Mile','Yards','Foot','Inch','Natucail mile')
LENGTH_converter_value_FROM=('KiloMeter','Meter','Centimeter','Millimeter','Micrometers','Nanometers','Mile','Yards','Foot','Inch','Natucail mile')
Combobox_for_length_converter_to=tkinter.ttk.Combobox(root,value=LENGTH_converter_value_TO,textvariable=LENGTH_tracker_to)
Combobox_for_length_converter_from=tkinter.ttk.Combobox(root,value=LENGTH_converter_value_FROM,textvariable=LENGTH_tracker_FRom)
Combobox_for_length_converter_to['state']='readonly'
Combobox_for_length_converter_from['state']='readonly'
from_label=Label(root,text=None,font=('Courier',13,'bold'))
to_Label=Label(root,text=None,font=('Courier',50,'bold'))
input_system=Entry(root,width=10)
convert_button_1=frquency=tkinter.ttk.Button(root,text='Convert',command=legth_converter)
input_system1=Entry(root,width=10)
def conversion():
	if tracking_unit.get()=='Length':
		messagebox.showinfo('Message',f'Your Length Converter Ready See Down Below')
		Combobox_for_length_converter_to.place(x=350,y=100)# take input down below'
		Combobox_for_length_converter_from.place(x=100,y=100)
		from_label.config(text='From:')
		to_Label.config(text=u'\u2192')
		from_label.place(x=45,y=100)
		to_Label.place(x=266,y=60)
		convert_button_1.place(x=250,y=140)
		input_system1.place(x=145,y=130)
		input_system.place(x=22222,y=4323)
		indicator.place(x=1,y=130)
heading=Label(root,text='Select A Unit To Convert From Down Below',font=('Courier',13,'bold'))
heading.pack()
to_value=("Time","Volume","Tempreature","Speed","Mass","Length","Energy","Digital Storage","Data Transfer Rate")
slection=tkinter.ttk.Combobox(root,values=to_value,textvariable=tracking_unit)
slection.pack()
slection['state']='readonly'
Select_=tkinter.ttk.Button(root,text='Select Unit',command=conversion)
Select_.place(x=255,y=55)
indicator=Label(root,text='Enter Value To Convert--:',font=('Arial',9))
output_op_text_len=StringVar()
value_goes_len=Entry(root,font=('Arial',10))
output_op_text_frequency=StringVar()
value_goes_freq=Entry(root,font=('Arial',10))
root.mainloop()
# a bot that can convert  big english sentence to small senctence using other words!!! 
# s software that can get color value froma int or hexadecimel number!!
# unit converter
# enache rock paper siccors!!
# a app that can help to lern python a kivy app idea!
# a app that can tech you python a kivy app idea!
# create a game using pygame!!
# complete python from book!!!
# from to = value
# copy paste bot unit converter enachne rock paper scissors game bas!
# software that can detect sound,a softawre that can get color value from a int
# enachen rock paper siccors!
# unit converter!!
