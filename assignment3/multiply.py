import MapReduce
import sys

"""
Matrix Multiply Assignment in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def genkey(i, j):
    return (i, j)

def mapper(record):
    m = record[0]
    i = record[1]
    j = record[2]
    v = record[3]
    if m == "a":
        for j in range(5):
            key = genkey(i, j)
            value = record
            mr.emit_intermediate(key, value)
    if m == "b":
        for i in range(5):
            key = genkey(i, j)
            value = record
            mr.emit_intermediate(key, value)

def reducer(key, list_of_values):
    # make dict of matrix a values and matrix b values
    a = {}
    b = {}
    for record in list_of_values:
        m = record[0]
        i = record[1]
        j = record[2]
        v = record[3]
        if m == "a":
            a[genkey(i, j)] = v
        if m == "b":
            b[genkey(i, j)] = v
    
    sum = 0

    i = key[0]
    j = key[1]
    
    for k in range(5):
        akey = genkey(i, k)
        bkey = genkey(k, j)
        aval = a.get(akey, 0)
        bval = b.get(bkey, 0)
        sum += (aval * bval)
    mr.emit((i, j, sum))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
