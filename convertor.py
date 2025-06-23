import argparse

parser = argparse.ArgumentParser(description="A simple addition program")

parser.add_argument("toCel", nargs = "*", metavar = "str",type= str ,help="C: To Celsius, F:To Fahrenheit")
parser.add_argument("temp", nargs="*", metavar="num", type=int, help="Temp to convert")
###Pass the argument for example if you want to convert 32 F to Celsius then type in cmd python convertor.py C 32


args = parser.parse_args()

toCon = args.toCel
#toCon returns a list of arguments in string
if(len(toCon)!=0):
    temp = int(toCon[1])
    if toCon[0] == "C":
        Cel = ((temp-32)*0.55)
        print("The temperature in Cesius is",Cel)
    else:
        Fah = (temp*0.555) + 32
        print("The temperature in Fahrenheit is",Fah)