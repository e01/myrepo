# -*- coding: utf-8 -*-
'''
Задание 9.4

Создать функцию, которая обрабатывает конфигурационный файл коммутатора
и возвращает словарь:
* Все команды верхнего уровня (глобального режима конфигурации), будут ключами.
* Если у команды верхнего уровня есть подкоманды, они должны быть в значении у соответствующего ключа, в виде списка (пробелы в начале строки можно оставлять).
* Если у команды верхнего уровня нет подкоманд, то значение будет пустым списком

Функция ожидает в качестве аргумента имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt

При обработке конфигурационного файла, надо игнорировать строки, которые начинаются с '!',
а также строки в которых содержатся слова из списка ignore.

Для проверки надо ли игнорировать строку, использовать функцию ignore_command.


Ограничение: Все задания надо выполнять используя только пройденные темы.
'''

ignore = ['duplex', 'alias', 'Current configuration']


def ignore_command(command, ignore):
    '''
    Функция проверяет содержится ли в команде слово из списка ignore.

    command - строка. Команда, которую надо проверить
    ignore - список. Список слов

    Возвращает
    * True, если в команде содержится слово из списка ignore
    * False - если нет
    '''
    return any(word in command for word in ignore)

def exclude_commands(filename="config_sw1.txt",del_excl=True):
    parsed_cfg = []
    with open(filename) as f:
        for line in f:
            if del_excl and line.startswith('!'):
                pass
            elif ignore_command(line, ignore):
                pass
            elif not line.strip():
                pass
            else:
                parsed_cfg.append(line.rstrip())
    return parsed_cfg

print(exclude_commands())

#def parse_config(config_file=config_sw1.txt):
#    ''' Check config and parse all high level commands, function return dte dictionary with all high level commands, the keys are the subcommands (if applicatible)'''
#    with open(config_file) as f:
#        cfg = f.readlines()
#        for line in range(0, len(cfg_lines)):
#            command = cfg[line]