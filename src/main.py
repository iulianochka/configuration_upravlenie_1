"""
Эмулятор командной оболочки. Вариант 16.
Этап 1: REPL (Read-Eval-Print-Loop)
"""
import sys


def print_error(message: str) -> None:
    """Выводит сообщение об ошибке."""
    print(f"Ошибка: {message}")


def handle_command(cmd: str, args: list) -> None:
    """
    Обрабатывает команду пользователя.
    
    :param cmd: имя команды
    :param args: аргументы команды
    """
    if cmd == "exit":
        print("Завершение работы эмулятора.")
        sys.exit(0)
    elif cmd == "ls":
        print(f"Команда: ls, аргументы: {args}")
    elif cmd == "cd":
        print(f"Команда: cd, аргументы: {args}")
    else:
        print_error(f"Неизвестная команда '{cmd}'")


def main() -> None:
    """Основной цикл программы (REPL)."""
    vfs_name = "default_vfs"
    print(f"Эмулятор оболочки. VFS: {vfs_name}")
    print("Введите 'exit' для выхода.\n")
    
    while True:
        try:
            user_input = input(f"[{vfs_name}] $ ")
        except EOFError:  
            # Корректная обработка прерывания (Ctrl+D или Ctrl+C)
            break
        
        parts = user_input.strip().split()
        if not parts:
            continue
        
        command = parts[0]
        arguments = parts[1:]
        
        handle_command(command, arguments)


if __name__ == "__main__":
    main()