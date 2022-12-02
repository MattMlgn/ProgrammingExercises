#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import images

class colors:
    orange = (255, 128, 0)
    red = (255, 0, 0)
    gray = (128, 128, 128)
    green = (0, 255, 0)
    black = (0, 0, 0)

def movement(field, i, j, moves):
	dimension = 1
	history = [[j,i]]
	for move in moves.split():
		field[j][i] = colors.gray
		if 'N' in move:
			j -= 1
		elif 'S' in move:
			j += 1
		if 'E' in move:
			i += 1
			if ((move == 'NE' and ([j, i-1] and [j+1,i])) or (move == 'SE' and ([j, i-1] and [j-1, i]))) in history[-dimension::]:
				break
		elif 'W' in move:
			i -= 1
			if ((move == 'NW' and ([j+1,i] and [j,i+1])) or (move == "SW" and ([j, i+1] and [j-1,i]))) in history[-dimension::]:
				break
		if i > (len(field[0])-1):
			i = 0
		elif i<0:
			i= len(field[0])-1
		if j >(len(field[0])-1):
			j=0
		elif j<0:
			j= len(field)-1
		if field[j][i] == colors.orange:
			dimension += 1
		elif field[j][i] == colors.red:
			break
		if [j, i] in history[-dimension::]:
			break
		history.append([j, i])
	history.reverse()
	for i in range(dimension):
		field[history[i][0]][history[i][1]] = colors.green
	return dimension


def generate_snake(start_img: str, position: list[int, int], commands: str, out_img: str) -> int:
	l = images.load(start_img)
	dimension = movement(l, position[0], position[1],commands)
	images.save(l, out_img)
	return dimension
	
	


if __name__ == "__main__":
	generate_snake("./data/input_02.png", [28, 1], "S S S S S W W W W N N N N W N N N W N N N E SE SE SE SW SW SW N N N N N N NE N NW NE NW NE NW NE S E E E E E N E E S S S W S S S S S S S S S S S S S S S E S E SW S S S S W SE W S S SW SE S NW NE SE S NW S N NE W S NW SE SE E S S W NW NW W S NW N NW NE NW N E S SE SW SW E S E N SW SE SW S NW S NW E NW S S NE W S W NE S E S S NW SE S NW W S NW SE W N S NW E S S S SW NW SE S E NW SW SW W S S NE NE S N S S NW W S SE NW SE N SE NW S NW S S N S W SW S S SE NE SW SW S N E SW N N E S N S N S N N SE NW N S NW NE NW S SW NW SE NW SW S W SW E S E SW S SE S N S NE NW N W SW W W S NW S N E S NW S S SE SW NE N NW E NW N N NW NW S W SW SW W E W W E S E W NW W S S S S E S NE SW NW NE SW E NW N S NE S W SE SE N NW SE W SW W NW NW S S N W NE S E S W SW NE NE SW S N SE SW N S SW S NE E SW NE S W SE NW E NW NW SW S SW SW NW SE S NE NE NE SW E E S W NE SE SW SE NW W W SE S S S NW W SE SE NW NW E W S N SE W S NW W NE NW NE E NW NE N N SW N S S SE SW NE SE S SW NE N NE SE S SW S E E S S W N NW E SW N NW E W S SW W NW E NE N E N W S S N NW NW SW NE SW NE S S S W N NW SW NE NE SE E E S S S S SE NE NW S SW S S NW S S NW NE N NW W NW E S", "test_output.png")