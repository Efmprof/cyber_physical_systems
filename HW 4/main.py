# Cyberphys GCODE generator
# 10/11/2021
import sys
import datetime


def box():
    print("; Printing box\n")
    z = 0
    while z <= 10:
        print(f"; {z}\n")
        print(f"G01 X0 Y0 Z{z}\n" +
              f"G01 X50 Y0 Z{z}\n" +
              f"G01 X50 Y10 Z{z}\n" +
              f"G01 X0 Y10 Z{z}\n" +
              f"G01 X0 Y0 Z{z}\n")
        z += 0.5


def lid(z: int):
    print("; Printing box lid\n")
    y = 0
    while y < 10:
        if y * 10 % 2 == 0:
            print(f"G01 X0 Y{y} Z{z}\n" +
                  f"G01 X50 Y{y} Z{z}\n")
        else:
            print(f"G01 X50 Y{y} Z{z}\n" +
                  f"G01 X0 Y{y} Z{z}\n")
        y += 0.5


def figures():
    print("; Printing figures\n")
    z = 10.5
    while z <= 60:
        print(f"; {z}\n")
        print(f"G00 X5 Y0 Z{z}")
        print(f"G03 X10 Y5 I0 J5")
        print(f"G03 X10 Y5 I-5 J0\n")

        radius = (5 - (((z - 10) / 50) * 2.5))
        print(f"G00 X{25 - radius} Y5 Z{z}")
        print(f"G02 X{25 - radius} Y5 I{radius} J0")
        print(f"G02 X{25 + radius} Y5 I{radius} J0\n")

        print(f"G00 X40 Y5 Z{z}")
        print(f"G03 X40 Y5 I5 J0")
        print(f"G03 X45 Y0 I5 J0\n")
        z += 0.5


def figureslid():
    print("; Printing figures lid\n")
    for i in range(5*2, 0, -1):
        print(f"G00 X{40 + i / 2} Y5 Z60")
        print(f"G03 X{40 + i / 2} Y5 I{5 - i / 2} J0\n")

    for i in range(int(2.5*2), 0, -1):
        print(f"G00 X{25 - 2.5 + i / 2} Y5 Z60")
        print(f"G02 X{25 - 2.5 + i / 2} Y5 I{2.5 - i / 2} J0\n")

    for i in range(5*2, 0, -1):
        print(f"G00 X{10 - i / 2} Y5 Z60")
        print(f"G03 X{10 - i / 2} Y5 I-{5 - i / 2} J0\n")


if __name__ == '__main__':
    sys.stdout = open('path.gcode', 'w')
    print(f"; Generated at {datetime.datetime.now()}\n")
    print("G21\n")
    lid(0)
    box()
    lid(10)
    figures()
    figureslid()
    sys.stdout.close()
