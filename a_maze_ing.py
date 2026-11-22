# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/21 03:09:09 by laveerka        #+#    #+#               #
#  Updated: 2026/11/21 05:49:52 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
from typing import Any
from mlx import Mlx


def activate_env() -> None:
    print("Create your virtual environment with:")
    print("- python3 -m venv venv")
    print("Activate your virtual environment:")
    print("- source venv/bin/activate")
    sys.exit(1)


def check_arguments() -> None:
    if len(argv) == 2 and argv[1] == "config.txt":
        return
    print("Run the program as such:")
    print("python3 a-maze-ing.py config.txt")
    sys.exit(1)


def read_config(file: str) -> dict[str, Any]:
    try:
        with open(file, "r") as f:
            lines = f.read()
    except (FileNotFoundError, PermissionError) as e:
        print(f"Error opening file '{file}': {e}")
        sys.exit(1)
    required = [WIDTH, HEIGHT, ENTRY, EXIT, OUTPUT_FILE, PERFECT]
    config = {}
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            config[key] = value
        else:
            print("Config file is invalid")
            sys.exit(1)
    missing = [item for item in required if item not in config]
    if missing:
        print(f"Config file is missing keys: {', '.join(missing)}")
        sys.exit(1)
    for item in config:
        if item == "WIDTH" or item == "HEIGHT":
            try:
                config[item] = int(config[item])
            except ValueError as error:
                print(f"Invalid value for {item}: {error}")
        elif item == "ENTRY" or item == "EXIT":
            try:
                xy = config[item].split(",", 1)
                if len(xy) != 2:
                    raise ValueError(f"Invalid value for {item}: {}")
                config[item] = (int(x), int(y))
                else:


    


def main() -> None:
    if sys.prefix == sys.base_prefix:
        activate_venv()
    check_arguments()
    config = read_config(argv[1])

if __name__ == "__main__":
    main()
