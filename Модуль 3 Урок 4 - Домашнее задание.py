def single_root_words(root_word, *other_words):
    if isinstance(root_word, str) == False:
        return f"Ошибка! Входные данные должны содержать только буквы алфавита и быть похожими на слово для поиска."
    else:
        same_words = []
        for i in other_words:
            if root_word.lower() in i.lower():
                same_words.append(i)
        return same_words

result1 = single_root_words("Секрет", "суперсекрет", "мегоСекрет", "ПростоСекрет", "Дерево", "ещёСекрет")
result2 = single_root_words("Банан", "банан", "банАновый", "БананЧатый", "Вишнёвый", "яблоко", "бананоОбразный")
result3 = single_root_words("АбВг", "Машина", "небо", "Дом", "телевизор", "огурец", "Дорога")
result4 = single_root_words(16, "Луна", "лунный", "Солнце", "Космос", "ветер", "Вода")
print(result1)
print(result2)
print(result3)
print(result4)
