import sys
import os
import shutil

def main():

    built_in_commands = ["echo", "type", "exit"]

    while True:
        sys.stdout.write("$ ")

        command = input().strip()
        if not command:
            continue

        new_command = command.split()
        first = new_command[0]

        if first == "exit":
            break
        elif first == "echo":
            print(" ".join(new_command[1:]))
        elif first == "type":
            if len(new_command) < 2:
                continue

            cmd = new_command[1]

            if cmd in built_in_commands:
                print(f"{cmd} is a shell builtin")

            # Accessing path without shutil
            #
            # else:
            #     path_env = os.environ.get("PATH", "")
            #     directories = path_env.split(os.pathsep) if path_env else []
            #
            #     found = False
            #     for directory in directories:
            #         full_path = os.path.join(directory, cmd)
            #         if os.path.exists(full_path):
            #             if os.access(full_path, os.X_OK):
            #                 print(f"{cmd} is {full_path}")
            #                 found = True
            #                 break
            #
            #     if not found:
            #         print(f"{cmd}: not found")


            # Shutil loops through all PATH directories, automatically resolves extension type
            else:
                full_path = shutil.which(cmd)
                if full_path:
                    print(f"{cmd} is {full_path}")
                else:
                    print(f"{cmd}: not found")
        else:
            print(f"{first}: command not found")



if __name__ == "__main__":
    main()