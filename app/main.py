import sys

paths = os.environ["PATH"].split(":")


def get_executable_from_path(program) -> str | None:
    for path in paths:
        exe = os.path.join(path, program)
        if os.path.isfile(exe) and os.access(exe, os.X_OK):
            return exe

def main():

    built_in_commands = ["echo", "type", "exit"]

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
                else:
                    exe = get_executable_from_path(program)
                    if exe:
                        print(f"{program} is {exe}")
                    else:
                        print(f"{program}: not found")
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()