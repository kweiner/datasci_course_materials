import MapReduce
import sys

"""
Asymmetric Friendships Assignment in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: person A
    # value: person B - a friend of person A
    pA = record[0]
    pB = record[1]
    pAB = sorted(record)
    persons = " ".join(pAB)
    mr.emit_intermediate(persons, 1)

def reducer(key, list_of_values):
    # key: person A and B
    # value: 1 for every occurance
    persons = key.split()
    total = 0
    for v in list_of_values:
      total += v
    #print persons, total
    if total < 2:
        pA = persons[0]
        pB = persons[1]
        mr.emit((pA, pB))
        mr.emit((pB, pA))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
