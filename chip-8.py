from tkinter import filedialog

class Chip8:
    def __init__(self):
        self.memory = bytearray(4096)
        self.pc = 0x200
        self.register = bytearray(16)
        self.i = 0

    def load_rom(self):
        path = filedialog.askopenfilename()
        with open(path, "rb") as file:
            f = file.read()
            start = 0x200
            end = start + len(f)
            self.memory[start:end] = f

    def fetch(self):
        opcode = (self.memory[self.pc] << 8) | self.memory[self.pc + 1]
        self.pc += 2
        return opcode

    def decode(self, opcode):
        first = (opcode & 0xF000) >> 12
        X = (opcode & 0x0F00) >> 8
        Y = (opcode & 0x00F0) >> 4
        N = (opcode & 0x000F)
        NN = (opcode & 0x00FF)
        NNN = (opcode & 0x0FFF)
        return first, X, Y, N, NN, NNN

    def execute(self, opcode):
        first, X, Y, N, NN, NNN = self.decode(opcode)
        if first == 0x0:
            if NN == 0xE0:
                print("Cleaning screen!!!")



chip = Chip8()
chip.load_rom()
opcode = chip.fetch()
print(hex(opcode))
chip.execute(opcode)