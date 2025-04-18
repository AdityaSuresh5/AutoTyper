import customtkinter
import keyboard
import pyautogui
import ollama
import time
import random
import threading  
import tkinter as tk

customtkinter.set_appearance_mode("Dark")

app = None  # Define app globally so it exists before being assigned


app = customtkinter.CTk()
height = 500
width = 700
app.geometry(f"{width}x{height}")
app.title("AutoTyper by AS")
#icon = tk.PhotoImage(file="your_icon.png")
#app.iconphoto(True, icon)

typing_active = False  

def splash_screen():
    print("Loading AutoTyper...")
    # Clear app (just in case)
    for widget in app.winfo_children():
        widget.destroy()

    app.geometry("400x400")

    splash_label = customtkinter.CTkLabel(app, text="Loading AutoTyper...", font=("Arial", 20))
    splash_label.pack(expand=True)

    # After 5 seconds, clear splash and load AutoTyper UI
    def load_main_ui():
        for widget in app.winfo_children():
            widget.destroy()
        AutoTyper()

    app.after(3000, load_main_ui)
    app.mainloop()

def AutoTyper():
    global textbox, compileButton, statusButton, splash_screen

    height = 500
    width = 700
    app.geometry(f"{width}x{height}")
    app.title("AutoTyper by AS")

    # Configure grid for app
    app.grid_rowconfigure(0, weight=0)  # OptionMenu
    app.grid_rowconfigure(1, weight=0)  # Title Row (Label, Description, Settings)
    app.grid_rowconfigure(2, weight=5)  # Textbox
    app.grid_rowconfigure(3, weight=1)  # Buttons

    app.grid_columnconfigure(0, weight=1)

    def mode_selected(choice):
        global app
        if choice == "AutoTyper + AI":
            app.destroy()
            app = customtkinter.CTk()
            AutoTyperAI()
        elif choice == "AutoTyper":
            app.destroy()
            app = customtkinter.CTk()
            AutoTyper()

    # Dropdown OptionMenu
    optionmenu = customtkinter.CTkOptionMenu(app, values=["AutoTyper", "AutoTyper + AI"], command=mode_selected)
    optionmenu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    optionmenu.set("AutoTyper")  # Set default value to "AutoTyper"

    # Title Row Frame
    title_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    title_frame.grid(row=1, column=0, padx=10, pady=10, sticky="ew")
    title_frame.grid_columnconfigure(0, weight=1)
    title_frame.grid_columnconfigure(1, weight=2)
    title_frame.grid_columnconfigure(2, weight=1)

    # Main Label
    main_label = customtkinter.CTkLabel(title_frame, text="AutoTyper", font=("Arial", 30))
    main_label.grid(row=0, column=0, sticky="w")

    # Small Description
    description_label = customtkinter.CTkLabel(title_frame,
                                               text="An open-source tool to automate typing tasks.",
                                               font=("Arial", 12), text_color="grey")
    description_label.grid(row=0, column=1, sticky="w", padx=10)

    # Settings Button
    settings_button = customtkinter.CTkButton(title_frame, text="Settings", width=100, height=35, corner_radius=20, command=setting)
    settings_button.grid(row=0, column=2, sticky="e")

    # Textbox
    textbox = customtkinter.CTkTextbox(app)
    textbox.insert("0.0", "Enter text here: ")
    textbox.grid(row=2, column=0, sticky="nsew", padx=10, pady=10)

    # Buttons Frame
    button_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    button_frame.grid(row=3, column=0, pady=10)
    button_frame.grid_columnconfigure((0, 1), weight=1)

    compileButton = customtkinter.CTkButton(button_frame, text="Compile", corner_radius=20, height=40, width=200, command=compile)
    compileButton.grid(row=0, column=0, padx=10)

    statusButton = customtkinter.CTkButton(button_frame, text="Ready", corner_radius=20, height=40, width=200)
    statusButton.grid(row=0, column=1, padx=10)


    app.mainloop()

def AutoTyperAI():
    global textbox, compileButton, statusButton, consoleTextbox, small_textbox

    height = 500
    width = 700
    app.geometry(f"{width}x{height}")
    app.title("AutoTyper by AS")

    # Configure grid for app
    app.grid_rowconfigure(0, weight=0)  # OptionMenu
    app.grid_rowconfigure(1, weight=0)  # Title Row (Label, Description, Settings)
    app.grid_rowconfigure(2, weight=0)  # Small Textbox
    app.grid_rowconfigure(3, weight=5)  # Main Textbox
    app.grid_rowconfigure(4, weight=3)  # Console Textbox
    app.grid_rowconfigure(5, weight=1)  # Buttons

    app.grid_columnconfigure(0, weight=1)

    def mode_selected(choice):
        global app
        if choice == "AutoTyper + AI":
            app.destroy()
            app = customtkinter.CTk()
            AutoTyperAI()
        elif choice == "AutoTyper":
            app.destroy()
            app = customtkinter.CTk()
            AutoTyper()

    # Dropdown OptionMenu
    optionmenu = customtkinter.CTkOptionMenu(app, values=["AutoTyper", "AutoTyper + AI"], command=mode_selected)
    optionmenu.grid(row=0, column=0, padx=10, pady=10, sticky="ew")
    optionmenu.set("AutoTyper + AI")  # Set default value to "AutoTyper + AI"


    # Title Row Frame
    title_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    title_frame.grid(row=1, column=0, padx=10, pady=5, sticky="ew")
    title_frame.grid_columnconfigure(0, weight=1)
    title_frame.grid_columnconfigure(1, weight=2)
    title_frame.grid_columnconfigure(2, weight=1)

    # Main Label
    main_label = customtkinter.CTkLabel(title_frame, text="AutoTyper + AI", font=("Arial", 30))
    main_label.grid(row=0, column=0, sticky="w")

    # Small Description
    description_label = customtkinter.CTkLabel(title_frame,
                                               text="An open-source tool to automate typing tasks, now with GenAI.",
                                               font=("Arial", 12), text_color="grey")
    description_label.grid(row=0, column=1, sticky="w", padx=11.5)

    # Settings Button
    settings_button = customtkinter.CTkButton(title_frame, text="Settings", width=100, height=35, corner_radius=20, command=setting)
    settings_button.grid(row=0, column=2, sticky="e")

    # Small Textbox (Single Line)
    small_textbox = customtkinter.CTkTextbox(app, height=25, text_color="steelblue")
    small_textbox.insert("0.0", "Create a helpful explanation of the following text for revision, dont ask any questions and give just the response as it would appear in a revision guide:  ")
    small_textbox.grid(row=2, column=0, padx=10, pady=5, sticky="ew")

    # Main Textbox (Large)
    textbox = customtkinter.CTkTextbox(app)
    textbox.insert("0.0", "Enter text here: ")
    textbox.grid(row=3, column=0, sticky="nsew", padx=10, pady=5)

    # Console Textbox (Single Line - No Label)
    consoleTextbox = customtkinter.CTkTextbox(app, height=70, text_color="yellow")
    consoleTextbox.insert("0.0", "Console </>")
    consoleTextbox.grid(row=4, column=0, padx=10, pady=5, sticky="nsew")

    # Buttons Frame
    button_frame = customtkinter.CTkFrame(app, fg_color="transparent")
    button_frame.grid(row=5, column=0, pady=10)
    button_frame.grid_columnconfigure((0, 1), weight=1)

    compileButton = customtkinter.CTkButton(button_frame, text="Compile", corner_radius=20, height=40, width=200, command=compileAI)
    compileButton.grid(row=0, column=0, padx=10)

    statusButton = customtkinter.CTkButton(button_frame, text="Ready", corner_radius=20, height=40, width=200)
    statusButton.grid(row=0, column=1, padx=10)

    app.mainloop()

def setting():

    def save_settings():
        global typing_speed, randomness_level

        typing_speed = speed_entry.get()
        randomness_level = randomness_entry.get()

        print("Saved Typing Speed:", typing_speed)
        print("Saved Randomness Level:", randomness_level)

        settings_window.destroy()  # Close window after saving
        
    settings_window = customtkinter.CTkToplevel(app)
    settings_window.title("AutoTyper - Settings")
    settings_window.geometry("400x500")

    # Configure grid
    settings_window.grid_rowconfigure(tuple(range(10)), weight=1)
    settings_window.grid_columnconfigure(0, weight=1)

    # Return Button
    return_button = customtkinter.CTkButton(settings_window, text="Return", command=save_settings)
    return_button.grid(row=0, column=0, pady=10, sticky="n")

    # Settings Title
    title_label = customtkinter.CTkLabel(settings_window, text="Settings", font=("Arial", 30))
    title_label.grid(row=1, column=0, pady=2)

    # Description Text
    description_label = customtkinter.CTkLabel(settings_window,
                                               text="This is an open-source initiative to help the community.",
                                               wraplength=350, justify="center", font=("Arial", 14))
    description_label.grid(row=2, column=0, pady=2)

    # Speed Setting
    speed_label = customtkinter.CTkLabel(settings_window, text="Speed:", font=("Arial", 16))
    speed_label.grid(row=3, column=0, pady=2)

    speed_entry = customtkinter.CTkEntry(settings_window, placeholder_text="Typing Speed (e.g., 2)")
    speed_entry.grid(row=4, column=0, pady=2)

    speed_description = customtkinter.CTkLabel(settings_window, text="Speed at which the text is typed.",
                                               font=("Arial", 12), text_color="grey")
    speed_description.grid(row=5, column=0, pady=10)

    # Randomness Setting
    randomness_label = customtkinter.CTkLabel(settings_window, text="Randomness:", font=("Arial", 16))
    randomness_label.grid(row=6, column=0, pady=2)

    randomness_entry = customtkinter.CTkEntry(settings_window, placeholder_text="Randomness Level (e.g., 1)")
    randomness_entry.grid(row=7, column=0, pady=2)

    randomness_description = customtkinter.CTkLabel(settings_window, text="Adds variation to typing speed.",
                                                    font=("Arial", 12), text_color="grey")
    randomness_description.grid(row=8, column=0, pady=10)

def compile():
    global textbox, text, compileButton, statusButton
    text = textbox.get("0.0", "end")
    print(text)
    
    # Update Buttons
    compileButton.configure(text="Compiled", text_color="yellow")
    statusButton.configure(text="Press Keybind")
    
    type()

def compileAI():
    global textbox, text, compileButton, statusButton, small_textbox

    text = textbox.get("0.0", "end")
    print(text)

    context = small_textbox.get("0.0", "end")
    stream = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[{"role": "user", "content": context+text}],
        stream=True
        )
    #print("\nQwen: ", end="")
    consoleTextbox.delete("0.0", "end")
    for chunk in stream:
        #print(chunk["message"]["content"], end="", flush=True)
        consoleTextbox.insert("end", chunk["message"]["content"])

    
    # Update Buttons
    compileButton.configure(text="Compiled", text_color="yellow")
    statusButton.configure(text="Press Keybind")

    type()

def type():
    global text, typing_speed, randomness_level, statusButton, compileButton, typing_active
    print("Typing...")

    def start_typing():
        global typing_active

        typing_speed = 0.1
        randomness = 0.3

        base_speed = float(typing_speed) if typing_speed else 0.5
        variance = float(randomness) if randomness else 0.1

        for char in text.strip():
            if not typing_active:
                break
            pyautogui.write(char)
            delay = random.uniform(base_speed - variance, base_speed + variance)
            delay = max(0.01, delay)
            time.sleep(delay)

        compileButton.configure(text="Compile", text_color="white")
        statusButton.configure(text="Ready", text_color="white")
        typing_active = False
        print("Finished typing or stopped by user.")

    def on_hotkey():
        global typing_active

        if typing_active:
            typing_active = False
            statusButton.configure(text="Stopped", text_color="orange")
            print("Typing interrupted by user.")
            return

        print("Hotkey pressed! Starting typing...")
        typing_active = True
        statusButton.configure(text="Typing Text", text_color="red")

        # Start the typing process in a separate thread
        threading.Thread(target=start_typing, daemon=True).start()

    keyboard.unhook_all()
    keyboard.add_hotkey("`", on_hotkey)
    exit

splash_screen()