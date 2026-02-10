leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

naulat_yht = leiviskat * 20 + naulat
luodit_yht = leiviskat * 32 + luodit
grammat = luodit_yht * 13.3

kg = int(grammat // 1000)
g = int(grammat % 1000)

print(f"Massa: {kg} kiloa ja {g} grammaa")
