import images as img, MatrixImages as MI

M = MI.createMatrix(100,100,(255,255,153))
M = MI.drawHorizontalLine(M, 50, (229,145,81))
M = MI.drawVerticalLine(M, 2, (229,145,81))
img.save(M, "output.png")

