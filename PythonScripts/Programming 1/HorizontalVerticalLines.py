
# you want to use a matrix (list of lists) of integers (0-255) to represent
# an image, in which 0 is black, 255 is white and intermediate
# values are tones of gray.

# write a function that receives a nxm (n rows, m columns) matrix Mat
# and an integer value I (0 <= I < n) as input, and fills row I of Mat
# with the value 255

# for example, if Mat is the following:
# [[0, 0, 0],
# [0, 0, 0],
# [0, 0, 0]]
# and I is 1, then the content of Mat after calling the function is:
# [[0, 0, 0],
# [255, 255, 255],
# [0, 0, 0]]

# test your function by creating a nxm matrix Mat full of zeros, then
# call the function by providing Mat and I (0 <= I < n), and finally
# save the matrix content as an image, by calling the function
# images.saveG, passing Mat and a filename as parameter, for example:
# images.saveG(Mat, "outputfile.png")
# the outputfile.png is a png image corresponding to the content of Mat

# write another function that, following the same principle above,
# "draws" a column of 255 values in Mat, and test it

def Horizontal(Mat, I):
    Mat[I] = [255] * len(Mat)
  
def Vertical(Mat, J):
    for row in Mat:
      row[J] = 255
  
import images

if __name__ == "__main__":
  M = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
  Horizontal(M, 0)
  Horizontal(M, len(M)-1)
  Vertical(M, 0)
  Vertical(M, len(M[0])-1)
  
    
  images.saveG(M, "outputfile.png")