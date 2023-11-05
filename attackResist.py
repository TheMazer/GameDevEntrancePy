# Input data
sword_dmg = input().split()
bow_dmg, spell_dmg = input().split()
physicResist, magicResist = input().split()

possibleDamages = []

# Count Sword
possibleDamages.append((int(sword_dmg[0]) - int(physicResist)) + (int(sword_dmg[1]) - int(magicResist)))

# Count Bow
possibleDamages.append(int(bow_dmg) - int(physicResist))

# Count Spell
possibleDamages.append(int(spell_dmg) - int(magicResist))

print(max(possibleDamages))