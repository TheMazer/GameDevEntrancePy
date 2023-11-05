def calculateDamage(initial_damage, seconds):
    damage_per_strike = initial_damage
    total_damage = 0

    # Два удара в секунду
    for second in range(seconds * 2):
        total_damage += damage_per_strike  # Прибавляем нанесённый урон к суммарному
        damage_per_strike -= 1  # Рыцарь устаёт

    return total_damage  # Возвращаем суммарный нанесённый урон рыцарем


initial_damage = 117  # Начальный урон, наносимый рыцарем
seconds = 11  # Время атаки
total_damage = calculateDamage(initial_damage, seconds)  # Считаем суммарный урон
print("Суммарный урон, нанесенный рыцарем:", total_damage)