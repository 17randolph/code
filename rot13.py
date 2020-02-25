
import tkinter as tk

decrypted = b"abcdefghijklmnopqrstuvwxyz "
encrypted = b"nopqrstuvwxyzabcdefghijklm "
encrypt_table = bytes.maketrans(decrypted, encrypted)
decrypt_table = bytes.maketrans(encrypted, decrypted)

class App:
    def __init__(self, master):
        master.title('Rot13 Encrypter/Decrypter')
        master.geometry('400x300')

        self.master = master
        self.create_widgets()
        font_specs = ('courier', 18)

    def create_widgets(self):
        # user input
        self.input = tk.Text(master, font=('courier', 12))
        self.scroll = tk.Scrollbar(master, command=self.input.yview)
        self.input.configure(height=6,width=40 ,yscrollcommand=self.scroll.set)
        self.input.pack(side='top')

        self.encrypt_btn = tk.Button(master, text='Encrypt', command=self.encrypt_text)
        self.encrypt_btn.pack(pady=15)

        self.decrypt_btn = tk.Button(master, text='Decrypt', command=self.decrypt_text)
        self.decrypt_btn.pack(pady=5)

        self.output = tk.Text(master, font=('courier', 12))
        self.scrollB = tk.Scrollbar(master, command=self.input.yview)
        self.output.configure(height=8, width=40, yscrollcommand=self.scrollB.set)
        self.output.pack(side='bottom')

    def encrypt_text(self):
        input_content = self.input.get(1.0, tk.END)
        input_content = input_content.lower()
        result = input_content.translate(encrypt_table)
        self.output.delete(1.0, tk.END)
        self.output.insert(1.0, result)
        print('encrypted')

    def decrypt_text(self):
        output_content = self.output.get(1.0, tk.END)
        output_content = output_content.lower()
        result = output_content.translate(encrypt_table)
        self.input.delete(1.0, tk.END)
        self.input.insert(1.0, result)
        print('decrypted')

if __name__ == '__main__':
    master = tk.Tk()
    app = App(master)
    master.mainloop()
