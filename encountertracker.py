import tkinter as tk
from PIL import Image, ImageTk


VERSION = '0.1'
# Window setup
root = tk.Tk()
root.geometry('500x350')
root.resizable(False, False)
root.title(f'D&D Encounter Tracker -- {VERSION}')
ico = ImageTk.PhotoImage(Image.open('dnd.jpg'))
root.wm_iconphoto(False, ico)

# Character panel
char_panel = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=250)
char_lb = tk.Label(char_panel, text='Characters')
char_list = tk.Listbox(char_panel, selectmode=tk.SINGLE)
add_char = tk.Button(char_panel, text='Add')
remove_char = tk.Button(char_panel, text='Remove')
# Packing
char_panel.pack(side=tk.LEFT, expand=True, fill='both')
char_lb.pack()
char_list.pack(expand=True, fill='both')
add_char.pack(expand=True, fill='both')
remove_char.pack(expand=True, fill='both')

# Next Turn Button
next_turn = tk.Button(root, width=20, text='Next Turn')
next_turn.pack(side=tk.LEFT, expand=True, fill='both')

# Combat Panels
combat_panel = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=250)
combat_lb = tk.Label(combat_panel, text='Combat')
combat_list = tk.Listbox(combat_panel, selectmode=tk.NONE)
# Packing
combat_panel.pack(side=tk.LEFT, expand=True, fill='both')
combat_lb.pack()
combat_list.pack(expand=True, fill='both')

# Main loop
root.mainloop()