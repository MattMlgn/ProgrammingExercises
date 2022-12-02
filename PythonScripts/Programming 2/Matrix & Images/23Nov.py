import images as img

l = img.load("input.png")

newVL = [x[::-1] for x in l]
newHL = list(l[::-1])
new90 = [[l[row][col] for row in range(len(l) - 1, -1, -1)] for col in range(len(l[0]))]

newIMG = [[(0, 0, 0)] * 200 for _ in range(100)]

img.save(new90,"output.png")