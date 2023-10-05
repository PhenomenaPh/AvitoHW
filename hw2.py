import csv
from typing import List, Tuple, Dict


def read_csv(file_name: str) -> List[List[str]]:
    """
    Читает csv-файл в список списков

    Параметры:
    - file_name: имя csv-файла

    Возвращает:
    - список списков со строками файла
    """
    data = []
    with open(file_name, encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            data.append(row)
    return data[1:]


def get_departments(data: List[List[str]]) -> List[str]:
    """
    Извлекает уникальные названия департаментов

    Параметры:
    - data: данные из csv

    Возвращает:
    - список названий департаментов
    """
    departments = set()
    for row in data:
        departments.add(row[1])
    return list(departments)


def get_teams(data: List[List[str]]) -> Dict[str, List[str]]:
    """
    Cоздает словарь "департамент - отделы"

    Параметры:
    - data: данные из csv

    Возвращает:
    - словарь "департамент - список отделов"
    """
    teams = {}

    for row in data:
        department = row[1]
        team = row[2]

        if department not in teams:
            teams[department] = []

        # Проверяем, что команды нет в списке
        if team not in teams[department]:
            teams[department].append(team)

    return teams


def print_teams_hierarchy(teams: Dict[str, List[str]]):
    """
    Печатает иерархию команд

    Параметры:
    - teams: словарь "департамент - список команд"
    """
    for department, department_teams in teams.items():
        print(department)
        for team in set(department_teams):
            print(f"- {team}")
        print()


def get_dept_stats(
    data: List[List[str]],
) -> List[Tuple[str, int, int, int, int]]:
    """
    Считает статистику по департаментам

    Параметры:
    - data: данные из csv

    Возвращает:
    - список кортежей вида (название департамента, численность,
    мин. зарплата, макс. зарплата, средняя зарплата)
    """
    depts = {}

    for row in data:
        dept = row[1]
        salary = int(row[5])

        if dept not in depts:
            depts[dept] = {"count": 0, "min": salary, "max": salary, "sum": 0}

        depts[dept]["count"] += 1
        depts[dept]["min"] = min(depts[dept]["min"], salary)
        depts[dept]["max"] = max(depts[dept]["max"], salary)
        depts[dept]["sum"] += salary

    stats = []
    for dept, dept_stats in depts.items():
        avg = round(dept_stats["sum"] / dept_stats["count"])
        stats.append(
            (
                dept,
                dept_stats["count"],
                dept_stats["min"],
                dept_stats["max"],
                avg,
            )
        )

    return stats


def print_dept_stats(stats: List[Tuple[str, int, int, int, int]]):
    """
    Выводит сводную статистику по департаментам

    Параметры:
    - stats: статистика в виде списка кортежей
    (название, численность, мин. зп, макс. зп, средняя зп)
    """

    d, h, min_zp, max_zp, avg_zp = (
        "Департамент",
        "Численность",
        "Мин зп",
        "Макс зп",
        "Средняя зп",
    )
    print(f"{d:<20}{h:^10}{min_zp:^10}{max_zp:^10}{avg_zp:^10}")

    # Вывод данных
    for dept, count, min_sal, max_sal, avg_sal in stats:
        count = str(count).center(10)
        min_sal = str(min_sal).center(10)
        max_sal = str(max_sal).center(10)
        avg_sal = str(avg_sal).center(10)
        print(
            f"{dept:20} {str(count).center(10)} {min_sal} {max_sal} {avg_sal}"
        )


def save_stats(stats: List[Tuple[str, int, int, int, int]], file_name: str):
    """
    Сохраняет статистику по департаментам в csv-файл

    Параметры:
    - stats: статистика в виде списка кортежей
    - file_name: имя файла для записи

    Возвращает: None
    """
    with open(file_name, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(
            ["Департамент", "Численность", "Мин зп", "Макс зп", "Средняя зп"]
        )
        for row in stats:
            writer.writerow(row)


if __name__ == "__main__":
    file_name = "Corp Summary.csv"
    data = read_csv(file_name)

    while True:
        print("Меню:")
        print("1. Вывести иерархию команд")
        print("2. Вывести сводный отчет")
        print("3. Сохранить сводный отчет")
        print("4. Выход")

        choice = input("Выберите пункт меню: ")
        if choice == "1":
            teams = get_teams(data)
            print_teams_hierarchy(teams)
        elif choice == "2":
            stats = get_dept_stats(data)
            print_dept_stats(stats)
        elif choice == "3":
            stats = get_dept_stats(data)
            save_stats(stats, "dept_stats.csv")
            print("Отчет сохранен в dept_stats.csv")
        elif choice == "4":
            break
        else:
            print("Неверный пункт меню")
