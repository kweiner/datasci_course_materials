import MapReduce
import sys

"""
Friend Count Assignment in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person A
    # value: person B - a friend of person A
    pA = record[0]
    pB = record[1]
    mr.emit_intermediate(pA, 1)

def reducer(key, list_of_values):
    # key: person A
    # value: value 1 for each friend of person A
    total = 0
    for v in list_of_values:
      total += v
    mr.emit((key, total))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
