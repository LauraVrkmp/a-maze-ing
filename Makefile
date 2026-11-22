# ************************************************************************* #
#                                                                           #
#                                                      :::      ::::::::    #
#  Makefile                                          :+:      :+:    :+:    #
#                                                  +:+ +:+         +:+      #
#  By: laveerka <laveerka@student.codam.nl>      +#+  +:+       +#+         #
#                                              +#+#+#+#+#+   +#+            #
#  Created: 2026/11/21 03:54:15 by laveerka        #+#    #+#               #
#  Updated: 2026/11/21 05:33:47 by laveerka        ###   ########.fr        #
#                                                                           #
# ************************************************************************* #

VENV = venv
PIP = $(VENV)/bin/python3 -m pip

install:
	sudo apt install -y clang libxcb1-dev libxcb-keysyms1-dev libvulkan-dev \
		mesa-vulkan-drivers zlib1g-dev libbsd-dev python3-venv
	@if [ ! -f mlx_CLXV/mlx-2.2-py3-none-any.whl ]; then $(MAKE) -C mlx_CLXV; fi
	python3 -m venv $(VENV)
	$(PIP) install mlx_CLXV/mlx-2.2-py3-none-any.whl