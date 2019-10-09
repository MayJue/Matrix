## TODO
## Implement a helper function to return the dot product of a 1 x n vector and
## an n x 1 vector - i.e. a row and a column.  They must be the same length,
## otherwise the function needs to exit without error.
def dot( vec1, vec2 ):

    print("dot")





class Matrix():

    ## Initialize a Matrix object with an input matrix, stored as a list-of-lists.
    def __init__( self, matrix ):
        self.matrix = matrix
        print(matrix)
        ## TODO
        ## Implement a class attribute to keep track of the matrix values.
        ## This attribute just stores the input data.  Be sure to check that
        ## 'matrix' is a list of lists before setting this value.
        ## REMINDER: set a class attribute by using 'self.attr_name = value'.






        ## TODO
        ## Implement class attributes to keep track of the number of rows and the
        ## number of columns.  You can use these to compare dimensions.



    ## TODO
    ## Implement helper function that returns the i-th row in the matrix.
    ## Should return a list of numbers (e.g. a 1 x m matrix).
    def get_row( self, i ):
        pass




    ## TODO
    ## Implement helper function that returns the j-th column in the matrix.
    ## Should return a list of lists, each of size 1 (e.g. an n x 1 matrix).
    def get_col( self, j ):
        pass



    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the sum of self and other.
    def add( self, other ):


        pass


    ## TODO
    ## Check that the dimensions of self and other are compatible.
    ## Return a Matrix equal to the difference of self and other.
    def sub( self, other ):

        pass




    ## TODO
    ## First, check whether other is a scalar or a matrix.
    ## If it is a scalar, return the product other * self.
    ## If it is a Matrix, return the matrix product of self
    ## and other.  This is to be accomplished by using the
    ## dot function defined above.
    def mult( self, other ):

        pass



    ## TODO
    ## Return a Matrix that is the transpose of self.
    def transpose( self ):
        pass


def main():
    matrix = [[1,2,3]]
    Matrix(matrix)
main()
