import MapReduce
import sys

"""
Unique Trim Assignment in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: sequence ID
    # value: nucleotides string
    seqid = record[0]
    n = record[1]
    n_stripped = n[:-10]
    mr.emit_intermediate(n_stripped, 1)

def reducer(key, list_of_values):
    # key: stripped nucleotides
    # value: doesn't matter - we ignore it
    mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
