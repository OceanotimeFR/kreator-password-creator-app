from PasswordCreator import PasswordCreator
from imports import tk, ttk, ctypes, colors

class UI():
    def __init__(self):
        self.winX = 720
        self.winY = 360
        self.pwdClass = PasswordCreator()

        self.root = tk.Tk()
        self.style = ttk.Style(self.root)

        self.pwdLabel = None 


    def winCustom(self):
        self.root.title("KreatoR - Password Generator")
        self.root.geometry(f"{self.winX}x{self.winY}")
        
        self.style.theme_use('clam')
        self.root.configure(bg=colors.darkGrey)

        self.style.configure("TLabel", background=colors.darkGrey, foreground=colors.White, font=("Helvetica", 12))
        self.style.configure("TButton", background=colors.darkGreen, foreground=colors.darkGrey, font=("Helvetica", 11))
        self.style.configure("TEntry",font=("Helvetica", 12), 
                             fieldbackground=colors.darkGrey, 
                             foreground=colors.White)
        
        self.style.map("TButton",
                        background=[("active",colors.Green)],
                        foreground=[("active",colors.White)])

        titleLabel = ttk.Label(self.root, text="KreatoR", font=("Segoe UI", 16, "bold"))
        titleLabel.pack(pady=10)

        charCountLabel = ttk.Label(self.root, text="Input a number of characters :")
        charCountLabel.pack()

        charCountEntry = ttk.Entry(self.root, font=('Helvetica',12), justify='center', style='TEntry')
        charCountEntry.pack(pady=5)

        def pwdCreation():
            charEntry = charCountEntry.get()
            try:
                self.pwdClass.pwdLength = int(charEntry)
                self.pwdClass.creator()
            except Exception as e:
                ctypes.windll.user32.MessageBoxW(0, str(e), "Erreur", 0x10)

            if self.pwdLabel:
                self.pwdLabel.config(text=self.pwdClass.pwd)
            else : 
                self.pwdLabel = ttk.Label(self.root, text=self.pwdClass.pwd)
                self.pwdLabel.pack()
        
        validateEntryButton = ttk.Button(self.root,text="Valider", style="TButton", command=pwdCreation)
        validateEntryButton.pack(pady=15, padx=10)
    

    def launcher(self):
        self.winCustom()
        self.root.mainloop()