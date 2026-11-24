# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  a_maze_ing.py                                     :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka                                  +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/21 03:09:09 by laveerka        #+#    #+#               #
#  Updated: 2026/11/24 12:11:00 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

import sys
from typing import Any


def activate_venv() -> None:
    print("Create your virtual environment with:")
    print("- python3 -m venv venv")
    print("Activate your virtual environment:")
    print("- source venv/bin/activate")
    sys.exit(1)


def check_arguments() -> None:
    if len(sys.argv) == 2 and sys.argv[1] == "config.txt":
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
    required = ["WIDTH", "HEIGHT", "ENTRY", "EXIT", "OUTPUT_FILE", "PERFECT"]
    config = {}
    for line in lines:
        if "=" in line:
            key, value = line.split("=", 1)
            config[key.strip()] = value.stip()
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
                    raise ValueError(f"Invalid value for {item}: {xy}")
                config[item] = (int(xy[0]), int(xy[1]))
            except ValueError as error:
                print(f"Invalid value for {item}: {error}")
        elif item == "OUTPUT_FILE":
            if config[item].endswith(".txt") and len(config[item]) > 4:
                continue
            else:
                raise ValueError(f"Invalid value for {item}: {config[item]}")
        elif item == "PERFECT":
            if isinstance(config[item], bool):
                continue
            else:
                raise ValueError(f"Invalid value for {item}: {config[item]}")
        else:
            print(f"Included other key: {item}")
    return config


def main() -> None:
    if sys.prefix == sys.base_prefix:
        activate_venv()
    check_arguments()
    config = read_config(sys.argv[1])
    print(f"{config}")


if __name__ == "__main__":
    main()
