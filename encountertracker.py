import tkinter as tk
from tkinter import simpledialog, messagebox

import active_encounter as encounter

## Button Functions to communicate to active_encounter
def add_character(root: tk.Tk,
                  enc_state: encounter.EncounterStorage):
    char_n = simpledialog.askstring('Add Character', 'Enter character name')
    if char_n != '' or char_n != None:
        enc_state.add_character(char_n)
        # Update listbox
        lstbox: tk.Listbox = root.pack_slaves()[0].pack_slaves()[1]
        lstbox.delete(0, tk.END)
        idx = 0
        for char in enc_state.characters:
            lstbox.insert(idx, char)
            idx += 1

def remove_character(root: tk.Tk,
                     selected_idx: int,
                     enc_state: encounter.EncounterStorage):
    enc_state.characters.pop(selected_idx)
    # Update listbox
    lstbox: tk.Listbox = root.pack_slaves()[0].pack_slaves()[1]
    lstbox.delete(0, tk.END)
    idx = 0
    for char in enc_state.characters:
        lstbox.insert(idx, char)
        idx += 1

def add_to_combat(root: tk.Tk,
                  selected_idx: int,
                  enc_state: encounter.EncounterStorage):
    p = enc_state.characters[selected_idx]
    init = simpledialog.askinteger('Add to Combat', f'Enter Initiative for {p}')
    if init != None:
        enc_state.add_combatant(p, init)
        # Update combat box
        lstbox: tk.Listbox = root.pack_slaves()[2].pack_slaves()[1]
        lstbox.delete(0, tk.END)
        idx = 0
        for combat in enc_state.combatants:
            lstbox.insert(idx, combat['Name'])
            idx += 1
            # Highlight top combatant
            lstbox.itemconfig(0, bg='yellow')

def start_next_turn(root: tk.Tk,
                    enc_state: encounter.EncounterStorage):
    lstbox: tk.Listbox = root.pack_slaves()[2].pack_slaves()[1]
    next = enc_state.next_turn()
    # Update combat box
    lstbox.delete(0, tk.END)
    idx = 0
    # Re-build
    for combat in enc_state.combatants:
        lstbox.insert(idx, combat['Name'])
        # Check if current
        if combat['Name'] == next['Name']:
            lstbox.itemconfig(idx, bg='yellow')
        idx += 1

def display_selected_init(root: tk.Tk,
                          selected_idx: int,
                          enc_state: encounter.EncounterStorage):
    p = enc_state.combatants[selected_idx]
    messagebox.showinfo(f'{p['Name']}', f'Initiative for {p['Name']}: {p['Initiative']}')

def clear_all(root: tk.Tk,
              enc_state: encounter.EncounterStorage):
    clear_characters(root, enc_state)
    clear_combat(root, enc_state)

def clear_characters(root: tk.Tk,
                     enc_state: encounter.EncounterStorage):
    lstbox: tk.Listbox = root.pack_slaves()[0].pack_slaves()[1]
    lstbox.delete(0, tk.END)
    enc_state.characters = []

def clear_combat(root: tk.Tk,
                 enc_state: encounter.EncounterStorage):
    if len(enc_state.combatants) > 1:
        lstbox: tk.Listbox = root.pack_slaves()[2].pack_slaves()[1]
        lstbox.delete(0, tk.END)
        enc_state.combatants = []


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
clear_menu.add_command(label='Combat', command=lambda: clear_combat(root, enc_state))
mainmenu.add_cascade(label='Clear', menu=clear_menu)
root.config(menu=mainmenu)
# Create data storage object
enc_state = encounter.EncounterStorage()

# Character panel
char_panel = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=250)
char_lb = tk.Label(char_panel, text='Characters')
char_list = tk.Listbox(char_panel, selectmode=tk.SINGLE, justify='center')
char_list.bind('<Double-1>', func=lambda e: add_to_combat(root, char_list.curselection()[0], enc_state))
add_char = tk.Button(char_panel, text='Add', command=lambda: add_character(root, enc_state))
remove_char = tk.Button(char_panel, text='Remove', command=lambda: remove_character(root, char_list.curselection()[0], enc_state))
# Packing
char_panel.pack(side=tk.LEFT, expand=True, fill='both')
char_lb.pack()
char_list.pack(expand=True, fill='both')
add_char.pack(expand=True, fill='both')
remove_char.pack(expand=True, fill='both')

# Next Turn Button
next_turn = tk.Button(root, width=20, text='Next Turn', bg='light grey', 
                      command=lambda: start_next_turn(root, enc_state))
next_turn.pack(side=tk.LEFT, expand=True, fill='both')

# Combat Panels
combat_panel = tk.Frame(root, highlightbackground='black', highlightthickness=1, width=250)
combat_lb = tk.Label(combat_panel, text='Combat')
combat_list = tk.Listbox(combat_panel, selectmode=tk.NONE, justify='center')
combat_list.bind('<Double-1>', func=lambda e: display_selected_init(root, combat_list.curselection()[0], enc_state))
# Packing
combat_panel.pack(side=tk.LEFT, expand=True, fill='both')
combat_lb.pack()
combat_list.pack(expand=True, fill='both')

# Main loop
root.mainloop()
