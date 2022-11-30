'''
In function skip_tuples with variable tuples
    return the slice of tuples
In function main 
    print the output from the skip_tuples function
Run the main function
'''
def skip_tuples(tuples):
    return tuples[::2]
def main():
    tupleInput = ('I', 'am', 'a', 'test', 'tuple')
    print(skip_tuples(tupleInput))
main()