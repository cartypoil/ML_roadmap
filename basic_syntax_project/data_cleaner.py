def parse_age(value):
    try:
        age = int(value)
        if 0 < age <= 120:
            return age
    except (ValueError, TypeError):
        return None


def clean_ages(raw_list):
    valid_ages = []
    invalid_ages = []
    for step, item in enumerate(raw_list, start=1):
        age = parse_age(item)
        if age is not None:
            valid_ages.append(age)
        else:
            invalid_ages.append((step, item))

    return valid_ages, invalid_ages


def get_stats(valid_ages):
    if not valid_ages:
        return None
    ages = sorted(set(valid_ages))
    count_unique = len(ages)
    sum_age = sum(ages)
    avg_age = round(sum_age / count_unique, 1)
    return {'ages': ages,
            'count': len(valid_ages),
            'count_unique': count_unique,
            'min_age': min(ages),
            'max_age': max(ages),
            'sum_age': sum_age,
            'avg_age': avg_age
            }


if __name__ == '__main__':
    raw_ages = [25, '30', -5, None, 'ошибка', 145, 25, '18', 0, '42']
    valid_ages, invalid_ages = clean_ages(raw_ages)
    stats = get_stats(valid_ages)

    if stats is not None:
        for key, value in stats.items():
            print(f'Полученные данные: {key}: {value}')
        for step, item in invalid_ages:
            print(f'Была ошибка в {step} элементе, его значение: {item}')
    else:
        print('Нормальных данных не нашлось')
