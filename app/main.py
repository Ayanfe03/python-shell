import sys


def main():

    built_in_commands = ["echo", "exit", "type"]

    while True:
        sys.stdout.write("$ ")

        command = input()
        new_command = command.split()
        first = new_command[0]

        if first == "exit":
            break
        elif first == "echo":
            print(" ".join(new_command[1:]))
        elif first == "type":
            if len(new_command) < 2:
                continue
            elif new_command[1] in built_in_commands:
                print(f"{new_command[1]} is a shell builtin")
            elif new_command[1] not in built_in_commands:
                print(f"{new_command[1]}: not found")
        else:
            print(f"{command}: command not found")
            


if __name__ == "__main__":
    main()
