leiviskat = float(input("Anna leiviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

#muunnokset

naulat_yht = 32 * luodit_yht
luodit_yht = 13.3
leiviskat_yht = 20 * naulat_yht

massa_grammoina = (leiviskat * leiviskat_yht + naulat * naulat_yht + luodit * luodit_yht)
kilot = int(massa_grammoina// 1000)
grammat = (massa_grammoina % 1000)

print(f"{kilot} kilogrammaa ja {g} grammaa")

