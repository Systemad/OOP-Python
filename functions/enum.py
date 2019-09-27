import enum

class vatCalc(enum.Enum):
    INK_MOM = 1
    EX_MOMS = 2

def calculateVat(amount, inkORex):
    if inkORex == vatCalc.INK_MOMS:
        return amount * 0.20
    return amount * 0.25


print(calculateVat(1000, vatCalc.EX_MOMS))


