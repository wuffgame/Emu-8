from tkinter import filedialog

class Chip8:
    def __init__(self):
        self.memory = bytearray(4096)
    def load_rom(self):
        path = filedialog.askopenfilename()
        with open(path, "rb") as file:
            f = file.read()
            start = 0x200
            end = start + len(f)
            self.memory[start:end] = f
            print(self.memory)
            print(len(self.memory))


chip = Chip8()
chip.load_rom()