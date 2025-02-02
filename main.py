import tkinter
import qiskit
from qiskit import QuantumCircuit
from tkinter import PhotoImage, LEFT, END, DISABLED, NORMAL
from qiskit.visualization import visualize_transition
import numpy as np
import warnings

warnings.filterwarnings("ignore")
#define the window for the app
root = tkinter.Tk()
root.title("Quantum eyes")
#set the icon
try:
    icon = PhotoImage(file='./icon.png')  # Change to .png if needed
    root.iconphoto(True, icon)

except Exception as e:
    print(f"Error loading icon: {e}")

root.geometry('410x350')
root.resizable(0,0) #(x,y) direction allowance ##done this to block the resizing of the window

#defining the colors and fonts
background='#2c94c8'
buttons='#834558'
special_buttons = '#bc3454'
button_font=('Futura', 18)
display_font=('Futura', 32)

#define the frames of the app
display_frame = tkinter.LabelFrame(root)
button_frame=tkinter.LabelFrame(root, bg='black')
display_frame.pack()
button_frame.pack(fill="both", expand=True)

#define the display frame of the app 
display = tkinter.Entry(display_frame, width=120, font=display_font, bg=background, borderwidth=10, justify=LEFT)
display.pack(padx=3, pady=4)

#the functions

###initialising quantum circuit
def initialize_circuit():
    global circuit
    circuit=QuantumCircuit(1)  ##use only one qubit try how 2 qubits can be made to work

initialize_circuit()
theta=0

###about
def about():
    info=tkinter.Tk()
    info.title("About")
    info.geometry('650x450')
    info.resizable(0,0)

    text=tkinter.Text(info, height=20, width= 20)
    label=tkinter.Label(info,text="about quantum eyes")
    label.config(font=("Futura", 15))
    text_to_display=""" 
        About: Visualization tool for Single Qubit Rotation on Bloch Sphere
    
        Created by : Prakhar Khurana
        Created using: Python, Tkinter, Qiskit
    
        Info about the gate buttons and corresponding qiskit commands:
    
        X = flips the state of qubit -                                 circuit.x()
        Y = rotates the state vector about Y-axis -                    circuit.y()
        Z = flips the phase by PI radians -                            circuit.z()
        Rx = parameterized rotation about the X axis -                 circuit.rx()
        Ry = parameterized rotation about the Y axis.                  circuit.ry()
        Rz = parameterized rotation about the Z axis.                  circuit.rz()
        S = rotates the state vector about Z axis by PI/2 radians -    circuit.s()
        T = rotates the state vector about Z axis by PI/4 radians -    circuit.t()
        Sd = rotates the state vector about Z axis by -PI/2 radians -  circuit.sdg()
        Td = rotates the state vector about Z axis by -PI/4 radians -  circuit.tdg()
        H = creates the state of superposition -                       circuit.h()
    
        For Rx, Ry and Rz, 
        theta(rotation_angle) allowed range in the app is [-2*PI,2*PI]
    
        In case of a Visualization Error, the app closes automatically.
        This indicates that visualization of your circuit is not possible.
    
        At a time, only ten operations can be visualized.
        """
    label.pack()
    text.pack(fill='both', expand=True)
    text.insert(END, text_to_display)
    info.mainloop()
    
###display gate
def display_gate(gate_input):
    display.insert(END,gate_input)
    input_gates=display.get()
    num_gates=len(input_gates)
    list_input=list(input_gates)
    search=["R", "D"]
    count_double=[list_input.count(i) for i in search]
    num_gates-=sum(count_double)
    if num_gates==10:
        gates=[x_g,y_g,z_g,rx_g,ry_g,rz_g,s_g,sd_g,t_g,td_g,h_g]
        for gate in gates:
            gate.config(state=DISABLED)

###clear
def clear_f(circuit):
    display.delete(0, END)
    initialize_circuit()
    if x_g['state']==DISABLED:
        gates=[x_g,y_g,z_g,rx_g,ry_g,rz_g,s_g,sd_g,t_g,td_g,h_g]
        for gate in gates:
            gate.config(state=NORMAL)

###change theta
def change_theta(num, window, circuit, key):
    global theta
    theta=num*np.pi
    if key=="x":
        circuit.rx(theta, 0)
        theta=0
    elif key=='y':
        circuit.ry(theta,0)
        theta=0
    else:
        circuit.rz(theta, 0)
        theta=0
    window.destroy()
    
###user_input
def user_input(circuit, key):
    get_input=tkinter.Tk()
    get_input.title("get angle")
    get_input.geometry('360x160')
    get_input.resizable(0,0)
    val1=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='π/4', command=lambda:change_theta(0.25, get_input, circuit, key))
    val1.grid(row=0, column=0)
    val2=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='π/2', command=lambda:change_theta(0.50, get_input, circuit, key))
    val2.grid(row=0, column=1)
    val3=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='π', command=lambda:change_theta(1.00, get_input, circuit, key))
    val3.grid(row=0, column=2)
    val4=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='2π', command=lambda:change_theta(2.00, get_input, circuit, key))
    val4.grid(row=0, column=3, sticky='W')
    nval1=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='-π/4', command=lambda:change_theta(-0.25, get_input, circuit, key))
    nval1.grid(row=1, column=0)
    nval2=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='-π/2', command=lambda:change_theta(-0.50, get_input, circuit, key))
    nval2.grid(row=1, column=1)
    nval3=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='-π', command=lambda:change_theta(-1.00, get_input, circuit, key))
    nval3.grid(row=1, column=2)
    nval4=tkinter.Button(get_input, height=2, width=5, bg=buttons, font=("Futura", 10), text='-2π', command=lambda:change_theta(-2.00, get_input, circuit, key))
    nval4.grid(row=1, column=3, sticky='W')


    note="The value of theta can range from [-2π to 2π]"
    ct=tkinter.Text(get_input, height=20, width=50, bg='black')
    ct.grid(sticky='WE', columnspan=6)
    ct.insert(END, note)
    get_input.mainloop()

###visualise circuit
def visualize_circuit(circuit, window):
    try:
        visualize_transition(circuit=circuit, trace=True, fpg=100, spg=5)
    except qiskit.visualization.exceptions.VisualizationError:
        window.destroy()
    

#the first row of buttons
x_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="X", command=lambda:[display_gate("x"), circuit.x(0)])
y_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="Y",command=lambda:[display_gate("y"), circuit.y(0)])
z_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="Z",command=lambda:[display_gate("z"), circuit.z(0)])
x_g.grid(row=0, column=0, ipadx=45, pady=1)
y_g.grid(row=0, column=1, ipadx=45, pady=1)
z_g.grid(row=0, column=2, ipadx=45, pady=1, sticky="E")

#the second row of buttons 
rx_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="RX", command=lambda:[display_gate("Rx"), user_input(circuit, 'x')])
ry_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="RY", command=lambda:[display_gate("Ry"), user_input(circuit, 'y')])
rz_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text="RZ", command=lambda:[display_gate("Rz"), user_input(circuit, 'z')])
rx_g.grid(row=1,column=0, columnspan=1, sticky='WE', pady=1)
ry_g.grid(row=1,column=1, columnspan=1, sticky='WE', pady=1)
rz_g.grid(row=1,column=2, columnspan=1, sticky='WE', pady=1)

#the third row of buttons
s_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text='S', command=lambda:[display_gate("s"), circuit.s(0)])
sd_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text='SD', command=lambda:[display_gate("SD"), circuit.sdg(0)])
h_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text='H', command=lambda:[display_gate("H"), circuit.h(0)])
s_g.grid(row=2, column=0, columnspan=1, sticky='WE', pady=1)
sd_g.grid(row=2, column=1, sticky='WE', pady=1)
h_g.grid(row=2, column=2, rowspan=2, sticky='WENS', pady=1)

#the fifth row of buttons
t_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text='T', command=lambda:[display_gate("t"), circuit.t(0)])
td_g=tkinter.Button(button_frame, font=button_font, bg=buttons, text='TD', command=lambda:[display_gate("td"), circuit.tdg(0)])
t_g.grid(row=3, column=0, sticky='WE', pady=1)
td_g.grid(row=3, column=1, sticky='WE', pady=1)

#quit and visualise
quit_b=tkinter.Button(button_frame, font=button_font, bg=special_buttons, text="quit", command=root.destroy)
visualise=tkinter.Button(button_frame, font=button_font, bg=buttons, text="visualize", command=lambda:visualize_circuit(circuit, root))
quit_b.grid(row=4, column=0, columnspan=2, sticky="WE", ipadx=5, pady=1)
visualise.grid(row=4, column=2, columnspan=1, sticky="WE", ipadx=8, pady=1)

#clear and about button
clear_b=tkinter.Button(button_frame, font=button_font, bg=special_buttons, text="clear", command=lambda:clear_f(circuit))
clear_b.grid(row=5,column=0, columnspan=3, sticky="WE")
about_b=tkinter.Button(button_frame, font=button_font, bg=special_buttons, text="About", command=about)
about_b.grid(row=6, column=0, columnspan=3, sticky="WE")

root.mainloop()