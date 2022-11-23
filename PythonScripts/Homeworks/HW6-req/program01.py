#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import images

class Colors:
	Orange = (255, 128, 0)
	Red = (255, 0, 0)
	Gray = (128, 128, 128)
	Green = (0, 255, 0)


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
	l = images.load("data/input_00.png")
	for r_idx, row in enumerate(l):
		for c_idx, column in enumerate(row):
			if sum(column) != 0:
				l[r_idx][c_idx] = Colors.Red
				#print(column)

	images.save(l,"test_output.png")

if __name__ == "__main__":
	generate_snake("",[],"","")