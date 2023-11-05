from random import choice


class Spell:  # Класс заклинание
    def __init__(self, name, page):
        self.name = name  # Имеет имя
        self.page = page  # И страницу в книге

    def getName(self):
        return self.name

    def getPage(self):
        return self.page


# Создаём книгу из 9 432 110 заклинаний, используя случайные названия
spellList = []
possibleNames = ["Infernal Flux", "Pyro Flash", "Mage Flare", "Fire Armor", "Mind Blast", "Ring of Demons", "Wave of Soul Fire", "Concentration of Strength", "Purification of Darkness", "Obliteration of Spirits", "Shadow Arrow", "Thunder Charge", "Mage Bomb", "Possess", "Tempest", "Burst of Greater Healing", "Flare of Chaotic Energy", "Delay of Stamina", "Abomination of Immortality", "Rage of Blessings"]
print("Заполняем книгу...")
for page in range(9432110):
    spellList.append( Spell(  # Добавляем в книгу новое заклинание
        choice(possibleNames),  # Берём случайный элемент из списка названий
        page  # Указываем страницу, на которой будет расположено заклинание
    ) )


# Функция для поиска заклинаний, передаём список и имя искомого заклинания
def findSpell(spellList, name):
    for spell in spellList:
        if spell.getName() == name:
            return spell.getPage()  # Если имя совпало с искомым, возвращаем номер страницы
    return -1  # Если ничего не найдено, возвращаем -1


print("Ищем заклинание Mage Flare...")
foundSpell = findSpell(spellList, "Mage Flare")  # Ищем например, заклинание "Mage Flare"
if foundSpell >= 0:
    print("Заклинание найдено на странице", foundSpell)
else:
    print("Заклинание не найдено")