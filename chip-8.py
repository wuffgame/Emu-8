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
            elif NN == 0xEE:
                print("Return from subrotine")
        elif first == 0x1:
            print(f"Jump to {hex(NNN)}")
        elif first == 0x2:
            print(f"Call subroutine at {hex(NNN)}")
        elif first == 0x3:
            print(f"Skip if V{X} == {NN}")
        elif first == 0x4:
            print(f"Skip if V{X} != {NN}")
        elif first == 0x5:
            print(f"Skip if V{X} == V{Y}")
        elif first == 0x6:
            self.register[X] = NN
            print(f"V{X} = {NN}")
        elif first == 0x7:
            print(f"V{X} += {NN}")
            self.register[X] = (self.register[X] + NN) % 256
        elif first == 0x8:
            if N == 0x0:
                print(f"V{X} = V{Y}")
            elif N == 0x1:
                print(f"V{X} = V{X} OR V{Y}")
            elif N == 0x2:
                print(f"V{X} = V{X} AND V{Y}")
            elif N == 0x3:
                print(f"V{X} = V{X} XOR V{Y}")
            elif N == 0x4:
                print(f"V{X} += V{Y} (with carry)")
            elif N == 0x5:
                print(f"V{X} -= V{Y}")
            elif N == 0x6:
                print(f"V{X} >>= 1")
            elif N == 0x7:
                print(f"V{X} = V{Y} - V{X}")
            elif N == 0xE:
                print(f"V{X} <<= 1")
        elif first == 0x9:
            print(f"Skip if V{X} != V{Y}")
        elif first == 0xA:
            print(f"I = {hex(NNN)}")
        elif first == 0xB:
            print(f"Jump to {hex(NNN)} + V0")
        elif first == 0xC:
            print(f"V{X} = random AND {NN}")
        elif first == 0xD:
            print(f"Draw sprite at V{X},V{Y} height {N}")
        elif first == 0xE:
            if NN == 0x9E:
                print(f"Skip if key V{X} pressed")
            elif NN == 0xA1:
                print(f"Skip if key V{X} not pressed")
        elif first == 0xF:
            if NN == 0x07:
                print(f"V{X} = delay_timer")
            elif NN == 0x0A:
                print(f"Wait for key, store in V{X}")
            elif NN == 0x15:
                print(f"delay_timer = V{X}")
            elif NN == 0x18:
                print(f"sound_timer = V{X}")
            elif NN == 0x1E:
                print(f"I += V{X}")
            elif NN == 0x29:
                print(f"I = font address for V{X}")
            elif NN == 0x33:
                print(f"Store BCD of V{X} at I")
            elif NN == 0x55:
                print(f"Store V0..V{X} to memory at I")
            elif NN == 0x65:
                print(f"Load V0..V{X} from memory at I")



chip = Chip8()
chip.load_rom()
i = 0
while i < 10:
    opcode = chip.fetch()
    print(hex(opcode))
    chip.execute(opcode)
    i += 1