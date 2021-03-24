from lexer import Lexer

testFile = "C:\\dev_py\\tta assembler\\test\\test_assembly.txt"

symbolTable = {}
literalTable = {} 

lxer = Lexer(testFile)

def firstPass():
    lxer.run()

def secondPass():
    pass

def main():
    firstPass()
    secondPass()

if __name__ == "__main__":
    main()