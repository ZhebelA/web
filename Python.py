stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}

max = 0

for key, value in stats.items():
  if value > max:
    max = value
    name = key
print(f'Канал с максимальным объемом продаж: {name}')
