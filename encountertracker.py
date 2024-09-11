import tkinter as tk
import tkinter.simpledialog

import active_encounter as encounter

## Button Functions to communicate to active_encounter
def add_character(root: tk.Tk,
                  enc_state: encounter.EncounterStorage):
    char_n = tkinter.simpledialog.askstring('Add Character', 'Enter character name')
    if char_n != '' or char_n != None:
        enc_state.add_character(char_n)
        # Update listbox
        lstbox: tk.Listbox = root.pack_slaves()[0].pack_slaves()[1]
        lstbox.delete(0, tk.END)
        for char in enc_state.characters:
            lstbox.insert(0, char)

def clear_all(root: tk.Tk,
              enc_state: encounter.EncounterStorage):
    clear_characters(root, enc_state)
    # TODO, clear combat

def clear_characters(root: tk.Tk,
                     enc_state: encounter.EncounterStorage):
    lstbox: tk.Listbox = root.pack_slaves()[0].pack_slaves()[1]
    lstbox.delete(0, tk.END)
    enc_state.characters = []


## Window setup and mainloop
VERSION = '0.1'
# Window setup
root = tk.Tk()
root.geometry('500x350')
root.resizable(False, False)
root.title(f'D&D Encounter Tracker -- {VERSION}')

# Menu
mainmenu = tk.Menu(root)
mainmenu.add_command(label='Open', command=None)
mainmenu.add_command(label='Save', command=None)
clear_menu = tk.Menu(mainmenu, tearoff=0)
clear_menu.add_command(label='All', command=lambda: clear_all(root, enc_state))
clear_menu.add_command(label='Characters', command=lambda: clear_characters(root, enc_state))
clear_menu.add_command(label='Combat', command=None)
mainmenu.add_cascade(label='Clear', menu=clear_menu)
root.config(menu=mainmenu)
# Create data storage object
enc_state = encounter.create_encounter_instance()

# Character panel
char_panel = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=250)
char_lb = tk.Label(char_panel, text='Characters')
char_list = tk.Listbox(char_panel, selectmode=tk.SINGLE)
add_char = tk.Button(char_panel, text='Add', command=lambda: add_character(root, enc_state))
remove_char = tk.Button(char_panel, text='Remove')
# Packing
char_panel.pack(side=tk.LEFT, expand=True, fill='both')
char_lb.pack()
char_list.pack(expand=True, fill='both')
add_char.pack(expand=True, fill='both')
remove_char.pack(expand=True, fill='both')

# Next Turn Button
next_turn = tk.Button(root, width=20, text='Next Turn', bg='light grey')
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
