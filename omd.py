def step2_umbrella() -> None:
    """
    Печатает высказывание о том, что малярная утка взяла зонтик
    и релоцировалась.

    :return: None
    """
    print('Утка-маляр 🦆 взяла зонтик ☂️ и пошла релоцироваться.')
    return None


def step2_no_umbrella() -> None:
    """
    Печатает высказывание о том, что малярная утка не взяла зонтик и утонула.

    :return: None
    """
    print('Утка-маляр 🦆 не взяла зонтик ☂️ и пошла утонула.')
    return None


def step1():
    print(
        'Утка-маляр 🦆 решила выпить зайти в бар. '
        'Взять ей зонтик? ☂️'
    )
    option = ''
    options = {'да': True, 'нет': False}
    while option not in options:
        option = input('Choose: {}/{} '.format(*options)).lower()

    if options[option]:
        return step2_umbrella()
    return step2_no_umbrella()


if __name__ == '__main__':
    step1()
