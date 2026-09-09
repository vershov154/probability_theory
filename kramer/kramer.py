# # 1.8, 1.9, 1.10, 1.11, 1.16, 1.17 1.38, 1.43, 1.48

# # Пример 1.8. В конкурсе по 5 номинациям участвуют 10 кино-
# # фильмов. Сколько существует вариантов распределения призов, ес-
# # ли по каждой номинации установлены: а) различные призы; б) оди-
# # наковые призы?

import itertools

# m = 10
# n = 5

# variantsA = len(list(itertools.product(range(m), repeat=n)))
# variantsB = len(list(itertools.combinations_with_replacement(range(m), r=n)))

# print(variantsA, variantsB)

# # Пример 1.9. Сколько существует семизначных чисел, состоя-
# # щих из цифр 4, 5 и 6, в которых цифра 4 повторяется 3 раза, а циф-
# # ры 5 и 6 - по 2 раза?

# digits = [4, 4, 4, 5, 5, 6, 6]

# variant = len(set(itertools.permutations(digits)))

# print(variant)

# # Пример 1.10. Буквы Т, Е, И, Я, Р, О написаны на отдельных
# # карточках. Ребенок берет карточки в случайном порядке и прикла-
# # дывает одну к друтой: а) 3 карточки; б) все 6 карточек. Какова ве-
# # роятность того, что получится слово: а) «ТОР»; б) «ТЕОРИЯ»?

# letters = ['Т', 'Е', 'И', 'Я', 'Р', 'О']

# variants3 = len(list(itertools.permutations(letters, r=3)))
# variants6 = len(list(itertools.permutations(letters)))
# Pa = 1 / variants3
# Pb = 1 / variants6
# print(variants3, variants6)
# print(f"{Pa:.5f}", f"{Pb:.5f}")

# # Пример 1.11. Используя условие примера 1.10, найти вероят-
# # ность того, что получится слово «АНАНАС», если на отдельных
# # карточках написаны три буквы А, две буквы Н и одна буква С.

# letters = ['А', 'А', 'А', 'Н', 'Н', 'С']
# variants = len(set(itertools.permutations(letters)))
# Pa = 1 / variants

# print(f"{variants:.5f}", f"{Pa:.5f}")

# # Пример 1.16. За круглым столом рассаживаются 5 мужчин и
# # 5 женщин. Найти вероятность того, что: а) никакие два лица одного
# # пола не сядут рядом; б) супруги сядут рядом, если эти мужчины и
# # женщины образуют 5 супружеских пар.

# variantsAll = len(list(itertools.permutations(range(10))))
# variantsMen = len(list(itertools.permutations(range(5))))
# variantsWomen = len(list(itertools.permutations(range(5))))

# Pa = (variantsMen * variantsWomen + variantsWomen * variantsMen) / variantsAll

# print(f"{Pa:.5f}")

# variantsCouple = len(list(itertools.permutations(range(5))))
# vrtsCplHW = variantsCouple * 2**5

# Pb = vrtsCplHW / variantsAll

# print(f"{Pb:.5f}")

# # Пример 1.17. В купейный вагон (9 купе по 4 места) семи пас-
# # сажирам продано 7 билетов. Найти вероятности того, что пассажи-
# # ры попали: а) в два купе; б) в семь купе; в) в три купе.

allseats = len(list(itertools.combinations(range(36), r=7)))
rooms_A = len(list(itertools.combinations(range(9), r=2)))
passengers_A = len(list(itertools.combinations(range(8), r=7)))

Pa = rooms_A * passengers_A / allseats

rooms_B = len(list(itertools.combinations(range(9), r=7)))
passengers_B = len(list(itertools.product(range(4), repeat=7)))

Pb = rooms_B * passengers_B / allseats

allcombinations = list(itertools.combinations(range(36), r=7))
C = 0

for i in allcombinations:
    full_rooms = set(seat // 4 for seat in i)
    if len(full_rooms) == 3:
        C += 1

Pc = C / allseats

print(f"а) {Pa:.7f}\nб) {Pb:.5f}\nв) {Pc:.5f}")

# # 1.38. Пятитомное собрание сочинений расположено на полке в
# # случайном порядке. Какова вероятность того, что книги стоят слева
# # направо в порядке нумерации томов (от 1 до 5)?

# variants = len(list(itertools.permutations(range(5))))
# P = 1 / variants
# print(f"{P:.4f}")

# # 1.43. Наудачу взятый телефонный номер состоит из 5 цифр.
# # Какова вероятность того, что в нем все цифры: а) различные;
# # б) одинаковые; в) нечетные? Известно, что номер телефона не на-
# # чинается с цифры ноль.

# digitsall = 9 * len(list(itertools.product(range(10), repeat=4)))

# digitsA = 9 * len(list(itertools.permutations(range(9), 4)))
# P_A = digitsA / digitsall

# digitsB = len(list(itertools.combinations(range(9), r=1)))
# P_B = digitsB / digitsall

# digitsC = len(list(itertools.product(range(5), repeat=5)))
# P_C = digitsC / digitsall

# print(f"а) {P_A:.4f} \n б) {P_B:.4f} \n в) {P_C:.4f}")

# # 1.48. В старинной игре в кости необходимо было для выигрыша
# # получить при бросании трех игральных костей сумму очков, превос-
# # ходящую 10. Найти вероятности: а) выпадения l l очков; б) выиг-
# # рыша.


# dice = [1, 2, 3, 4, 5, 6]

# allVariants = list(itertools.product(dice, repeat=3))
# allVariantsCount = len(allVariants)

# variantsA = 0
# variantsB = 0

# for i in allVariants:
#     current_sum = sum(i)
    
#     if current_sum == 11:
#         variantsA += 1

#     if current_sum > 10:
#         variantsB += 1

# Pa = variantsA / allVariantsCount
# Pb = variantsB / allVariantsCount

# print(f"a) {Pa}\nб) {Pb}")